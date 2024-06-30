import base64
import sys
import logging
import requests
import os
from typing import List, Dict
from argparse import ArgumentParser, Namespace

#urllib3
logging.getLogger("urllib3").setLevel(logging.WARNING) #nivel defecto de WARNING

#configuración del logger
logger = logging.getLogger()
logger.setLevel(logging.WARNING)
ch = logging.StreamHandler() #mensajes de log a la consola
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #formato de los mensajes de log
ch.setFormatter(formatter)
logger.addHandler(ch) #manejador configurado al logger

def parse_args(args: List) -> Namespace:
    parser = ArgumentParser(description="Our first program") #manejo de los argumentos de las líneas de comando
    parser.add_argument('-u', '--username', type=str, required=True)
    parser.add_argument('-p', '--password', type=str, required=True)
    parser.add_argument('-v', '--verbosity', action='store_true', help="verbosity On") #si se incluye, su valor será True. Esto muestra nivel de logging DEBUG
    parser.add_argument('-c', '--count', type=int, default=5, help="number of users")
    return parser.parse_args(args) #analiza los argumentos y los convierte en un objeto, Namespace.

#función de autenticación en base64
def get_auth_header(username: str, password: str) -> str:
    encoded_auth_string = f"{username}:{password}".encode('ascii') #cadena a bytes usando ASCII
    b64_auth_string = base64.b64encode(encoded_auth_string) #cadena combinada -> cadena base64
    return f"Basic {b64_auth_string.decode('ascii')}" #cadena base64 -> basic base64string

#datos de usuarios aleatorios
def get_random_users(count: int) -> List[Dict]:
    logger.info(f"Fetching data for {count} users")
    response = requests.get(f"https://random-data-api.com/api/users/random_user?size={count}") #solicitud GET a la API
    if response.ok:
        return response.json()
    raise RuntimeError("Unable to get response from server") #error indicando que no se pudo obtener una respuesta del servidor


def save_users_to_files(users: List[Dict]): #donde se guardarán los archivos
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for user in users:
        state = user['address']['state'] #estado del usuario
        country = user['address']['country'] #país del usuario
        user_data = f"{user['first_name']} {user['last_name']}" #cadena para nombre y apellido

        country_dir = os.path.join(output_dir, country)
        if not os.path.exists(country_dir): #verifica si el directorio del país existe
            os.makedirs(country_dir) #si no existe, lo crea

        state_file = os.path.join(country_dir, f"{state}.txt")
        with open(state_file, 'a') as f: #archivo en modo append
            f.write(user_data + '\n') #datos del usuario en el archivo

    logger.info(f"Data saved in {output_dir} directory")


#flujo principal del programa
def main(args: List):
    parsed_args = parse_args(args)

    if parsed_args.verbosity:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbosity turned on") #si la verbosity está activada, nivel de logging a DEBUG

    users = get_random_users(parsed_args.count)
    logger.debug(f"Fetched users: {users}") #mensaje de debug con los datos obtenidos

    save_users_to_files(users)


if __name__ == '__main__':
    main(sys.argv[1:])
