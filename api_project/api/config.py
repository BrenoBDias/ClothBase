import json

def get_secrets():
    with open("D:\\Repos\\ClothBase\\api_project\\api\\secrets.json")as file:
        secret = json.load(file)
    return secret

class Settings:

    secrets = get_secrets()
    production = False
    secret_key = secrets.get('secret_key')
    psql_user = secrets.get('psql_user')
    psql_pass = secrets.get('psql_pass')
    psql_hostip = secrets.get('psql_hostip')
    psql_dockerip = secrets.get('psql_dockerip')
    psql_url = f'postgresql://{psql_user}:{psql_pass}@{psql_dockerip if production else psql_hostip}:5432/clothbase'








