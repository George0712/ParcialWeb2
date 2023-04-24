from config.db import bd, app, ma

class Profesor(bd.Model):
    __tablename__ ='tblprofesor'
    id = bd.Column(bd.Integer, primary_key = True)
    nameProf = bd.Column(bd.String(50))

def __init__(self, nameProf):
    self.nameProf = nameProf

class ProfesorSchema(ma.Schema):
    class Meta:
        fields =('id', 'nameProf')
