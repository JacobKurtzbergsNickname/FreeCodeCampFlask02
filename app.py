from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/css_tutorial")
def css_tutorial():
    return render_template("css_tutorial.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)