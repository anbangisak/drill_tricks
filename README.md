# drill_tricks
data analytics with datawrkz

# Setup
## Clone Repo
```
git clone repo.git
```

## Installation

### Enable virtual environment
```
pip3 install virtualenv
virtualenv vbase
```

### Install necessary packages for python
```
pip install -r requirements.txt
```

### Install necessary packages for angular

To install nodejs follow below link procedures,
https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04

```
cd anglr/disply
npm install
```

## Run servers

### Run python django server
```
cd drill
python manage.py runserver 0:8200
```

### Run angular proxy server to avoid inter domain API call
```
cd anglr/disply
corsproxy
```

Note: `proxy default port is 1337`

### Run angularJs
```
cd anglr/disply
ng serve
```
