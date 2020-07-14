from foxdemo.common.flask import initialize_app
from foxdemo.common.config import WEB_HOST, WEB_PORT

app = initialize_app()

if __name__ == '__main__':
    app.run(host=WEB_HOST, port=WEB_PORT)