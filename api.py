import flask
from shopee import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/shoppe', methods=['GET'])
def shoppe():
    line = ""
    product = scrap_shopee("monitor", 5)
    for i in product:
        line += """ <tr ><td >{0}</td><td >{1}</td><td >{2}</td><td >{3}</td></tr >""".format(
            i.name, i.price, i.ratings, i.url)
    return"""<table ><tr ><th >Name< /th ><th >Price< /th ><th >Ratings< /th ><th >Url< /th ></tr >{}</table >""".format(line)


app.run()
