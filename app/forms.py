from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


from flask_wtf.file import FileField,FileAllowed, FileRequired
from werkzeug.utils import secure_filename



 
class UploadForm(FlaskForm):
    description = StringField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
