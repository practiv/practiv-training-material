import json
import logging

from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    with open('/config/config.json') as config_file:
        data = json.load(config_file)
    app.logger.info('Hello, World! endpoint was reached')
    return data['greeting_message']


if __name__ == '__main__':
    try:
        with open('/secrets/license.json') as licenseFile:
            data = json.load(licenseFile)
    except FileNotFoundError:
        app.logger.info('License file not present')
        exit(2)

    key_ = data['license_key']
    if key_ != 'super secret license key':
        app.logger.info('License key is incorrect')
        exit(2)

    app.logger.info('License: ' + key_)

    # Start server
    port = 8080
    app.logger.info('Application started. Listening on port %s', port)
    app.run(host='0.0.0.0', port=port)
