from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Applied Biologist",
        "location": "Tabanga, Isla Sombra",
        "salary": "300000 gross per year"
    },
    {
        "id": 2,
        "title": "Encarceration Engineer",
        "location": "Tabanga, Isla Sombra",
        "salary": "400000 gross per year"
    },
    {
        "id": 3,
        "title": "Hands-on Biologist",
        "location": "Tabanga, Isla Sueño",
        "salary": "150000 gross per year"
    },
    {
        "id": 4,
        "title": "Traversal Application Developer",
        "location": "Sowahige"
    }
]

@app.route("/")
def hello_world():
    return render_template("index.html", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

@app.route("/css_tutorial")
def css_tutorial():
    return render_template("css_tutorial.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)