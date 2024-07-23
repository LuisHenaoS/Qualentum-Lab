## AWS EC2 Management CLI

Esta CLI permite gestionar instancias EC2 en AWS, incluyendo la creación, terminación, reanudación y eliminación de instancias en diferentes regiones.
Incluye tests con boto3.

# Requisitos

- **SDK Python 3.11.9**: Se recomienda usar esta versión para asegurar la compatibilidad con todas las dependencias. Aunque con la versión 3.4 en adelante debería bastar.

# Uso cli. Crear una instancia EC2:
- python aws_cli.py create --instance-type --image-id --key-name --security-group-id --region

-Ejemplo: python aws_cli.py create --instance-type t2.micro --image-id ami-12345678 --key-name my-key-pair --security-group-id sg-0123456789abcdef0 --region eu-west-3

# Uso cli. Terminar una instancia EC2:
-python aws_cli.py terminate --region

-Ejemplo: python aws_cli.py terminate i-0abcdef1234567890 --region eu-west-3

# Uso cli. Reanudar una instancia EC2:
-python aws_cli.py terminate --region

-Ejemplo: python aws_cli.py terminate i-0abcdef1234567890 --region eu-west-3

# Cli de los tests.
- pytest test_aws_cli.py
