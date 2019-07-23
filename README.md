# Amazon Landnig Page

Magical stick to create **landing page** for your product coupon on **Amazon** using only the product's link

## Getting Started

### Prerequisites

- [Python3.6](https://www.python.org/downloads/) or later

### Installing

Create virtual environment

``` bash
pip install --upgrade virtualenv
virtualenv -p python3 env
source env/bin/activate && cd env
```

Clone The repository, install dependencies and run.

``` bash
(env) $ git clone https://github.com/mohamed17717/amazon-landing-page.git src && cd src
(env) $ pip install -r requirements.txt
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

## Built With

- **Django** -  Web framework
- **Requests / Beautiful Soup** - Scraping tools
- **SASS** - Preprocessor for css
- **GULP** - Task Runner

## Features

- User doesn't need an account to start

- User determine coupon's code, sale percent, life long and howmany

- Scrape and extract wanted data by only the product's link

- Simple Desgin contain :
  - All images for the product that are on amazon page
  - Timer for the coupon life
  - Counter for remaining and used coupons
  - Old and new price
