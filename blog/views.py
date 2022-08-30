from .models import Tutorial

from django.shortcuts import render 



# Create your views here.
def home(request):
    tutorials=Tutorial.objects.all()
    context={'tutorials':tutorials}
    
    return render(request,"blog/home.html",context)

    