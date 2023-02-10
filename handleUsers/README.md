# START

Open VS Code, cd into the main folder
- mkdir folder_name (eg: project_folder)
- cd project_folder

Create a virtual environment in the folder (before adding the new django project, it's easier than conficuring a venv after project creation):
- python -m venv name-virtual-environment
- C:\Users\PESSAE\Documents\webserver\django> name-virtual-environment\Scripts\activate

Install django and djangorest (pay attention to eventual proxy)
- pip install --proxy=http://proxy-xxxxxxxx:801 django (whatch out http vs htpps!!!)
- pip install djangorestframework

Install cors
How CORS works https://www.stackhawk.com/blog/angular-cors-guide-examples-and-how-to-enable-it/ and https://www.stackhawk.com/blog/what-is-cors/
- pip install django-cors-headers
- in settings.py add corsheaders to INSTALLED APPS = [ ..., 'corsheaders']
- in settings.py add to MIDDLEWARE = [ ..., 'corsheaders.middleware.CorsMiddleware']
- in settings.py add
  CORS_ALLOWED_ORIGINS = ['http://localhost:4200']
  CORS_ALLOW_ALL_ORIGINS = False

Install trough requirements (not mandatory step, requirements now are for frontend dashboard template)
- pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 -r requirements.txt

Create the project
-  django-admin startproject project_name

Create GIT
- git init
- git remote add origin **URL**
- create .gitignore

Create README
- and copy from past projects

Create basic database for users (inside project_name)
- cd project_name ()
- python manage.py migrate
- python manage.py runserver (just as a test, then CTRL+C)

Create superuser
- python manage.py createsuperuser (administrator - administrator@localhost.com - com04***) http://127.0.0.1:8000/admin/

Delete django key (if product has to go on production, otherwise if it runs locally it can stay there)

Run server from cdm (inside project folder)
- python manage.py runserver

Create new app (in project_name)
- python manage.py startapp app_name (eg: api)
- add app-name to INSTALLED APPS in mainProject/mainProject/settings.py
  INSTALLED_APPS = [
    'django.contrib.admin',
    . . .
    'app-name',
  ]
- create a url.py inside app_name (eg: inside api)
In mainProject/mainProject/urls.py
- add include in from django.urls import path, include
- add urls to urlpatterns in the form of path('api/', include('api.urls'))

Register the models in the admin interface


# Create api service

Create a model and migrate it so the table is created in the db
- Create a model (table structure) in api/models.py
- python manage.py makemigrations (it creates a mainProject/api/migrations/0001_initial.py file and eventually a mainProject/db.sqlite3 if not present)
  to peak at the db see the section below
- python manage.py migrate

Create a serializer
- in project/app-name (es: project_name/api) create a serializer.py file with
  from rest_framework import serializers
  from .models import woman, path

  class womanSerializer(serializers.ModelSerializer):
    class Meta:
      model = woman
      fields = '__all__'
      depth = 1
- for linked (aka related) data, the detault option is to show just the id of the object, adding a depth allows to specify how many nested informations should be returned (eg: depth = 1  returns one nested object inside a key, depth 2 returns a nested object inside a nested object in a key...)

# Create a view



# Add the tables to the admin view
- in admin.py (es: project_name/api/admin.py) import the models and add to register
  from .models import User, Railway, Question, Video, Result
  admin.site.register(User)

# CREATE A LOGIN PAGE
- Check that in settings.py in INSTALLED APPS is included 
  'django.contrib.auth'
- in the main url.py file add 
  path("accounts/", include("django.contrib.auth.urls")),  # to use django.auth and implement login page
- The URLs provided by auth are: 
    accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
- django.contrib.auth will look for templates inside templates/registration, so create that folder if it's not there. To know where django will look for the templates folder
  go to settings.py and search for TEMPLATE_DIR (or TEMPATES[DIR] in some projects)
  TEMPLATE_DIR = os.path.join(CORE_DIR, "api/templates")  # ROOT dir for templates (es: api/templates/registration)
- create a login.html for a login page, remember to use the simplest <form> (just method and button type). Also remember the csrf token
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log In</button>
  </form>

## ALLOW TO SEE PAGES BASED ON PERMISSIONS
- Every time you add a model django creates some basic permissions
  applabel.add_modelname
  applabel.view_modelname
  applabel.change_modelname
  applabel.delete_modelname (es: api.delete_customuser)
- Above the page function add a decorator to decide who should see that page
  @permission_required('api.add_askuser', raise_exception=True)



# Create an authentication tool - https://www.jetbrains.com/pycharm/guide/tutorials/django-aws/rest-api-jwt/

https://www.youtube.com/watch?v=PUzgZrS_piQ

- pip install djangorestframework-simplejwt
- in setting.py add
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
- in urls.py import
  from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
- in urls.py add to urlpatterns
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
- in urls.py in urlspatterns add wich adds the prefined user urls (es accounts/login/[name='login'])
  path('accounts/', include('django.contrib.auth.urls')),
  https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication

- in api/views.py import
from rest_framework.permissions import IsAuthenticated
- in api/views.py import
from rest_framework.decorators import api_view, permission_classes
- in api/views.py add
  @api_view(['GET'])
  @permission_classes([IsAuthenticated])

# Create relations among tables
- first parameter is the name of the model that we want to link
- second parameter is what happens on delete
--- models.foreignKey(..., on_delete=models.SET_NUL, null=True) so it will make the property null if the linked model gets deleted
--- models.foreignKey(..., on_delete=models.CASCADE) so it will delete the child if the parent gets deleted
- related_name is the parameter that allows us to query reverse in a one-to-many relationship (eg: I've got many articles by one author, article has a foreignKey to author, adding a related_name I'm able to query all the articles written by that author)

https://betterprogramming.pub/django-select-related-and-prefetch-related-f23043fd635d


https://thetldr.tech/how-to-query-reverse-foreign-key-relationship-in-django-queryset/

# CREATE AN API
- requires, model, serializer, view and a migration
- *** IF NOT USING SQLite3 CREATE THE DATABASE HERE, BEFORE MAKING MIGRATIONS ***
- crete a model (table structure) in mainProject/api/models.py
  -- adding blank=True in the model type makes it not required (es: models.EmailField(blank=True))
- make a migration (to create the table) with: python manage.py makemigrations api
  (it creates a mainProject/api/migrations/0001_initial.py file and eventually a mainProject/db.sqlite3 if not present)
  to peak at the db see the section below
  *** REMEMBER THAT WHEN YOU NEED TO UPDATE A MIGRATION (A DB) THE COMMMAND IS: python manage.py migrate ***
  it creates a table that has app-name_model-name (es: api_women)
- create a serializer (transform tables data in python dictionaries - objects) in mainProject/api/serializer.py
  -- serialization is the process of converting a Model to JSON and allows to specify what fields should be present in the JSON representation of the model (so I can drop the _id autoGenereted and use a custom id)
  -- here you can set up custom validatiors and say if a field is required or not
- create a view in mainProject/api/viwes.py
  remember to import the model and the serializer in the view
- create an url path in mainProject/api/urls.py

python manage.py makemigrations









## ADD A NEW FILED TO DB
- add it in the model
- add it in the serializer
- make migration, migrate

## DB PEAKING (SQLITE3)
- if it gives a CommandError: You appear not to have the 'sqlite3' program installed or on your path. copy the sql.exe file in the same folder as manage.py

- cd into mainProject and in a shell type command: python manage.py dbshell
- >>> .tables (to see all tables)
- >>> .schema --indent table-name (see the stricture)
- >>> select * from table-name
https://realpython.com/django-migrations-a-primer/

## DB MONGODB
- Install djnongo using:
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 djongo
- install the right mongoengine
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 mongoengine
- install the right pymongo versione (eventually remove if its >4.0)
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1
- in settings.py change the default DATABASE in
  DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': 'w-database',
      }
  }
