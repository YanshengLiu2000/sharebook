from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q= StringField(validators=[DataRequired(),Length(min=1,max=30)])#这里可以传入msg, 这样当验证不通过时, form会返回你传入的msg
    page=IntegerField(validators=[NumberRange(min=1,max=99)],default=1)