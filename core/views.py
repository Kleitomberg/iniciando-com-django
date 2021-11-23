from django.shortcuts import render

# Create your views here.

##views
def index(request):
    context ={
        'nome':'kleitomberg',
        'title':'tela home'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')