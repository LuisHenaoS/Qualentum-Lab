import boto3
import click
from botocore.exceptions import NoCredentialsError, \
    PartialCredentialsError


# instancia EC2 del tipo especificado.
def create_ec2_instance(instance_type, image_id, key_name, security_group_id, region):
    try:
        ec2 = boto3.resource('ec2', region_name=region)
        # crea el EC2 con parámetros
        instance = ec2.create_instances(
            ImageId=image_id,  # ID de la AMI
            InstanceType=instance_type,  # tipo de instancia
            MinCount=1,  # mínimo de instancias
            MaxCount=1,  # máximo de instancias
            KeyName=key_name,  # key pair configurada en AWS
            SecurityGroupIds=[security_group_id]  # ID de seguridad
        )[0]
        print(f"Instance created with ID: {instance.id}")
        return instance.id
    except (NoCredentialsError, PartialCredentialsError):  # errores
        print("AWS credentials not found. Please configure your credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")


# terminar instancia EC2 con el ID
def terminate_ec2_instance(instance_id, region):
    try:
        # start de recurso EC2 en la región dada
        ec2 = boto3.resource('ec2', region_name=region)
        # instancia por ID
        instance = ec2.Instance(instance_id)
        instance.terminate()
        print(f"Instance {instance_id} terminated.")
    except (NoCredentialsError, PartialCredentialsError):  # errores
        print("AWS credentials not found. Please configure your credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")


# iniciar instancia EC2. Misma semántica
def start_ec2_instance(instance_id, region):
    try:
        ec2 = boto3.resource('ec2', region_name=region)
        instance = ec2.Instance(instance_id)
        instance.start()
        print(f"Instance {instance_id} started.")
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not found. Please configure your credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")


@click.group()  # comandos
def cli():
    pass


# comando create para crear EC2
@click.command()
@click.option('--instance-type', default='t2.micro', help='Introduzca el tipo de instancia. Por defecto t2 micro')
@click.option('--image-id', required=True, help=' Introduzca algun AMI ID para usar en la instancia, requerido')
@click.option('--key-name', required=True, help='Introduzca Key pair name, requerido')
@click.option('--security-group-id', required=True, help='Introduzca el Security group ID, requerido')
@click.option('--region', required=True, help='Introduzca la region de la instancia, requerida')
def create(instance_type, image_id, key_name, security_group_id, region):
    create_ec2_instance(instance_type, image_id, key_name, security_group_id, region)


# comando terminate para acabar una instancia
@click.command()
@click.argument('instance_id')
@click.option('--region', required=True, help='Introduzca la region de la instancia. Requerida')
def terminate(instance_id, region):
    terminate_ec2_instance(instance_id, region)


# comando start
@click.command()
@click.argument('instance_id')
@click.option('--region', required=True, help='Introduzca la region de la instancia. Requerida')
def start(instance_id, region):
    start_ec2_instance(instance_id, region)


# adicion de los comandos
cli.add_command(create)
cli.add_command(terminate)
cli.add_command(start)

if __name__ == '__main__':
    cli()
