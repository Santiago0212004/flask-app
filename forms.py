from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, EqualTo
from models import Team

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    team = SelectField('Equipo de trabajo', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Registrarse')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.team.choices = [(team.id, team.name) for team in Team.query.all()]

class TaskForm(FlaskForm):
    content = TextAreaField('Contenido de la tarea', validators=[DataRequired()])
    due_date = DateField('Fecha de entrega', validators=[DataRequired()])
    submit = SubmitField('Añadir tarea')