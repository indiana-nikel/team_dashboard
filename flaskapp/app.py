from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/teams")
def teams():
    return render_template("teams.html")

@app.route("/rankings")
def rankings():
    return render_template("rankings.html")


if __name__ == "__main__":
    app.run(debug=True)
