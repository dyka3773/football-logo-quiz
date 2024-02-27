import configs
from routes import bp

from flask import Flask


app = Flask(__name__, template_folder='templates', static_folder='static')
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",  # This will make the app available to other computers on the network
        port=8000,
        debug=True
    )
