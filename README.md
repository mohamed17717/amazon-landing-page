# Amazon Landnig Page

Magical stick to create __landing page__ for your product coupon on __Amazon__ using only the product's link

## Getting Started

### Prerequisites

- [Python3](https://www.python.org/downloads/).6 or later

### Installing

Create virtual environment

``` bash
$ pip install --upgrade virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate && cd env
```

Clone The repository, install dependencies and run.

``` bash
(env) $ git clone https://github.com/mohamed17717/amazon-landing-page src && cd src
(env) $ pip install -r requirements.txt
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py runserver
```

## Built With

- Django -  The web framework used

- SASS - Preprocessor for css

- GULP - Task Runner

## Features

- User don't need an account to start

- User determine coupon's code, sele percent, life long and howmany

- Scrape and extract wanted data by only the product's link

- Timer for the coupon life

- Counter for remaining and used coupons

- All images for the product that are on amazon page

- Old and new price

- Nice Simple Desgin