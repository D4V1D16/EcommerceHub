from flask import Flask
from routes.CRUDUsers import crud
from routes.jwtRoutes import jwtRoutesBluePrint

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  
# Configuración de la aplicación Flask y registro de blueprints
app.register_blueprint(crud)
app.register_blueprint(jwtRoutesBluePrint)

if __name__ == '__main__':
    app.run(debug=True)