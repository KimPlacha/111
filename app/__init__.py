#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sample hello world Flask app"""

from flask import Flask


app = Flask(__name__)
@app.route("/")
def hello():
    return '<h1>Hello World!</h1>'

@app.route("/products")
def products():
    products_list = ["Apple", "Banana", "Cherry"]
    bullet_list = "".join(f"<li>{product}</li>" for product in products_list)
    return f"<ul>{bullet_list}</ul>"FLASK