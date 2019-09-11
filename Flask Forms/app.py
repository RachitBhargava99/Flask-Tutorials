from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    form = DummyForm()
    if form.is_submitted():
        input_data = form.input_field.data
        return render_template('home.html', form=form, data=input_data)
    else:
        return render_template('home.html', form=form, data='Form Not Submitted')


class DummyForm(FlaskForm):
    input_field = StringField('Input')
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 80, debug = True)
