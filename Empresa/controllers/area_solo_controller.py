from flask_restful  import Resource
from Base_de_datos import conexion
from dtos.area_dto import AreaResponseDto
from models.area_modelo import AreaModel

class AreaSoloController(Resource):
    def GET (self, id):
        area = conexion.session.query(AreaModel).filter_by(id=id).first()
        if area is None:
            return{
                "message" : "el area no existe"
            }
        dto= AreaResponseDto()
        resultado = dto.dump(area)
        return{
            "content": resultado
        }