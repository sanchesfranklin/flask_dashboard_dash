#pylint: disable=import-outside-toplevel
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    register_blueprints(app)

    return app

def register_blueprints(app):
    #TODO depois mudar essa implementação
    from app.routes.routes import bp as main_bp
    from app.routes.roles.roles_route import bp_roles
    from app.routes.usuarios.usuarios_route import bp_usuarios

    app.register_blueprint(main_bp)
    app.register_blueprint(bp_roles)
    app.register_blueprint(bp_usuarios)
