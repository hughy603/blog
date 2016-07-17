# blog
A blog written in Django and hosted on aws

# Virtual Environment Setup

## Install Virtual Environment Wrapper
sudo pip-3.4 install virtualenvwrapper

###### Add the following to .bashrc
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh


###### Reset Environment
. ~/.bashrc

## Environment Setup
mkvirtualenv blog
workon blug
