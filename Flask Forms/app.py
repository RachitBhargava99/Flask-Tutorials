from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


default_str = "Form Not Submitted"


@app.route('/', methods=['GET', 'POST'])
def home():
    curr_form = PokeForm()
    if curr_form.is_submitted():
        p_name = curr_form.pokemon_name.data
        p_rank = curr_form.rank.data
        p_type = curr_form.pokemon_type.data
        return render_template('home.html', form=curr_form, poke_name=p_name, poke_rank=p_rank, poke_type=p_type)
    else:
        return render_template('home.html', form=curr_form, poke_name=default_str, poke_rank=default_str, poke_type=default_str)


class PokeForm(FlaskForm):
    pokemon_name = StringField('Pokemon Name')
    rank = IntegerField('Pokemon Rank')
    pokemon_type = SelectField('Pokemon Type', choices = [(1, 'Dark'), (2, 'Psychic'), (3, 'Electric'), (4, 'Fighting')])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 80, debug = True)
