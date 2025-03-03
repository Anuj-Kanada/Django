from django.shortcuts import render
from datetime import datetime

# Create your views here.
# def learn_django(request):
#     # example-1 : Variable
#     return render(request,'app/django.html', context={'name' : 'Django'})

# def learn_django(request):
#     name = 'Django'
#     duration = '4 month'
#     seats = 10
#     courseDetails = {'nm' : name, 'du':duration, 'st':seats}
#     return render(request,'app/django.html', courseDetails)

#filters
# def learn_django(request):
#     return render(request,'app/django.html', context={'name' : 'Django', 'description' : 'Django is awesome web framework.'})

# def learn_django(request):
#     d = datetime.now()
#     return render(request,'app/django.html', context={'dt':d})

#
# def learn_django(request):
#     return render(request,'app/django.html', context={'p1': 56.2325, 'p2':56.000, 'p3':56.37000 })

# # If TAG 5.1
# def learn_django(request):
#     return render(request,'app/django.html', context={'nm' : True})


# If TAG 5.2
# def learn_django(request):
#     return render(request,'app/django.html', context={'nm' : 'Django', 'st': 5})

# # if else
# def learn_django(request):
#     return render(request,'app/django.html', context={'nm' : 'Django', 'st': 5})

# # For Loop
# def learn_django(request):
#     students = {'names':['Anuj','Raj', 'Parth', 'Vasu']}
#     return render(request,'app/django.html', context=students)


# # more data
# def learn_django(request):
#     stu = { 'stu1': {'name': 'Anuj', 'roll':101},
#             'stu2': {'name': 'Vasu', 'roll':102},
#             'stu3': {'name': 'KB', 'roll':103},
#             'stu4': {'name': 'UV', 'roll':104},
#         }
    
#     students = {'student':stu}
#     return render(request,'app/django.html', context=students)

# # more data-2
# def learn_django(request):
#     student = {'name': 'Anuj', 'roll':101 }
#     return render(request,'app/django.html', context={'student':student})


# more data-3
def learn_django(request):
    stu = { 'stu1': {'name': 'Anuj', 'roll':101},
            'stu2': {'name': 'Vasu', 'roll':102},
            'stu3': {'name': 'KB', 'roll':103},
            'stu4': {'name': 'UV', 'roll':104},
        }
    
    students = {'student':stu}
    return render(request,'app/django.html', context=students)