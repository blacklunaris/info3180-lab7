from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


from flask_wtf.file import FileField,FileAllowed, FileRequired
from werkzeug.utils import secure_filename



 
class UploadForm(FlaskForm):
    desc=FileField('Desciption',validators=[InputRequired()])
    upload = FileField('image', validators=[
    FileRequired(),
    FileAllowed(['jpg', 'png'], 'Images only!')
    ])