- in project/app-name/models.py change che import models from django.db to
  from djongo import models
- makemigrations and then migrate to change to mongoDB:
  python manage.py makemigrations
  python manage.py migrate
  *** REMEMBER: makemigration creates the file to create the tables, migrates actually creates them ***

## CSS 
- create a static folder in the main project (so it's accessable from every app), inside you can create the folders css, img, js...
- in settings make sure that a static path is specified with
  STATIC_URL = 'static/'
  STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), BASE_DIR / "static",
  ]

## CONSTANTS
- to show a constant in a template (es: app name) create a constants.py file in the app folder (es: api/constants.py)
- create a constant in the form of an object with multiple key values co you can import just one object in all pages and have all the values
- in the view file import the constants file
  from .constants import MY_CONST
- in the single view function create a contect (has to be an object, with the key value 'MY_CONST': MY_CONST )
  def user_overview(request):
    userList = customUser.objects.all()
    return render(request, 'user_overview.html', {'userList': userList, 'MY_CONST': MY_CONST})
- in the template use the constant as {{MY_CONST.keyName}}    

*** NESTED MODELS ***
- add _id = models.ObjectIdField() to the model fields of the nested model in order to have nested models



# ERRORS

*** WITH ERROR NotImplementedError: Database objects do not implement truth value testing or bool(). Please compare with None instead: database is not None ***
- pymongo version might be wrong, use 3.12.1
  pip uninstall pymongo
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 pymongo==3.12.1

