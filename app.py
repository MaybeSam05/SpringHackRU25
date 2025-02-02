from flask import Flask, render_template, request, redirect, url_for, jsonify
from  main import get_ingredients, get_website_data, get_images, clean_data, mergeDataImage
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/get-items", methods=["GET", "POST"])
def submit():
    final_data = []
    user_input = request.form.get("user-input") # hamburger buns
    ingredients = get_ingredients(user_input) # ["hamburger", "buns"]
    
    for ingredient in ingredients:
        website = get_website_data(ingredient)
        images = get_images(ingredient)
        individual_data = mergeDataImage(website, images) # [["hamburger", "10.99", img], ["buns", "2.99", img]]
        final_data.append(individual_data)

    return render_template('confirm.html', food=user_input,data=final_data, ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)