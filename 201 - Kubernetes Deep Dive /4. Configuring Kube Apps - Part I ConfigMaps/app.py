import json

from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    with open('/config/config.json') as config_file:
        data = json.load(config_file)
    app.logger.info('Hello, World! endpoint was reached')
    return data['greeting_message']


if __name__ == '__main__':
    port = 8080
    app.logger.info('Application started. Listening on port %s', port)
    app.run(host='0.0.0.0', port=port)
