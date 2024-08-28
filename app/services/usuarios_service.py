from app import db
from app.models.usuario import User

def list_all_users():
    lista_usuarios = User.query.all()
    return lista_usuarios

def save_user(user: User):
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as exception:
        print("Não foi possível gravar no banco", exception)
