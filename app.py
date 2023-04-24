#importo las librerias de flask
from flask import Flask, request, jsonify, json, render_template
#importo las dependencias de trabajo
from config.db import app, bd

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

