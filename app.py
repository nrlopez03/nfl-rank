from flask import Flask, render_template

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/docs")
def docs():
    return render_template("page.html", title="docs page")

@app.route("/about")
def about():
    return render_template("page.html", title="about page")

if __name__ == "__main__":
    app.run(debug=True)