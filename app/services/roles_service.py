from app import db
from app.models.role import Role

def save_role(role: Role):
    try:
        db.session.add(role)
        db.session.commit()
    except Exception as exception:
        print("Não foi possível gravar no banco", exception)
