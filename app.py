#importo las librerias de flask
from flask import Flask, request, jsonify, json, render_template
#importo las dependencias de trabajo
from config.db import app, bd

#importamos los modelos

from model.user import Users, UsersSchema
from model.asistencia import asistencia, asistenciaSchema
from model.profesor import Profesor, ProfesorSchema


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

profesor_schema = ProfesorSchema()
profesores_schema = ProfesorSchema(many=True)

asistencia_schema = asistenciaSchema()
asistencias_schema = asistenciaSchema(many=True)

