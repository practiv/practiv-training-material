from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    app.logger.info('Hello world hit')
    return 'Hello, World!'


if __name__ == '__main__':
    port = 8080
    app.logger.info('Application started. Listening on port %s', port)
    app.run(host='0.0.0.0', port=port)
