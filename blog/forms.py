from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField, SelectField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileAllowed

from blog.models import Category, Goverment, Parameter

def categories():
    return Category.query

def goverments():
    return Goverment.query

def parameters():
    return Parameter.query


class PostForm(FlaskForm):
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], 'We only accept JPG or PNG images')
    ])
    title = StringField('Title', [
            validators.InputRequired(),
            validators.Length(max=80)
        ])
    body = TextAreaField('Content', validators=[validators.InputRequired()])

    category = QuerySelectField('Category', query_factory=categories,
        allow_blank=True)
    new_category = StringField('New Category')

    goverment = QuerySelectField('Goverment', query_factory=goverments,
        allow_blank=True)
    new_goverment = StringField('New Goverment')
    
    api_url = StringField('API_URL', [
        validators.InputRequired(),
        validators.Length(max=255)
    ])

    api_request =TextAreaField('Request', validators=[validators.InputRequired()])
    api_response =TextAreaField('Response', validators=[validators.InputRequired()])

    new_parameter = StringField('Parameter', [
            validators.InputRequired(),
            validators.Length(max=50),
        ])
    
    new_type = StringField('Type', [
            validators.InputRequired(),
            validators.Length(max=80)
        ])

    new_desctiption = StringField('Desctiption', [
            validators.InputRequired(),
            validators.Length(max=500)
        ])

