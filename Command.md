-> to chech installed or not : django-admin --version

-> to check which python packages are installed : pip freeze

->Install Create and Activate Virtual ENV : 
	- Goto this website and run the command avalable at there : pip install virtualenv
	- create virtual env : virtualenv venv(any name) -> run over your project directory
	- to activate : venv\Scripts\activate
	- to deactivate write inside (venv) : deactivate
        - to uninstall virtual env : pip uninstall virtualenv

-> install django: install django (installed latest)
for specific version : py -m pip install Django==5.1.6 (version)
	- to uninstall django : pip uninstall django == version

-> Create Django Project:
 - if no project folder exists : django-admin startproject projectname
 - if project folder exists : django-admin startproject projectname . (dot) (projectname = foldername)


cd /d D:

-> to run project : python manage.py runserver

