### Access server
ssh jsolly@69.164.205.120

### Create new migration
 python3 manage.py makemigrations --name changed_my_model your_app_label
 python3 manage.py migrate


After pulling new changes from github
python3 manage.py check --deploy

1 - source venv/bib/activate to get the Python virtual env
2 - python3 manage.py migrate (to inherit db changes) # Don't need to makemigrations, because migrations are already in git
3 - sudo chmod -R 777 blogthedata
4 - sudo service apache2 restart  


# login to postgres in terminal
psql -U postgres

# test on mobile
ngrok http 8000

# important paths
sudo tail -f /var/log/apache2/access.log
sudo tail -f /var/log/apache2/error.log
sudo nano /etc/django_config.json 
sudo nano -c /etc/apache2/sites-available/django_project.conf
/var/log/postgresql/postgresql-13-main.log
/etc/postgresql-common/createcluster.conf 
sudo nano /etc/apache2/apache2.conf


# Other useful commands
sudo service postgresql restart
sudo chmod -R 777 blogthedata
become root user -> sudo -i

### Postgres export and restore
sudo -u postgres pg_dump blogthedata > blogthedata_db_3_8_22.sql
scp jsolly@69.164.205.120:/home/jsolly/backups/blogthedata_db_3_8_22.sql .
psql -U postgres
postgres=# DROP DATABASE blogthedata;
postgres=# CREATE DATABASE blogthedata;
exit
psql blogthedata < blogthedata_db_5_6_22.sql

# Copy over media folder
scp -r jsolly@69.164.205.120:/home/jsolly/blogthedata/django_project/media .

### Backup Linode
ssh jsolly@69.164.205.120 "dd if=/dev/sda " | dd of=/Users/johnsolly/Documents/code/blogthedata/backups/linode.img


### Code Coverage
coverage run -m unittest discover django_project 
coverage report -m --skip-empty --skip-covered
coverage html --skip-empty -d blog/templates/htmlcov

### Linting (flake8)
flake8 django_project

### Setup new test database
- Configure settings.py to point to a sqlite database
- run python3 manage.py migrate to create all the tables in sqlite

### Upgrade django
- Check for depreciations and make sure unit tests are passing
python3 -Wa manage.py test
- Freeze dependencies
pip freeze > requirements_5_4_22.txt
- Upgrade
pip install Django==3.2.13
- Re-run unit tests
- commit dependencies to source control
- use dependencies to upgrade prod
pip install -r requirements_5_4_22.txt

# Create new venv
make sure an up-to-date pip freeze has happened
make sure you're using the right python version

$ python3 -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt

# Configuring Python install on new Mac
Install using the regular installer from python.org. Make sure to match the version that is on production.
The file path should look like:
/Applications/"Python 3.9"/IDLE.app/Contents/MacOS/Python

Go into Applications/<Python Directory>
Open 'Install Certificates.command'


 ### Roll back migration
 python3 manage.py migrate blog 0011

 ### Roll back a currupt db on production
 # Log into postgres
 psql -U postgres
 # drop existing database
postgres=# DROP DATABASE blogthedata;
# Create an empty db
postgres=# CREATE DATABASE blogthedata;
type <exit> and hit enter to go back to the terminal
# Cd to the backups folder and restore the db
psql blogthedata < blogthedata_db_5_5_22.sql
# If that doesn't work, try
sudo -u postgres psql blogthedata < blogthedata_db_5_5_22.sql


# Not needed anymore
python3 manage.py collectstatic
scp jsolly@69.164.205.120:/home/jsolly/blogthedata/django_project/db.sqlite3 .