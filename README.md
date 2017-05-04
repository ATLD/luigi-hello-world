# Luigi Example

This is just a simple 'Hello World' example to demonstrate the use of Luigi.

It will create a file that says "Hello", and another that says "World". 

Usage:

```
pip install venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
luigid --background --port=8082 --logdir=logs
python hello_world.py HelloTask
python hello_world.py WorldTask
```
