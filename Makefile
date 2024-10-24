install:
	# Instalar dependências
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	# Formatar o código com black
	black app

lint:
	# Analisar o código com flake8
	flake8 --extend-ignore E501 app

test:
	# Rodar testes com pytest
	pytest

deploy:
	# Comandos para deploy (substitua conforme necessário)
	echo "Deploying application..."

all: install format lint test deploy
