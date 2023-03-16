import csv
import requests

# Configurar el token de acceso y la URL base de la API
token = 'your-access-token'
url_base = 'https://gitlab.server/api/v4/'

# Abrir el archivo CSV y leer los datos de cada usuario
with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Crear el objeto JSON del usuario
        user_data = {
            'name': row['name'],
            'username': row['username'],
            'email': row['email'],
            'password': row['password'],
            'reset_password': True
        }

        # Realizar la solicitud POST a la API para crear el usuario
        response = requests.post(url_base + 'users', headers={'PRIVATE-TOKEN': token}, json=user_data)

        # Manejar la respuesta de la API
        if response.status_code == 201:
            new_user = response.json()
            print(f'Usuario creado: {new_user["username"]}')
        else:
            print(f'Error al crear el usuario: {response.text}')