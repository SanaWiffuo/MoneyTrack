# Productify

Productify helps track products from websites like Shoppe and Lazada.

## Built With

- [Flask](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
- [Bootstrap](https://maven.apache.org/) - Used for styling of websites
- [requests](https://rometools.github.io/rome/) - Used to send http requests
- [bs4](http://www.dropwizard.io/1.0.2/docs/) - Used for scraping
- [fake_useragent](http://www.dropwizard.io/1.0.2/docs/) - Used for masking ip
- [lxml](http://www.dropwizard.io/1.0.2/docs/) - Parser used for receive html pages
- [Pandas](http://www.dropwizard.io/1.0.2/docs/) - Used for data visualization
- [Firebase](http://www.dropwizard.io/1.0.2/docs/) - Used for storage of products and users information
- [pytz](http://www.dropwizard.io/1.0.2/docs/) - Used for formatting timezone

## How It Works

### Scraping

### Tracking

### Webserver

Using Flask as our web framework , it acts as a local web server to launch our website on localhost:5000.

Websites are build with Html , Css , Bootstrap and Javascript. It is compiled by Flask built-in template website template system , Jinja template. The .html files can be found in templates folder , .css and .js files can be found in css folder located in the static folder.

## Getting Started

### Prerequisites

Productify is written in Python 3.6

(Please ensure you have [Python 3.6](https://www.python.org/downloads/release/python-360/) installed)

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
