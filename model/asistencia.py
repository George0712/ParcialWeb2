from config.db import bd, app, ma

class asistencia(bd.Model):
    __tablename__='tblasistencia'
    id = bd.Column(bd.Integer,primary_key=True)
    id_userFK = bd.Column(bd.Integer, bd.ForeignKey('tblusers.id'))
    horaLlegada = bd.Column(bd.String(10))
    estado = bd.column(bd.String(20))
    horaSalida = bd.Column(bd.String(10))
    
def __init__(self,id_userFK, horaLlegada, estado, horaSalida):
    self.id_userFK = id_userFK
    self.horaLlegada = horaLlegada
    self.estado = estado
    self.horaSalida = horaSalida

with app.app_context():
    bd.create_all()
class asistenciaSchema(ma.Schema):
    class Meta:
        fields=('id', 'id_userFK', 'horaLlegada', 'estado', 'horaSalida')