import csv
import requests

# Configurar el token de acceso y la URL base de la API
token = 'your_access_token'
url_base = 'https://your.gitlab.server/api/v4/'

# ID del proyecto donde se agregarán los usuarios
project_id = 'your_project_id'

# Abrir el archivo CSV y leer los datos de cada usuario
with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Crear el objeto JSON del usuario
        user_data = {
            'email': row['email'],
            'password': row['password'],
            'username': row['username'],
            'name': row['name'],
        }

        # Realizar la solicitud POST a la API para crear el usuario
        response = requests.post(url_base + 'users', headers={'PRIVATE-TOKEN': token}, json=user_data)

        # Manejar la respuesta de la API
        if response.status_code == 201:
            new_user = response.json()
            print(f'Usuario creado: {new_user["username"]}')
            
            # Agregar el usuario al proyecto con nivel de acceso "developer"
            access_level = 30
            user_id = new_user['id']
            response = requests.post(url_base + f'projects/{project_id}/members', headers={'PRIVATE-TOKEN': token}, json={
                'user_id': user_id,
                'access_level': access_level
            })
            
            # Manejar la respuesta de la API
            if response.status_code == 201:
                print(f'Usuario agregado al proyecto: {new_user["username"]}')
            else:
                print(f'Error al agregar el usuario al proyecto: {response.text}')
        else:
            print(f'Error al crear el usuario: {response.text}')
