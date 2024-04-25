from flask import Blueprint,jsonify,request
from utils.encrypt import encrypt
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required,JWTManager
from utils.DBPushQuery import pushQuery


crud = Blueprint('crudUsers',__name__)


@crud.post('/api/users')
def create_users():
    usuario = request.get_json()
    print(type(usuario))
    username = usuario['username']
    userpass = usuario['password']
    print(f'Contrasena puesta en el POST:{userpass}')
    userpass = encrypt(userpass)
    print(f'Contrasena encriptada:{userpass}')
    queryTuple = (username, userpass)
    print(queryTuple)
    result = pushQuery('INSERT INTO users (username,password) VALUES (%s,%s) RETURNING *;', queryTuple)
    return jsonify(result)


@crud.delete('/api/users/<id>')
def delete_users(id):

    queryTuple = (id,)
    result = pushQuery('DELETE FROM users WHERE id = %s RETURNING *',queryTuple)

    return jsonify(result)


@crud.put('/api/users/<id>')
def update_users(id): 

    usuario = request.get_json()
    username = usuario['username']
    queryTuple = (username,id)
    result = pushQuery('UPDATE users SET username = %s WHERE id = %s RETURNING username',queryTuple)
    return jsonify(result)


@crud.get('/api/users/<id>')
def getOne_user(id):
    queryTuple = (id,)
    result = pushQuery('SELECT id,username FROM users WHERE id = %s',queryTuple)

    if result is None:
        return jsonify({'Mensaje':'Usuario no encontrado'}),404

    return jsonify(result)