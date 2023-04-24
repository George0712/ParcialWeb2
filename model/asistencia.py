from config.db import bd, app, ma

class asistencia(bd.Model):
    __tablename__='tblasistencia'
    id = bd.Column(bd.Integer,primary_key=True)
    horaLlegada = bd.Column(bd.String(50))
    horaSalida = bd.Column(bd.String(50))
    
def __init__(self,horaLlegada, horaSalida):
    self.horaLlegada = horaLlegada
    self.horaSalida = horaSalida

class asistenciaSchema(ma.Schema):
    class Meta:
        fields=('id','horaLlegada', 'horaSalida')