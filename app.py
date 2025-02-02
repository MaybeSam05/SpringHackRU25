from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from  main import get_ingredients, get_website_data, get_images, clean_data, mergeDataImage, high_to_low
import json
import os
import sys

app = Flask(__name__)
app.secret_key = '1234'

@app.route("/get-items", methods=["GET", "POST"])
def submit():
    final_data = []
    user_input = request.form.get("user-input") # hamburger buns
    selected_filter = request.form.get('filter')

    if selected_filter == "none":
        ingredients = get_ingredients(user_input) # ["hamburger", "buns"]

        for ingredient in ingredients:
            website = get_website_data(ingredient)
            images = get_images(ingredient)
            individual_data = mergeDataImage(website, images) # [["hamburger", "10.99", img], ["buns", "2.99", img]]
            final_data.append(individual_data)

        return render_template('confirm.html', food=user_input,data=final_data, ingredients=ingredients)
    elif selected_filter == "high-to-low":
        ingredients = get_ingredients(user_input) # ["hamburger", "buns"]

        for ingredient in ingredients:
            website = get_website_data(ingredient)
            images = get_images(ingredient)
            individual_data = mergeDataImage(website, images) # [["hamburger", "10.99", img], ["buns", "2.99", img]]
            individual_data = high_to_low(individual_data, 1)
            final_data.append(individual_data)

        return render_template('confirm.html', food=user_input,data=final_data, ingredients=ingredients)
    else:
        ingredients = get_ingredients(user_input) # ["hamburger", "buns"]

        for ingredient in ingredients:
            website = get_website_data(ingredient)
            images = get_images(ingredient)
            individual_data = mergeDataImage(website, images) # [["hamburger", "10.99", img], ["buns", "2.99", img]]
            individual_data = high_to_low(individual_data, 0)
            final_data.append(individual_data)

        return render_template('confirm.html', food=user_input,data=final_data, ingredients=ingredients)

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    cart_items = request.json.get('items', [])
    # Get existing cart items
    current_cart = session.get('cart', [])
    
    # Add new items to cart
    current_cart.extend(cart_items)
    
    # Update session with new cart
    session['cart'] = current_cart
    # Force session to update
    session.modified = True
    
    return jsonify({"success": True})

@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():
    index = request.json.get('index')
    if 'cart' in session and 0 <= index < len(session['cart']):
        # Remove the item at the specified index
        session['cart'].pop(index)
        session.modified = True
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route("/cart")
def view_cart():
    cart_items = session.get('cart', [])
    return render_template("cart.html", cart_items=cart_items)

@app.route("/", methods=["GET", "POST"])
def home():
    cart_items = session.get('cart', [])
    return render_template("index.html", cart_count=len(cart_items))

if __name__ == '__main__':
    app.run(debug=True, port=5001)