*** WITH ERROR cannot be of type "<class \'django.db.models.fields.BigAutoField\'>" ***
- If it's a mega object with nested objects defined as models, remember to add abstract = True to the Meta class, wich means that djongo won't create a new "table" for the model just include the field where you embedded them
- it's best to reset the DB and migrate again by
  -- in migration folder KEEP __init__.py and delete all the other files
  -- python manage.py makepigrations
  -- python manage.py migrate

*** WITH CORS ERROR - Access to XMLHttpRequest at 'url’' from origin  has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource ***


*** WITH CSS NOT LOADING ***
- https://learndjango.com/tutorials/django-static-files
- https://docs.djangoproject.com/en/4.0/howto/static-files/




reset DB
https://dev.to/rawas_aditya/how-to-reset-django-migrations-169o


## MANAGE URLS
- In main project folder urls.py you can link the ursl.py of a specific app within the main project inside urlpatterns in the form:
  path('sample/', include('sample.urls'))
- remember to have include imported at the top:
  from django.urls import path, include
- Create a ursl.py within the app folder to specify urls for the subfolder (the urs will be ip/root-name-main-urls/root-name-app-urls) :
  from django.urls import path
  from . import views
  urlpatterns = [
    path('pageOne', views.pageOneFunction, name='pageOneName'),
  ]
- In settings.py in the main projects add the string with the app name to INSTALLED APPS
  INSTALLED_APPS = [
    'django.contrib.admin',
    . . .
    'sample',
  ]






## MODELS SPECIFICS
To use constants for models,
- Create a separate file (es modelsConstat)
- Import it on the main models in the form of: from my-app-name.modelConstants import *


reset DB
https://dev.to/rawas_aditya/how-to-reset-django-migrations-169o




### CREATE VIEWS
- In the app folder views.py specify the functions that link to the template in the form

def pageOneFunction(request):
    return render(request, 'pageOne.html', {})

- In the app folder create a folder named templates and inside the pageOne.html. It's important to create templates because django will look for it

    sample/templates/pageOne.html


## DJANGO ADMIN CUSTOM
- The files are in venv/django/contrib/admin/templates



## GITHUB
git init
git add README.md
git config --global http.proxy http[s]://username:password@proxyipaddress:portnumber
git config --global user.name "NICK"
git config --global user.mail mail@gmail.com
git config --global user.password *********
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/flond7/angular-startingPoint.git
git push -u origin main

git branch (check branch name)
git branch -mv origin master (change name from origin to master)

git remote -v (check origin)
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git (change repository)


## DJANGO REST FRAMEWORK
- in the api app add models (one table one model) modifying mainProject/api/models.py


## REST
https://www.bezkoder.com/django-angular-crud-rest-framework/

# REST - USER AUTHENTICATION AND PERMISSIONS https://spapas.github.io/2021/08/25/django-token-rest-auth/
- install dj-rest-auth
  pip install dj-rest-auth
- in the main urls.py add  (if you want to see the specific urls go to the generic url 127.0.0.1:8000 and move from there)
  path('auth/', include('dj_rest_auth.urls')),
- in settings.py add
  INSTALLED_APPS = [
    . . .
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    . . . 
  ]
