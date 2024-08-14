from django.shortcuts import render
from django.http import *
from .models import Author
# Create your views here.
def Authorss(request,authors):
   id_name=Author.objects.get(id=authors)
   return render(request,'authors/author_id.html',{
       'auth':id_name
   })
def slug(request,slug_name):
    slug_form=Author.objects.get(slug=slug_name)
    return render(request,'authors/author_id.html',{
        'slug':slug_form
    })
def index(request):
    print(Author.objects.all())
    return render(request,"authors/authors.html",{"author":Author.objects.all()})