import json
import logging

from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    with open('config.json') as config_file:
        data = json.load(config_file)
    app.logger.info('Received a request.')

    return data['GREETING']


if __name__ == '__main__':
    port = 8080
    app.logger.info('Application started. Listening on port %s', port)
    app.run(host='0.0.0.0', port=port)
