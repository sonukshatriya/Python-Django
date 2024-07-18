from django.shortcuts import render, redirect
from .models import wedlock

# Create your views here.

def index(request):
    return render(request, 'index.html')


def insertdata(request):
    if request.method == "POST":
        uemail = request.POST.get("email address")
        upassword = request.POST.get("password")
        uprofileseekingfor = request.POST.get("userprofileseekingfor")
        ufirstname = request.POST.get("userfname")
        ulastname = request.POST.get("userlastname")
        ugender = request.POST.get("gender")
        ureligion = request.POST.get("userreligion")
        umothertongue = request.POST.get("usermothertongue")
        insertdata = wedlock(email=uemail,password=upassword,profile_seeking_for=uprofileseekingfor,first_name=ufirstname,last_name=ulastname,gender=ugender,religion=ureligion,mother_tongue=umothertongue,)
        insertdata.save()
    return render(request, 'index.html')


def manageproducts(request):
    fetch = people.objects.all()
    return render(request, 'manageproducts.html', {'people': fetch})


def output(request):
    data = wedlock.objects.all()
    return render(request, 'output.html', {'formate': data})




