from flask import Flask
from Base_de_datos import conexion
from flask_restful import Api
from flask_migrate import Migrate
from controllers.area_controller import AreaController
from controllers.empleado_controller import EmpleadoController


app = Flask(__name__)
api=Api(app=app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/Area"
conexion.init_app(app)

Migrate(app, conexion)

api.add_resource(AreaController, "/area")
api.add_resource(EmpleadoController, "/empleado")

if __name__=="__main__":
    app.run(debug = True)