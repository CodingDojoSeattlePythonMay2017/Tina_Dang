from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    print "Got Post Info"

    return render_template("result.html",name=request.form['name'],locations = request.form['locations'],language = request.form['language'],comment = request.form['comment'])


app.run(debug=True)
