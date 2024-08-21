from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RoleForm(FlaskForm):
    name = StringField('Nome da Função', validators=[DataRequired(), Length(max=64)])
    description = TextAreaField('Descrição', validators=[Length(max=255)])
    submit = SubmitField('Criar Função')
