from flask_restful import Resource, request
from  Base_de_datos import conexion
from models.empleado_modelo import EmpleadoModel
from dtos.empleado_dto import EmpleadoResponseDto,EmpleadoRequestDto

class EmpleadoController(Resource):
    def get(self):
        resultado = conexion.session.query(EmpleadoModel).all()
        dto=EmpleadoResponseDto(many = True)
        data= dto.dump(resultado)

        return {
            "content" : data
        }
def post(self): 
    data= request.json
    dto = EmpleadoRequestDto()
    dataValidada = dto.load(data)
    print(dataValidada)
    nuevoEmpleado = EmpleadoModel(**dataValidada)
    conexion.session.add(nuevoEmpleado)
    try:
        conexion.session.commit()
        return {
            "message":" Empleado creado con exito"
        },201
    except Exception as error:
        conexion.session.rollback()
        return{
            "message" : "Error al crear al Empleado",
            "content" : error.args
        },400
