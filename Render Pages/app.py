from flask import Flask, request, render_template

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=['GET'])
def home():
    pokemon_name = "Pikachu"
    return f'''<head>
    <title>Hello World!</title>
</head>

<body>
    <p style="font-family: 'Comic Sans MS', 'Times New Roman'">Hello {pokemon_name}!</p>
</body>'''


@app.route('/home-2', methods=['GET'])
def home2():
    pokemon_name = "Pikachu"
    return render_template('home-2.html', pokemon_name=pokemon_name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
