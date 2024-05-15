from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request) :
    print("This message generated through views")
    isActive = False
    if request.method == 'POST': 
        check = request.POST.get("check")
        if check is not None:
            isActive = True
        else:
            isActive = False
        print(check)
    
    
    date = datetime.datetime.now()
    name = "Saurabh Giri"
    list_of_programs = [
        "WAP to print odd and even",
        "WAP tp print factorial of n",
        "WAP to reverse the string",
        "WAP to print prime number"
    ]
    student = {
        'student_name' : 'Saurabh',
        'student_college' : 'csc',
        'student_city' : 'Mumbai'
    }
    data = {
        'isActive' : isActive,
        'date' : date,
        'name' : name,
        'list_of_programs' : list_of_programs,
        'student_data' : student
    }

    # return HttpResponse("<h1>Hello message from views test function called</h1>")
    return render(request, "home.html", data) #3rd paramtere is dict type

def about(request):
    date = datetime.datetime.now()
    print("about function called")
    # return HttpResponse("<h1>This is about page</h1>"+str(date))
    return render(request, "about.html", {})

def service(request):
    # return HttpResponse("Hi")
    return render(request, "service.html", {})