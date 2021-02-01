## Articles Django App

# How to run & install
Clone repo & rename .env.example file to .env
```
git clone https://github.com/Namnetsy/articles-django-app
cd articles-django-app
cp .env.example .env
```

Create and activate a virtual environment.
```
python3 -m venv workenv
source workenv/bin/activate
```

Install dependencies.
```
pip install -r requirements.txt
```

Apply database migrations, collect static files & create a super user
```
cd articles
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

Run the app.
```
python manage.py runserver
```
