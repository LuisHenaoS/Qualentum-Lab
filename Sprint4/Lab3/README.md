## Requistos

- python >= 3.11
- pip >= 21.2.1

## virtual env

```bash
python3 -m venv .venv
source  .venv/bin/activate
```

requirements

```bash
pip install -r requirements.txt
```

## App execute

```bash
 python server.py 
```

argumentos

- `--insert`: Insertar datos a la DB
- `--getdata`: Recupera todos los datos de la DB.
- `--delete`: Borra datos la DB.
- `--update`: Actualiza datos de la DB
- `--old_data`: Dato acutal en la DB.
- `--new_data`: Nuevo dato para la DB.

### Usos 

Server on para obtener todos los datos de la db

```bash
python client.py --getdata
```

En caso de no haber ningun archivo el servidor nos devolverá

```text
Resource not found
```

insertar un nuevo dato a la DB

```bash
python client.py --insert <data a insertar>
```

En caso de que no exista, lo que hará el servidor es crearlo e insertará el dato indicado en el parametro.

Borrar un dato

```bash
python client.py --delete <data a borrar>
```

Actualizar un dato existente

```bash
python client.py --update  --old_data <data antiguo> --new_data <nuevo data>
```

## tests

```bash
python -m pytest tests/
```
