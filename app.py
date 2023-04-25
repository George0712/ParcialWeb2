#importo las librerias de flask
from flask import Flask, request, jsonify, json, render_template
#importo las dependencias de trabajo
from config.db import app, bd
#importamos el datetime
import datetime
#importamos los modelos

from model.user import Users, UsersSchema
from model.asistencia import asistencia, asistenciaSchema
from model.estudiante import estudiante, estudianteSchema


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

estudiante_schema = estudianteSchema()
estudiantes_schema = estudianteSchema(many=True)

asistencia_schema = asistenciaSchema()
asistencias_schema = asistenciaSchema(many=True)


@app.route("/", methods=['GET'])
def index():
    nombre= "Iniciar Sesión"
    return render_template('login.html', name = nombre)

@app.route("/estudiante", methods=['POST'])
def saveEst():
    id = request.json['id']
    name = request.json['name']
    password = request.json['password']
    newuser = estudiante(id, name, password)
    bd.session.add(newuser)
    bd.session.commit()
    return "guardado"

@app.route("/eliminar", methods=['POST'])
def eliminarEst():
    id = request.json['id']
    usuario = estudiante.query.get(id)
    bd.session.delete(usuario)
    bd.session.commit()
    return jsonify(estudiante_schema.dump(usuario))

@app.route("/actualizar", methods=['POST'])
def actualizarEst():
    id = request.json['id']
    name = request.json['name']
    password = request.json['password']
    est = estudiante.query.get(id)
    est.id = id
    est.name = name
    est.password = password
    bd.session.commit()
    return "actualizado"

@app.route("/user", methods=['POST'])
def saveUser():
    codigo = request.json['id']
    name = request.json['name']
    position = request.json['position']
    password = request.json['password']
    newuser = Users(codigo, name, position, password)
    bd.session.add(newuser)
    bd.session.commit()
    return "guardado"

@app.route("/eliminarUser", methods=['POST'])
def eliminarUser():
    id = request.json['id']
    usuario = Users.query.get(id)
    bd.session.delete(usuario)
    bd.session.commit()
    return jsonify(user_schema.dump(usuario))

@app.route("/actualizarUser", methods=['POST'])
def actualizarUser():
    id = request.json['id']
    name = request.json['name']
    password = request.json['password']
    user = Users.query.get(id)
    user.id = id
    user.nombre =name
    user.contraseña = password
    bd.session.commit()
    return "actualizado"

@app.route("/entrada", methods=['POST'])
def horaEntrada():
   entrada = datetime.datetime.now()
   salida = datetime.datetime.now()
   estado = request.json['estado']
   id_estFK = request.json['fk_idEst']
   newuser = asistencia(id_estFK, entrada, estado, salida)
   bd.session.add(newuser)
   bd.session.commit()
   return "guardado"

@app.route("/salida", methods=['POST'])
def horaSalida():
   salida = datetime.datetime.now()
   id_est = request.json['fk_idEst']
   estado = request.json['estado']
   bd.session.query(asistencia).filter(asistencia.fk_idEst == id_est).update
   (
        {
            asistencia.salida : salida,
            asistencia.estado : estado
        }
   )  
   bd.session.commit()
   return "guardado"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8085)