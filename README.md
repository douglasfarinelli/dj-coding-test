# dj-coding-test
Coding test with django admin painel + API to manager the data

# API HOST

http://localhost:8000/api/v1/employees/

# Recommendations

    - Use python3.5;
    
# Installation

Via Dockerfile:

    $ docker build .
    $ docker docker run --rm -p 8000:8000 <img_id>
    
Or with virtualenv:

    $ virtualenv <path> -p python3.5
    $ source <path>/bin/activate
    $ ./virtualenv-init.sh

# Request

curl -H "Content-Type: application/javascript" http://localhost:8000/api/v1/employees/
