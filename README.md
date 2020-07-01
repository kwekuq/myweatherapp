My Weather App

![Django CI](https://github.com/kwekuq/myweatherapp/workflows/Django%20CI/badge.svg)

To run:
1. Clone repo

2. `pip install -r requirements.txt`

3. `python manage.py migrate --settings=myweatherapp.settings.dev`

4. `python manage.py test --settings=myweatherapp.settings.dev`

5. `python manage.py runserver --settings=myweatherapp.settings.dev`