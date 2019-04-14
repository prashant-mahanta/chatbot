# chatbot
This project is developed using Django framework. 

Rest API for message communication.

``path('api-message/', ChatAppView.as_view(), name="ChatAppView")``

Can test the APIs using POSTMAN.

## Project installation
You need to have Python 3.5+ to run this project.
It's always better to create a virtual environment and install dependencies.

#### Create virtual environment for python
``$ virtualenv venv``

``$ source ./venv/bin/activate``

To install dependencies run:

``(venv)$ pip3 install -r requirements.txt``

#### To run project
``$ python3 manage.py runserver``
