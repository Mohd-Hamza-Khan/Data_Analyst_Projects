from django.shortcuts import render
from static.mdl import rf

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def prediction(request):
    if request.method=="POST":
        age=int(request.POST.get('age'))
        sex=int(request.POST.get('sex'))
        bmi=int(request.POST.get('bmi'))
        children=int(request.POST.get('children'))
        smoker=int(request.POST.get('smoker'))
        region=int(request.POST.get('region'))
        pred = round(rf.predict([[age,sex,bmi,children,smoker,region]])[0])
        
        output = {
            'output':pred
        }
        return render(request,'prediction.html',output)
        
    return render(request, 'prediction.html')


def contact(request):
    return render(request, 'contact.html')