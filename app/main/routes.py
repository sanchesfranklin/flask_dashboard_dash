from flask import render_template, Blueprint, flash, redirect, url_for
from app.forms.role_form import RoleForm
from app.models.role import Role
from app.services.roles_service import save_role

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/create_role', methods=['GET', 'POST'])
def create_role():
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data, description=form.description.data)
        save_role(role)
        flash('Função criada com sucesso!', 'alert-success')
        return redirect(url_for('create_role'))
    return render_template('create_role.html', title='Criar Função', form=form)
