install:
	virtualenv venv
	. venv/bin/activate; pip install -r requirements.txt

start:
	. venv/bin/activate; python run.py &

stop:
	ps -ef | grep "run.py" | grep -v grep | awk '{print $$2}' | xargs kill

test:
	. venv/bin/activate; python tests.py
