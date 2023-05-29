from flask import Flask
from Base_de_datos import conexion
from flask_restful import Api
from flask_migrate import Migrate
from controllers.area_controller import AreaController
from controllers.empleado_controller import EmpleadoController
from controllers.area_solo_controller import AreaSoloController
from models.area_modelo import AreaModel
from models.empleado_modelo import EmpleadoModel

app = Flask(__name__)
api=Api(app=app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/fabrica"
conexion.init_app(app)

Migrate(app, conexion)

api.add_resource(AreaController, "/area ", "/areas")
api.add_resource(AreaSoloController, "/area/<int:id>")
api.add_resource(EmpleadoController, "/empleado")

if __name__=="__main__":
    app.run(debug = True)