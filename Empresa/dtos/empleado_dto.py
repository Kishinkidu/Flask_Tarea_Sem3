from models.empleado_modelo import EmpleadoModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class EmpleadoResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model= EmpleadoModel

        

class EmpleadoRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel