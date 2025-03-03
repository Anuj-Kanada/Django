from django.shortcuts import render

# Create your views here.

def learn_django(req):
    # Example-1: variable
    # return render(req, 'course/django.html', context={'name':'Django', 'version' : '5.1.0'}) 
    # Example-1.2: variable
    name ='Django'
    duration = "4 month"
    seats = 10
    course_details = {'nm':name, 'du':duration, 'st': seats}
    return render(req, 'course/django.html', course_details) 
