from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Find Your Crop Page
@app.route("/findyourcrop")
def findyourcrop():
    return render_template("findyourcrop.html")

if __name__ == "__main__":
    app.run(debug=True)
