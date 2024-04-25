from flask import Blueprint,request,jsonify
from services.userAuth import verificarUsuario
jwtRoutesBluePrint = Blueprint('jwtRoutes',__name__)


@jwtRoutesBluePrint.route('/login', methods=['POST'])
def login():
    user = request.get_json()
    username = str(user['username'])
    userpassword = str(user['password'])

    result = verificarUsuario(username,userpassword)
    return jsonify(result)



