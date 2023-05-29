from flask_restful import Resource, request
from  Base_de_datos import conexion
from models.area_modelo import AreaModel
from dtos.area_dto import AreaRequestDto

class AreaController(Resource):
    def post(self):
        data= request.json
        try:
            dto= AreaRequestDto()
            dataValida = dto.load(data)
            nuevaArea = AreaModel(**dataValida)

            conexion.session.add(nuevaArea)
            conexion.session.commit()

            return{
                "message":"Area creada exitosamente"
            },201
        
        except Exception as error:
            conexion.session.rollback()
            return{
                "message": "Error al crear la Area",
                "content": error.args
            }
