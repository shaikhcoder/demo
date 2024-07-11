from flask import Flask,render_template,request,make_response,Response

app = Flask(__name__)
port = 5500


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/works")
def works():
    return render_template("works.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_form")
def submit_form():
    if request.method =="POST":
        return render_template("thankyou.html")
    else :
        return (render_template("404.html"),404)


@app.errorhandler(404)
def _404(e):
    return (render_template("404.html"),404)


app.run(port=8000)