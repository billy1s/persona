from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class searchForm(FlaskForm):

    username = StringField('Username: ')
    submit = SubmitField('Search')
