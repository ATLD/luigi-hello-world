# Luigi Example

This is just a simple 'Hello World' example to demonstrate the use of Luigi.

It will create a file that says "Hello", another that says "World", and concatenate the contents of those files into a third that says "Hello World". 

Usage:

```
pipenv install
pipenv shell
luigid --background --port=8082 --logdir=logs
python hello_world.py HelloWorldTask --id=some_id
```
go and see results at:
http://localhost:8082