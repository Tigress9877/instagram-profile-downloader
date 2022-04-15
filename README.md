# Introduction
This project is written with django-rest and it can be usefull for getting image of any accounts of **instagram** profile.

# Usage
At first create your virtual environment: 

`
python -m venv env
`

`
source env/bin/activate
`

`
pip install -r requirements.txt
`

Then start your server:

`
python manage.py makemigrations
`

`
python manage.py migrate
`

`
python manage.py runserver
`

Next send your username to the server with POST HTTP request and JSON format like:

`
{
	"username": "TEST"
}
`