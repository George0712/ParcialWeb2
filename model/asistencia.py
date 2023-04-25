from config.db import bd, app, ma

class asistencia(bd.Model):
    __tablename__= 'tblasistencia'
    id = bd.Column(bd.Integer, primary_key=True)
    fk_idEst = bd.Column(bd.Integer, bd.ForeignKey('tblestudiante.id'))
    horaLlegada = bd.Column(bd.DateTime())
    estado = bd.Column(bd.String(20))
    horaSalida = bd.Column(bd.DateTime())
    
    def __init__(self,fk_idEst, horaLlegada, estado, horaSalida):
        self.fk_idEst = fk_idEst
        self.horaLlegada = horaLlegada
        self.estado = estado
        self.horaSalida = horaSalida

with app.app_context():
    bd.create_all()
class asistenciaSchema(ma.Schema):
    class Meta:
        fields=('fk_idEst', 'horaLlegada', 'estado', 'horaSalida')