import json
import logging

from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    with open('config.json') as config_file:
        data = json.load(config_file)
    with open('api_key.json') as api_key_file:
        api_key = json.load(api_key_file)

    app.logger.info('Received a request.')

    return f"{data['GREETING']} and the secret API key is {api_key['KEY']}"


if __name__ == '__main__':
    app.logger.info('Starting the application.')
    app.run(host='0.0.0.0', port=8080)
