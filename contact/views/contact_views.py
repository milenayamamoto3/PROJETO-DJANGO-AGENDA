from django.shortcuts import render
from contact.models import Contact

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[0:20]
    
    # print(contacts.query) #consulta SQL na tabela

    context = {
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        context
    )