import os
from flask import Flask

app = Flask(__name__, template_folder='templates')
app.config.from_mapping(
    SECRET_KEY = 'dev',
    DATABASE = os.path.join(app.instance_path, 'hello.sqlite'),
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import db
db.init_app(app)


if __name__ == "__main__":
    app.run()

    
