web: python app/manage.py collectstatic --noinput; python app/manage.py migrate; gunicorn --pythonpath app app.config.wsgi --log-file -
