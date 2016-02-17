# Python hackathon

During the hackthon we will build a web app that does fraud detection on (fake) transactional data stored in a Postgress database. 

## Prerequisites

- Python 3 virtual environment with the following packages:

        aniso8601==1.1.0
        Flask==0.10.1
        Flask-Compress==1.3.0
        Flask-REST==1.1
        Flask-RESTful==0.3.5
        itsdangerous==0.24
        Jinja2==2.8
        MarkupSafe==0.23
        psycopg2==2.6.1
        python-dateutil==2.4.2
        pytz==2015.7
        six==1.10.0
        Werkzeug==0.11.2

- Postgres version 9.5 or later
- your favourite IDE

## Outline

During the handson you will:

- build a transactional data generator
- setup a postgres database for storing the transactional data
- build a flask app that provides api to the postrgres db, the app
  - will have several different API end points
  - allows inserting of data via the api
  - performs fraud detection on transactional data
- optional: write test cases for your code
- optional: package the your app

### Step 1: Transactional data generator

Create a fake transacitonal data generator that creates data in the following format:

- account id; integer
- transaction id; integer
- timestamp; string or int (resolution ms)
- transaction value; decimal

Further requirements on the generator:

- the time difference between generated transactions should vary
- the generator should be able to store data in the db
 - through the app api using post requests
 - direct inserting into the db
- should be configurable thoughs some simple parameters; eg post_url, num_transations, etc

### Step 2: Setup the Postgres db

Setup a database such that:

- your app is be able to access the db (create a user etc..)
- it contains a table that can store the transactional data

### Step 3: Create the Flask app

We will built the app by further extending the provided skeleton.

The api should at least implement the following two end points:

- `/is_fraud/<int:account>/` (GET): returns fraudulent events for the specified account
- `/store_data`  (GET + POST): stores transactional data into the db

The fraud detection logic can be implemented in two ways:

- in the db by creating a UDF
- in python code by applying detection to data retrieved from the db

The decection logic itself should be based on a couple of simple rules (eg. amount < 0.9 average(amount))

### Step 4 (optional): Write test cases

Create some nosetests for your developed python app.

###  Step 4 (optional): Package you app

Create a Python package for easy distribution and installation of your app.











