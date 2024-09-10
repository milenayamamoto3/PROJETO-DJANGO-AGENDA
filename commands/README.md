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

Migrando a base de dados do Django

python manage.py makemigrations  (criar migrations)
python manage.py migrate (apply migrations)

Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword "USERNAME"

Shell interativo do python (terminal vscode) 

(myvenv) PS C:\Users\acerc\OneDrive\Desktop\Aulas_python\PROJETO-DJANGO-AGENDA> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>> quit()

Shell interativo do django (terminal vscode) 

(myvenv) PS C:\Users\acerc\OneDrive\Desktop\Aulas_python\PROJETO-DJANGO-AGENDA> python manage.py shell        
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from contact.models import Contact
>>> Contact
<class 'contact.models.Contact'>
>>> c = Contact(first_name='Gustavo') #criando "em lazy" um contato
>>> c
<Contact: Gustavo >
>>> c.save() #salvando um novo contato no formulário, sem levar em consideração o "blank"
>>> c.last_name = "Moreira"
>>> c.save()
>>> c
<Contact: Gustavo Moreira>
>>> c.delete() #deletou do formulário mas não da memória
(1, {'contact.Contact': 1})
>>> c.save() #criou o novo contato no formulário com o novo id
>>> c = Contact.objects.get(id=2) #pegando UM contato para alterar
>>> c.first_name = 'Helena' #alterando o nome para 'Helena'
>>> c.save()
>>> c.pk #chave primária (id)
2
>>> c = Contact.objects.all() #pegando TODOS os contatos 
>>> c
<QuerySet [<Contact: Milena Vieira>, <Contact: Helena Costa>, <Contact: Gustavo Moreira>]>
>>> for contato in c: contato.first_name
...
'Milena'
'Helena'
'Gustavo'
>>> c = Contact.objects.filter(id=4)
>>> c
<QuerySet [<Contact: Gustavo Moreira>]>
>>> c = Contact.objects.all().filter(id=1)
>>> c
<QuerySet [<Contact: Milena Vieira>]>
>>> c = Contact.objects.all().order_by('-id')
>>> c
<QuerySet [<Contact: Gustavo Moreira>, <Contact: Helena Costa>, <Contact: Milena Vieira>]>
>>> c = Contact.objects.create(first_name="Edu", last_name="Sousa") #criar um contato diretamente no formulário
>>> c
<Contact: Edu Sousa>
>>> quit()

Criando um usuário no shell interativo
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user(username='usuario', password='123') #não lazy
user.is_staff = True #lazy
user.save()
user.delete()
quit()

Ignorando errors:
mypy(error) -> # type: ignore
Flake8(E501) -> # flake8: noqa

Usando faker para criar contatos aleatórios:
python -m pip install faker
python utils/create_contact.py





