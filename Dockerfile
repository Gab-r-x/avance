# Usar a imagem oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Expor a porta que a aplicação Flask usará
EXPOSE 5000:5000

# Definir a variável de ambiente para rodar o Flask
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True
ENV FLASK_APP=app.app:create_app

# Comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
