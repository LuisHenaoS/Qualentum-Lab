import boto3
from moto import mock_aws
import pytest


@pytest.fixture
def ec2():
    # EC2 simulado usando pero con moto
    with mock_aws():  # simulacion de AWS para este bloque
        yield boto3.resource('ec2', region_name='eu-west-3')  # region para la simulacion


@pytest.fixture
def security_group(ec2):
    # grupo de seguridad simulado
    client = ec2.meta.client
    sg = client.create_security_group(GroupName='test-sg', Description='Test security group')
    yield sg['GroupId']


def test_create_ec2_instance(ec2, security_group, monkeypatch):
    from aws_cli import create_ec2_instance

    def mock_create_ec2_instance(instance_type, image_id, key_name, security_group_id, region):
        # mock para simular la creación de un EC2
        instances = ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            KeyName=key_name,
            SecurityGroupIds=[security_group_id]
        )
        return instances[0].id

    # función original create_ec2_instance a versión mock durante el test
    monkeypatch.setattr("aws_cli.create_ec2_instance", mock_create_ec2_instance)
    instance_id = create_ec2_instance('t2.micro', 'ami-0c55b159cbfafe1f0', 'my-key-pair', security_group,
                                      'eu-west-3')  # argumentos requeridos.
    instances = list(ec2.instances.all())  # instancias EC2 simuladas.
    assert len(instances) == 1  # comprobacion de instancia creada
    assert instances[0].instance_type == 't2.micro'  # verifica el tipo


def test_terminate_ec2_instance(ec2, security_group, monkeypatch):
    from aws_cli import terminate_ec2_instance

    # instancia EC2
    instance = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='my-key-pair',
        SecurityGroupIds=[security_group]
    )[0]

    def mock_terminate_ec2_instance(instance_id, region):
        # mock para simular el EC2
        ec2.Instance(instance_id).terminate()

    # funcion terminate_ec2_instance a mock para el test como antes
    monkeypatch.setattr("aws_cli.terminate_ec2_instance", mock_terminate_ec2_instance)
    terminate_ec2_instance(instance.id, 'eu-west-3')  # termina la instancia  mock y la region
    instance.reload()
    assert instance.state['Name'] == 'terminated'  # verificacion


def test_start_ec2_instance(ec2, security_group, monkeypatch):
    from aws_cli import start_ec2_instance

    instance = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='my-key-pair',
        SecurityGroupIds=[security_group]
    )[0]
    instance.stop()
    instance.wait_until_stopped()

    def mock_start_ec2_instance(instance_id, region):
        ec2.Instance(instance_id).start()

    monkeypatch.setattr("aws_cli.start_ec2_instance", mock_start_ec2_instance)
    start_ec2_instance(instance.id, region='eu-west-3')
    instance.reload()
    assert instance.state['Name'] == 'running'
