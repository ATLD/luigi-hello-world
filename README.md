# Luigi Example

This is just a simple 'Hello World' example to demonstrate the use of Luigi.

It will create a file that says "Hello", another that says "World", and concatenate the contents of those files into a third that says "Hello World". 

Usage:

```
pip install venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
luigid --background --port=8082 --logdir=logs
python hello_world.py HelloWorldTask --id=some_id
```
