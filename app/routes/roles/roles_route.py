from flask import render_template, flash, redirect, url_for, Blueprint
from app.forms.role_form import RoleForm
from app.models.role import Role
from app.services.roles_service import\
    delete_role_service, edit_role_service, list_all_roles, save_role

bp_roles = Blueprint('roles', __name__)

@bp_roles.route('/roles', methods=['GET'])
def list_roles():
    roles = list_all_roles()
    return render_template('roles/list_all_roles.html', title='Listar Funções', roles=roles)

@bp_roles.route('/create_role', methods=['GET', 'POST'])
def create_role():
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data, description=form.description.data)
        save_role(role)
        flash('Função criada com sucesso!', 'alert-success')
        return redirect(url_for('roles.create_role'))
    return render_template('roles/create_role.html', title='Criar Função', form=form)

@bp_roles.route('/roles/delete/<int:role_id>', methods=['POST'])
def delete_role(role_id):
    role = Role.query.get_or_404(role_id)
    delete_role_service(role)
    flash('Função excluída com sucesso!', 'success')
    return redirect(url_for('roles.list_roles'))

@bp_roles.route('/roles/edit/<int:role_id>', methods=['GET', 'POST'])
def edit_role(role_id):
    role = Role.query.get_or_404(role_id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        edit_role_service()
        flash('Função editada com sucesso!', 'success')
        return redirect(url_for('roles.list_roles'))
    return render_template('roles/edit_role.html', form=form)
