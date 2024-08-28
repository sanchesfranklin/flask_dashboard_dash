#from flask import render_template, flash, redirect, url_for, Blueprint
from flask import render_template, Blueprint, flash, redirect, url_for
from app.models.usuario import User
from app import bcrypt
from app.services.usuarios_service import list_all_users, save_user
from app.forms.usuario_form import FormCriarUsuario

bp_usuarios = Blueprint('usuarios', __name__)

@bp_usuarios.route('/users', methods=['GET'])
def list_users():
    users = list_all_users()
    return render_template('usuarios/list_all_users.html', title='Usuários', users=users)

@bp_usuarios.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = FormCriarUsuario()
    if form.validate_on_submit():
        # Declarando variáveis
        username = form.username.data
        email = form.email.data
        senha_crypt = bcrypt.generate_password_hash(form.senha.data)
        role_id = form.role.data
        user = User(username=username, email=email, password_hash=senha_crypt, role_id=role_id)
        save_user(user)
        flash('Usuário criado com sucesso!', 'alert-success')
        return redirect(url_for('usuarios.create_user'))
    return render_template('usuarios/create_user.html', title='Criar Usuário', form=form)
