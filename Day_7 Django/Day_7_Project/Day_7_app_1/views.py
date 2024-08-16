from django.shortcuts import render
from django.http import *
from .models import Author
from django.db.models import Avg
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
   auth=Author.objects.all().order_by('First_name')
   author_count=auth.count()
   total_avg=Author.objects.all().aggregate(Avg('rating'))
   return render(request,"authors/authors.html",{
       "author":auth,
       "author_count":author_count,
       "total_avg":total_avg
       })