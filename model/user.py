from config.db import bd, app, ma

class Users(bd.Model):
    __tablename__ = 'tblusers'
    id = bd.Column(bd.Integer, primary_key = True) 
    name = bd.Column(bd.String(50))
    position = bd.Column(bd.String(30))
    password = bd.Column(bd.String(20))

    def __init__(self, id, name, position, password):
        self.id = id
        self.name = name
        self.position = position
        self.password = password
    
with app.app_context():
    bd.create_all()   
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'position', 'password')