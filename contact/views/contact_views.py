from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import get_object_or_404, render

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

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )