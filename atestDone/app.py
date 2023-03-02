from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit_form", methods=["POST"])
def submit_form():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Do something with the data (e.g. store it in a database)

    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
