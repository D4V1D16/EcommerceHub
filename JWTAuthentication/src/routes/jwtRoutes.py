from flask import Blueprint,request,jsonify
from services.userAuth import verificarUsuario
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity,get_jwt
from utils.DBPushQuery import pushQuery
from datetime import datetime,timezone
jwtRoutesBluePrint = Blueprint('jwtRoutes',__name__)
@jwtRoutesBluePrint.route('/login', methods=['POST'])
def login():
    user = request.get_json()
    username = str(user['username'])
    userpassword = str(user['password'])

    result = verificarUsuario(username,userpassword)

    if result == True:
        
        return jsonify({'token':create_access_token(identity=username)})
    else:
        return jsonify({'message':'Credenciales Incorrectas'}),401



@jwtRoutesBluePrint.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


def check_if_token_revoked(jwtPayload:dict) -> bool:
    jti = jwtPayload["jti"]
    queryTuple = (jti,)
    result = pushQuery('SELECT * FROM tokenblocklist WHERE jti = %s',queryTuple)

    return result is not None




@jwtRoutesBluePrint.route("/logout",methods=["DELETE"])
@jwt_required()
def Logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    queryTuple=(jti,now)
    result = pushQuery('INSERT INTO tokenblocklist (jti,created_at) VALUES (%s,%s)RETURNING id',queryTuple)

    return jsonify({'message':'Se ha cerrado la sesión'}),200