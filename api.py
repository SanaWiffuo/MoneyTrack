import flask
from flask import render_template
from shopee import *
from flask_table import Table, Col


app = flask.Flask(__name__)
app.config["DEBUG"] = True


class ItemTable(Table):
    name = Col('Name')
    price = Col('Price')
    ratings = Col('Ratings')
    url = Col('Url')


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/shoppe', methods=['GET'])
def shoppe():
    product = scrap_shopee("iphone 11 pro", 5)
    table = ItemTable(product)
    return render_template("index.html", table=table)


app.run()
