from django.shortcuts import render

# Create your views here.
def father(request):
    return render(request,'father.html')

def mother(request):
    return render(request,'mother.html')
    