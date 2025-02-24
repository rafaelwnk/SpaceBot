from django.shortcuts import render
from chat.scraper import save_satellites
from rag.rag import rag_db
from django.contrib.auth.decorators import user_passes_test

def chat(request):
    return render(request, 'index.html')

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def load_database(request):
    save_satellites()
    return render(request, 'load_database.html') 

@user_passes_test(is_admin)
def build_rag(request):
    rag_db()
    return render(request, 'build_rag.html') 


