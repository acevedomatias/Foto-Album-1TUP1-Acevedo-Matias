from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL

class PhotoForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    image = StringField('Imagen (URL)', validators=[DataRequired(), URL()])
    submit = SubmitField('Añadir')
