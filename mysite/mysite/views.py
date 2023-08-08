from django.http import HttpResponse
import datetime

from django.shortcuts import render

def home(request):

    isActive = True
    if request.method == 'POST':
        # check = request.POST['check']
        check  = request.POST.get('check')
        print(check)

        if check is None:
            isActive = False
        else:
            isActive = True


    date = datetime.date.today()
    print('test function is called from view.')
    # return HttpResponse(f"<h1>Hello, world. You're at the Home Page.</h1>\n\
    #                     <h1>{date}</h1>")

    name = 'Anurag Verma'
    listOfProgram = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all numbers from 1 to 100',
    ]
    students = {
        'sName': 'Anurag Verma',
        'scollege':'xyz',
        'sId': 101
    }


    data = {
        'date': date,
        'isActive':isActive,
        'name': name,
        'listOfProgram': listOfProgram,
        'students': students
    }

    return render(request, "home.html", data)

def about(request):
    # return HttpResponse("This is About page\
    #                     <h1>Hi I'M ANURAG VERMA</h1>\
    #                     <h3>Python Developer</h3>")

    return render(request, 'about.html')


def services(request):
    # return HttpResponse("This is Services page\
    #                     <h1>Available Cources</h1>\
    #                     <h2>Python</h2>\
    #                     <h2>Java</h2>\
    #                     <h2>JavaScript</h2>")
    return render(request, 'services.html')
