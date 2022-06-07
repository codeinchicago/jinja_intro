# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <p>Here is a list of my favorite games: <ul><li>Spirit Island</li> <li>The Crew</li> <li>No Retreat! </li> <li>Brass:Birmingham</li> <li>Watergate</li> </ul></p>"


# from flask import Flask,render_template

# app = Flask(__name__)

# @app.route('/end')
# def index():
#     return render_template('index.html',header='Amazing Universe', sub_header='Our universe is quite amazing', list_header="Galaxies!",
#                        galaxies=get_galaxies(), site_title="Camposha.info")

# def get_galaxies():
#     galaxies = ["Messier 81", "StarBurst", "Black Eye", "Cosmos Redshift", "Sombrero", "Hoags Object", "Andromeda","Pinwheel","Cartwheel",
#     "Mayall's Object","Milky Way","IC 1101","Messier 87","Ring Nebular", "Centarus A", "Whirlpool", "Canis Major Overdensity","Virgo Stellar Stream"]
#     return galaxies


@app.route("/code")
def index():
    games = ['Spirit Island', 'The Crew', 'No Retreat!', 'Brass:Birmingham', 'Watergate']
    return render_template('index.html', games=games)

lis = [1, 2, 3, 4]

# @app.route('/')
# def showquestion():
#     questions = ['favourite color?','favourite color?','favourite color?','do you like pasta?','do you like pasta?']
#     answers = ["red","green",'blue','yes','no']
#     return render_template('question.html', questions=questions, answers=answers)

# def index():
#     user_dict = {
#         'username': 'brians',
#         'email': 'brians@codingtemple.com'
#     }
#     colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#     return render_template('index.html', user=user_dict, colors=colors)


@app.route('/test')
def test():
    return 'This is a test'