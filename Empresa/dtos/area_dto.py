from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.area_modelo import AreaModel

class AreaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel
        include_fk=True