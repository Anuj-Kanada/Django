from django.shortcuts import render

# Create your views here.
def learn_django(req):
    coursename = {'cname':'django 5.1'}
     
    # return render(req,'course/django.html', context= coursename)
    # return render(req,'course/django.html',  {'cname':'django 5.0'})
    return render(req,'course/django.html',  coursename)

def learn_fastapi(req):
    seats = 10
    coursedetails = {
                    'cname':'FAST API', 
                    'version':'6.3.2',
                    'st':seats
                 }
    return render(req, 'course/fastapi.html', coursedetails)