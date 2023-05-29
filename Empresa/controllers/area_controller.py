from flask_restful import Resource, request
from  Base_de_datos import conexion
from models.area_modelo import AreaModel
from dtos.area_dto import AreaRequestDto, AreaResponseDto

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
            },400
    def get (self):
        resultado = conexion.session.query(AreaModel).all()
        dto=AreaResponseDto(many=True)
        data = dto.dump(resultado)
        return{
            "content": data
        }

