import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="Aboot", recipes=data)

@app.route("/about/<recipe_name>")
def about_recipe(recipe_name):
    recipe = {}
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == recipe_name:
                recipe = obj
    return render_template("recipe.html", recipe=recipe)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("Hello My Friend")
        print(request.form)
        print(request.form.get("name"))
        print(request.form["name"])
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
