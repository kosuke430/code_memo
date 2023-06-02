from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo


class RegistrationForm(FlaskForm):
    #メモを追加する時に呼び出すForm
    language=StringField('プログラミング言語',validators=[DataRequired()])
    error_name=StringField('件名',validators=[DataRequired()])
    error_content=TextAreaField('エラー内容',validators=[DataRequired()])
    submit=SubmitField('メモ登録')
    #エラーが生じたり、問題が出たら下に関数を追加して処理を行う

class Change_Form(FlaskForm):
    #メモに変更を加える時に使うForm
    language=StringField('プログラミング言語',validators=[DataRequired()])
    error_name=StringField('件名',validators=[DataRequired()])
    error_content=TextAreaField('エラー内容',validators=[DataRequired()])
    submit=SubmitField('メモ更新')

    def __init__(self,change_id,*args,**kwargs):
        super(Change_Form,self).__init__(*args,**kwargs)
        self.id=change_id

