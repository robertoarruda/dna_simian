# Teste Símios - Mercado Livre

## Prerequisites
- Python 3.8 `sudo apt install python3.8`
- Pip `sudo apt install python3-pip`
- VirtualEnv `sudo pip3 install virtualenv`

## Installation

### Clone the project:
```
git clone git@github.com:robertoarruda/test_meli.git
```

### Enter the project directory:
```
cd ./test_meli
```

### Create the Environment:
Within the project root, run the command below:
```
virtualenv venv --python=python3.8
```

### Activate the environment:
Run the command below to enable:
```
source venv/bin/activate
```

### Install dependencies:
Run the command below to install the project dependencies:
```
pip install -r requirements.txt
```

### Run API:
Execute the command below to run the crawler:
```
python main.py
```

### Turn off the environment:
Execute the command below to deactivate:
```
deactivate
```
## Unit tests:
Execute the command below to run unit tests:
```
coverage run --source=dna -m unittest
```

Execute command below to see test coverage:
```
coverage report -m
```
```
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
dna/__init__.py              0      0   100%
dna/service.py              39      0   100%
dna/simian_analyzer.py     110      0   100%
dna/validator.py            26      0   100%
------------------------------------------------------
TOTAL                      175      0   100%
```

## Demo [AWS]
### [POST] /simian
To verify that a DNA is simian, run the following command:
```
curl -v --request POST \
  --url http://54.211.82.161:5000/simian \
  --header 'content-type: application/json' \
  --data '{
    "dna": [
        "AT",
        "GC"
    ]
}'
```

If the DNA is identified as a simian, you will get an HTTP 200-OK:
```
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 61
< Server: Werkzeug/0.16.0 Python/3.8.0
< Date: Fri, 27 Dec 2019 12:23:14 GMT
```

Otherwise an HTTP 403-FORBIDDEN:
```
< HTTP/1.0 403 FORBIDDEN
< Content-Type: text/html; charset=utf-8
< Content-Length: 0
< Server: Werkzeug/0.16.0 Python/3.8.0
< Date: Fri, 27 Dec 2019 12:43:36 GMT
```
### [GET] /stats
To query DNA checks statistics, run the following command:
```
curl --request GET \
  --url http://54.211.82.161:5000/stats
```

This query will return the following json:
```
{"count_mutant_dna": 40, "count_human_dna": 100: "ratio": 0.4}
```
