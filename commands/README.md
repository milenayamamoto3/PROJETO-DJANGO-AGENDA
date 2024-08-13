Iniciar o projeto Django

*Crie a configurações do seu project (.vscode->settings.json)
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

Criando app contact e pastas de templates e static

python manage.py startapp contact
*Coloque o nome do seu app no (project->settings->INSTALLED_APPS)
*Crie a pasta base para templates e pra static
*base_templates->global->base.html
*base_static->global->css->style.css
*Insira "base_templates" no(project->settings->TEMPLATES->DIR->"BASE_DIR / 'base_templates'")
*Insira a "base_static" no(project->settings->"STATICFILES_DIRS = (BASE_DIR / 'base_static',)")
*Crie uma pasta "templates/contact" para seu app
*Crie nesta pasta "index.html"
*Crie um "urls.py" dentro do app



