from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", x=8, y=8, color1="whitesmoke", color2="darkgrey" )

@app.route('/<int:x>')
def board_x(x):
    return render_template("index.html", x=x, y=8, color1="whitesmoke", color2="darkgrey" )

@app.route('/<int:x>/<int:y>')
def board_xy(x,y):
    return render_template("index.html", x=x, y=y, color1="whitesmoke", color2="darkgrey" )

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def board_xy_color12(x,y,color1,color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2 )


if __name__=="__main__":
    app.run(debug=True)