- in the specific views.py (api/views.py)
  from rest_framework.authentication import SessionAuthentication, TokenAuthentication
  from rest_framework.permissions import IsAuthenticated
- in views.py add in each view the requirement for authentication and permissions
  class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
## login
- from the front end call http://127.0.0.1:8000/auth/login/ passing as data a JSON as {"username": "foo", "password": "myPassword"}. It will return a JSON as { "key": "xxxx"}
## access protected views
- from the front end call the view url and pass the key in the header as 
  Authorization:Token xxxxx



## CSV
https://blog.logrocket.com/filtering-querysets-dynamically-in-django/


# SU LINUX MINT
## set proxy
- sudo nano /etc/environment
- add config proxy insiel
  export proxy_http="http://172.25.10.10:801"
  export proxy_https="https://172.25.10.10:801"
  export proxy_ftp="http://172.25.10.10:801"
  export no_proxyp="localhost,172.0.0.1"
## install apache
- sudo apt-get install apache2 apache2-utils libexpat1 ssl-cert python (then check with http://localhost to see if everything is ok)
## install mod_wsgi (needed to deploy django in apache)
- sudo apt-get install libapache2-mod-wsgi
- sudo service apache2 restart
- sudo nano /var/www/html/test-wsgi.py
  create a test file to see if the module is working
  
  def application(environ,start_response):
    status = '200 OK'
    html = '<html>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'Welcome to Apache with mod_wsgi \n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]

- sudo nano /etc/apache2/conf-available/mod-wsgi.conf
  add this content to check if the mod is working
  WSGIScriptAlias /test-wsgi /var/www/html/test-wsgi.py
