setup:
	python3 -m venv venv


activate-venv:
	source venv/bin/activate

install:
	pip install --upgrade pip
	pip install -r requirements.txt

activate-install:
	source venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt