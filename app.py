from flask import Flask # type: ignore


from routes.usuario_route import usuario_bp 

app = Flask(__name__)

app.register_blueprint(usuario_bp)

app.run(debug=True)