# Final_Project

### LOCAL INSTALLATION (windows sytems)
#### create a directory in your drive C:
mkdir /c/g1
mkdir /c/g1/database
mkdir /c/g1/source
mdkir /c/g1/virtualenv
mkdir /c/g1/static

#### clone project into source folder
git clone https://github.com/CS673S15-Group1/Final_Project /c/g1/source

#### create a virtualenviroment
##### must have installed python 2.7 to the default directory in C:\Python27
##### must have virtual env installed 'pip install virtualenv' -- must have pip installed, usually included on windows system installs
virtualenv -p /c/Python27/python.exe /c/g1/virtualenv

#### change directory to the project source
cd /c/g1/source/group1

#### install dependencies 
##### windependencies file for windows since readline is not compatible, may have to change all 'import readline' to 'import pyreadline as readline'
../../virtualenv/Scripts/pip.exe install -r ../windependencies.txt

#### make the migration files
../../virtualenv/Scripts/python.exe manage.py makemigrations

#### run the database migration
../../virtualenv/Scripts/python.exe manage.py migrate

#### run server, navigate to http://localhost:8000 in a browser
../../virtualenv/Scripts/python.exe manage.py runserver



### LOCAL INSTALLATION (*nix sytems [Mac, Ubuntu...])
#### create a directory in your home directory
mkdir ~/g1
mkdir ~/g1/database
mkdir ~/g1/source
mdkir ~/g1/virtualenv
mkdir ~/g1/static

#### clone project into source folder
git clone https://github.com/CS673S15-Group1/Final_Project ~/g1/source

#### create a virtualenviroment
##### must have installed python 2.7 to the default directory in /usr/local/bin with a python2.7 executable via altinstall
##### must have virtual env installed 'pip install virtualenv' -- must have pip installed, usually included on windows system installs
##### see server installation script under deploy_tools for details on installing a new python
virtualenv - p /usr/local/bin/python2.7 ~/g1/virtualenv

#### change directory to the project source
cd ~/g1/source/group1

#### install dependencies 
##### windependencies file for windows since readline is not compatible, may have to change all 'import readline' to 'import pyreadline as readline'
../../virtualenv/bin/pip install -r ../dependencies.txt

#### make the migration files
../../virtualenv/bin/python manage.py makemigrations

#### run the database migration
../../virtualenv/bin/python manage.py migrate

#### run server, navigate to http://localhost:8000 in a browser
../../virtualenv/bin/python manage.py runserver