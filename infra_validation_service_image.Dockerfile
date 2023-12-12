# Dockerfile

# Use a imagem base do Python
FROM python:3.9

# Copie o código Python para o contêiner
COPY infra_validation_service.py /app/infra_validation_service.py

# Defina o diretório de trabalho como /app
WORKDIR /app

# Instale as dependências, se houver
# Se o seu script precisar de dependências adicionais, adicione aqui com o requirements.txt
# RUN pip install -r requirements.txt

# Comando a ser executado quando o contêiner for iniciado
CMD ["python", "infra_validation_service.py"]
