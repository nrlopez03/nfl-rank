from flask import Flask, render_template

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def homepage():
    return render_template("index.html", title="NFL Rank")

if __name__ == "__main__":
    app.run(debug=True)