
# Documentation for Fantasy NFL Draft App

Interactive and AI program for NFL Draft assisstance


## Post Data URL
Location: https://github.com/dmscul11/nfldraft
Heroku URL: 


## Install

```
# install conda for python 3
conda create --name handsfree-apple-watch-django python=3.6
source activate handsfree-apple-watch-django
pip install -r requirements.txt
createdb emrstats
python manage.py bower_install
python manage.py migrate
python manage.py collectstatic
```

- [Python3 and Pip3](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
- [NVD3](https://github.com/areski/django-nvd3/blob/develop/README.rst)
- [Bower for NVD3](https://github.com/nvbn/django-bower/blob/master/README.rst)


## Run App Locally

	$ python3 manage.py makemigrations
	$ python3 manage.py migrate
	$ python3 manage.py collectstatic
	$ heroku local web 	# to run app locally
	$ python3 manage.py runserver 5000 	# to run app locally and updates automatically with code changes


## Push Branch Changes

	$ git branch
	$ git status
	$ git add .
	$ python3 manage.py bower_install && python3 manage.py collectstatic --noinput
	$ git commit -m "commit summary"
	$ git push origin branch_name


## Checkout Branch Changes

	$ git checkout -b new_branch_name existing_branch_name	# creates a new branch from an existing
	$ git checkout branch_name
	$ git pull origin branch_name


## Deployment to Heroku

    $ heroku login
    $ heroku git:remote -a apple-watch-backend-django
    $ python3 manage.py bower_install && python3 manage.py collectstatic --noinput
    $ git push heroku master
    $ git push heroku branch_name:master 	# for test git branches

    $ heroku run python3 manage.py makemigrations
    $ heroku run python3 manage.py migrate
    $ heroku run python3 manage.py collectstatic
    $ heroku open
    $ heroku addons:open papertrail		# opens heroku logs


## Access PostgreSQL Database

    # Local database
    $ psql
    	# \list
    $ psql emrstats
    	# delete from emrdata_emrstats;

    # Heroku database
    $ heroku pg:info
    $ heroku pg:psql
    	# \dt
    	# select * from emrdata_datasession;
    	# select * from emrdata_emrstats;


## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
- [Flake8Lint](https://github.com/dreadatour/Flake8Lint)
- See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

