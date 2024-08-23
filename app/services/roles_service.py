from app import db
from app.models.role import Role

def list_all_roles():
    lista_roles = Role.query.all()
    return lista_roles

def save_role(role: Role):
    try:
        db.session.add(role)
        db.session.commit()
    except Exception as exception:
        print("Não foi possível gravar no banco", exception)

def delete_role_service(role: Role):
    try:
        db.session.delete(role)
        db.session.commit()
    except Exception as exception:
        print("Não foi possível deletar a role", exception)

def edit_role_service():
    try:
        db.session.commit()
    except Exception as exception:
        print("Não foi possível editar a role", exception)
