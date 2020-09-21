from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Title',validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('quote', 'quote'), ('education', 'education'), ('business', 'business')],
                           validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[Required()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('bio', validators=[Required()])
    submit = SubmitField('Post')