- a2enconf mod-wsgi
- sudo service apache2 restart
- open browser and check  http://your-server-ip/test-wsgi
## configure apache2 for django
- sudo nano /etc/apache2/apache2.conf (this is for ubuntu related OS, for others it might be an httpd.conf file, if OS is different check on https://cwiki.apache.org/confluence/display/HTTPD/DistrosDefaultLayout)
- at the end of the file add

  WSGIScriptAlias /var/www/html/utenti/handleUsers/handleUsers/wsgi.py
  WSGIPythonHome /var/www/html/utenti/venv
  WSGIPythonPath /var/www/html/utenti

  <Directory /var/www/html/utenti/handleUsers>
  <Files wsgi.py>
  Require all granted
  </Files>
  </Directory>

- for details about commands meaning see https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/modwsgi/




## install mod_wsgi (needed to deploy django in apache)
- sudo apt-get install libapache2-mod-wsgi-py3  
- sudo nano /etc/apache2/sites-available/000-default.conf
  (substitute the default config with this one)

  <VirtualHost *:80>

    # where to save error logs
    # folder has to exist so check or create it
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combine

    # to correctly serve static files specify where to go when apache sees /static pointing to the static directory with absolute path
    # and grant all permissions for that directory
    alias /static /var/www/html/utenti/handleUsers/static
    <Directory /var/www/html/utenti/handleUsers/static>
      Require all granted
    </Directory>

    # directory points to where wsgi.py is
    <Directory /var/www/html/utenti/handleUsers/handleUsers>
      Require all granted
    </Directory>

    # first param is the process name, it can be whatever you want, es "handleUsers"
    # python-home points to /venv
    # python-path point to where manage.py is
    WSGIDaemonProcess handleUsers python-home=/var/www/html/utenti/venv python-path=/var/www/html/utenti/handleUsers
    # processGroup just has to have the same name as the process above
    WSGIProcessGroup handleUsers
    # when apache sees root I want it to see the django app (points to wsgi.py)
    WSGIScriptAlias / /var/www/html/utenti/handleUsers/handleUsers/wsgi.py
  </VirtualHost>
- apachectl configtest (check if syntax is ok, don't worry about eventual server name error)
- service apache2 restart
# correctly serve static files
- create a STATIC_ROOT in settings.py with the absolute url from apache pointing to the static folder
  STATIC_ROOT = '/var/www/html/handleUsers'
- test the application
# make sure the correct user is running the files
- nano /etc/apache2/envars
  look for APACHE_RUN_USER and APACHE_RUN_GROUP to know which user and group you need to abilitate as owners (probably www-data)
- cd where the db is
  cd /var/www/html/utenti/handleUsers
- sudo chown www-data:www-data db.sqlite3
- cd to the enclosing folder and change owner there too
  cd ..
  sudo chown www-data:www-data handleUsers
- service apache2 restart

## ERROR attempt to write a readonly database (SQLITE)
- permission might be setted wrong, check both the sqlite db and the folder enclosing it, they have to have all permissions with the right user
- cd /var/www/html/utenti/handleUsers
- chmod +rwx db.sqlite3





https://www.google.com/search?client=firefox-b-d&q=django+on+apache+2#fpstate=ive&scso=_ZsHkY4mGJfCFxc8PsP-kSA_32:872&vld=cid:5cca81a2,vid:UY_UIH89elA,st:2232



## set permissions
- cd /var/www
- change the html folder owner and set it as the administrator user. If you put : after the user name it will choos authomatically the right group
  chown NOMEUTENTE: html
- cd html
- mkdir NOME_CARTELLA_PROGETTO (es: utenti) 
- check if the new folder has the right owner (ls -la) and eventually change them
  sudo chown NOMEUTENTE: NOME_CARTELLA_PROGETTO (es sudo chown nodeweaver: utenti)
## copy files
- use something like bitwise/filezilla to transfer the files to the new server
- ** don't copy the venv folder, it will have to be created and populated from scratch ** 
## install php8
- sudo apt update
- sudo apt upgrade
- sudo apt install software-properties-common
- sudo add-apt-repository ppa:ondrej/php 
If there is an error try
- sudo -E add-apt-repository ppa:ondrej/php
- sudo apt update
- sudo apt install php8.0
## activate for the first time the venv environment
You have to create the venv environment
- python -m venv venv (if it doesn't work try "python3 -m venv venv" if it still doesn't work see next line then try again this one or the python3 version)
--- sudo apt install python3.8-venv
- source venv/bin/activate (activate the venv)
## install django and libraries
- cd PROJECTFOLDER
- pip install -r requirements.txt
## start django server and check
- python manage.py runserver
- check on linux with a browser localhost (apache webpage) and 127.0.0.1:8080/api/user_overview
## make the page visible from the same LAN
https://guide.debianizzati.org/index.php/Apache_e_Virtual_Hosts:_configurare_Apache2_per_ospitare_pi%C3%B9_siti_web




# SU RASBBERRY
- Make sure you have the proxy configured (see below)
- Create project folder in var/www/html/projectFolder
- Create the virtual environment and activate it
  python -m venv venv (create a venv virtuanl environment)
  source venv/bin/activate (to activate the venv environment)
- Install django
  pip install --proxy=http://proxy-xxxxxxxx:801 django==4.1
- copy the files with bitvise ssh client (main project-folder) inside the var/www/html/projectFolder (so you have venv and then the project-folder)
- Insall the other requirements
  cd var/www/html/projectFolder/project-folder
  pip install --proxy=http://proxy-bc-el.regione.fvg.it:801 -r requirements.txt
- Run the server (it will let you see if there are some libraries you still have to install, in that case install them)
  python manage.py runserver 0.0.0.0:3000
- access the webpage from anywhere on local network trough http://172.20.34.138:3000/api/user_overview


## CONFIG PROXY ON RASPBERRY (https://www.pitronica.com/tutorials/pi-tutorials/raspberry-pi-behind-a-proxy-server/)
- Make sure you have the proxy configured for APT
  sudo nano /etc/apt/apt.conf
  Acquire::http::Proxy "http://192.168.10.10:8081"; (line to add)
### proxy for the general environment ### (THIS ONE WORKS!!!)
- sudo nano /etc/environment
- eport both http_proxy and https_proxy (add both lines with http if you don't have an https)
  export http_proxy="http://proxy-xxxx:801"
  export https_proxy="http://proxy-xxxx:801"
- modify the visudo file that allows to use sudo on some commands
- add these settings to the sudoers file
  sudo visudo
- Add the following line to the file so sudo will use the environment variables you just created
  Defaults    env_keep+="http_proxy https_proxy no_proxy"
- reboot



## EMAIL da django
- https://www.sitepoint.com/django-send-email/