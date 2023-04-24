from config.db import bd, app, ma

class estudiante(bd.Model):
    __tablename__ ='tblestudiante'
    id = bd.Column(bd.Integer, primary_key = True)
    name = bd.Column(bd.String(50))
    password = bd.Column(bd.String(20))


def __init__(self, name, password):
    self.name = name
    self.password = password

with app.app_context():
    bd.create_all()

class estudianteSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'password')
