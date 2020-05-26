# Python

python3 -m venv venv
. venv/bin/activate

pip install Flask
pip install gunicorn

# Heroku

heroku login
heroku create
git push heroku master