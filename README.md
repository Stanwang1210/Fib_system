# Fib_system
- Install depenency
```bash
$ pip3 install -r requirements.txt
```
- Migrate database tables
```bash
$ python3 manage.py migrate
```
- Run the REST server
```bash
$ python3 django-rest-tutorial/mysite/manage.py runserver               
```
- Run the gRPC Fibonacci server
```bash
$ python3 gRPC-with-protobuf/server.py 
```

- Note that if the build/ directory doesn't exist in any server directory (gRPC/Fib/, REST/ ...)
  run ```make``` before running the server


## Using `http` to perform client request
- POST request
- e.g. if order = 11
```bash
$ sudo apt-get install httpie
$ http --form POST http://localhost:8000/rest/tutorial data="{'order':11}"
```

- GET request
```
$ http --form GET http://localhost:8000/rest/tutorial 
```
