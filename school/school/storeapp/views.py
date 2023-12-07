from django.shortcuts import render

# Create your views here.
from .models import School
from .models import Faculity


# Create your views here.
def home(request):
    obj = School.objects.all()
    obj1 = Faculity.objects.all()
    return render(request,"index.html",{'res':obj,'result':obj1})

