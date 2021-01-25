import logging

from environs import Env
from sanic import response, Sanic
from tortoise.contrib.sanic import register_tortoise

# Environment configuration
env = Env()
env.read_env()

# Read environment variables
DEBUG = env.bool('DEBUG')
DB_HOST = env.str('DB_HOST')
DB_PORT = env.str('DB_PORT')
DB_NAME = env.str('DB_NAME')
DB_USER = env.str('DB_USER')
DB_PASSWORD = env.str('DB_PASSWORD')

logging.basicConfig(level=logging.ERROR)

app = Sanic('imdb_clone')

register_tortoise(app, db_url=f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', modules={'models': ['models']}, generate_schemas=True)


if __name__ == "__main__":
    app.run(port=8000, debug=DEBUG)