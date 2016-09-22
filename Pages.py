from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "hello, try adding /goodbye/ or /help/ to the url"

@app.route("/goodbye/")
def goodbye():
    return "goodbye"

@app.route("/help/")
def help():
    return "help"

if __name__=='__main__':
    app.run()
