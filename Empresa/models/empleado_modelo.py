from sqlalchemy.schema import Column , ForeignKey
from sqlalchemy import types
from Base_de_datos import conexion

class EmpleadoModel(conexion.Model):
    id= Column(autoincrement=True, type_= types.Integer, primary_key=True)
    nombre=Column(type_=types.Text, nullable=False)
    apellido=Column(type_=types.Text, nullable=False)
    correo=Column(type_=types.Text, nullable=False, unique=True)
    area_ID=Column(ForeignKey(column="area.id"), type_=types.Integer,name = "area_id")

    __tablename__="empleados"