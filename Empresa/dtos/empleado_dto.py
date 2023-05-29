from models.empleado_modelo import EmpleadoModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class EmpleadoResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model= EmpleadoModel
        include_fk = True

        

class EmpleadoRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        include_fk = True