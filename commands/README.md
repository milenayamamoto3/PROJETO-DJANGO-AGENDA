Iniciar o projeto Django

python -m venv "venv"
venv\Scripts\activate
python -m pip install django
django-admin startproject "nome do projeto" .
python manage.py runserver

Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
git push origin main -u