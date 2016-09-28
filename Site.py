from flask import Flask, render_template
from utils import softdevhw1
app=Flask(__name__)

@app.route("/")
def hello():
    return "hello, try adding /goodbye/ or /help/ to the url"

@app.route("/occupations/")
def help():
    d = softdevhw1.split(softdevhw1.importation("data/occupations.csv"))
    return render_template("02_flask-w-tmplt.html",collection=d,randomjob=softdevhw1.randomOcc(d))

if __name__=='__main__':
    app.debug=True
    app.run()
