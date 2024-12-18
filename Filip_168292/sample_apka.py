from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! this is the main page! <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/wsb")
def wsb():
    return redirect("https://www.merito.pl/warszawa/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
