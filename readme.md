# Productify

Productify helps track products from websites like Shoppe and Lazada.

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - Used for styling of websites
- [requests](https://pypi.org/project/requests/) - Used to send http requests
- [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used for scraping
- [fake_useragent](https://pypi.org/project/fake-useragent/) - Used for chnaging browser user agents
- [lxml](https://lxml.de/) - Parser used for receive html pages
- [Pandas](https://pandas.pydata.org/) - Used for data visualization
- [Firebase](https://firebase.google.com/products) - Used for storage of products and users information
- [pytz](https://pypi.org/project/pytz/) - Used for formatting timezone

## How It Works

Our project can be run on the console , preferably a [bash](<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>) shell.

### Scraping

### Tracking

### Webserver

Using Flask as our web framework , it acts as a local web server to launch our website on localhost:5000.

Websites are build with Html , Css , Bootstrap and Javascript. It is compiled by Flask built-in website template system , [Jinja template](https://jinja.palletsprojects.com/en/2.11.x/).

Flask is used for backend programming of the website , for example routing of web pages. Each webpage has its speceifc function.

api.py is the Flask file. .html files can be found in templates folder and .css and .js files can be found in css folder located in the static folder.

## Getting Started

### Prerequisites

Productify is written in Python 3.6 . (Please ensure you have Python 3.6 installed)

[Download here](https://www.python.org/downloads/release/python-360/)

It recommend that you create a virtual environment with python 3.6

### Installing

Use the package manager pip to install the following python libraries.

(Please ensure you are in the project folder)

```bash
pip3 install -r setup.txt
```

## Usage

```bash
python3 api.py
```

## Authors

- **Haoman**

- **Zachary**
