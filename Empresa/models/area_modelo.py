from sqlalchemy import Column , types
from Base_de_datos import conexion

class AreaModel(conexion.Model):
    id = Column(autoincrement=True, type_=types.Integer, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False, unique = True)
    piso= Column(type_=types.Text, nullable=False)



    __tablename__="area"