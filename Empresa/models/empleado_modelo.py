from sqlalchemy import Column , ForeignKey, types
from Base_de_datos import conexion

class EmpleadoModel(conexion.Model):
    id= Column(autoincrement=True, type_= types.Integer, primary_key=True)
    nombre=Column(type_=types.Text, nullable=False)
    apellido=Column(type_=types.Text, nullable=False)
    correo=Column(type_=types.Text, nullable=True)
    area_ID=Column(ForeignKey(column="area.id"))

    __tablename__="empleados"