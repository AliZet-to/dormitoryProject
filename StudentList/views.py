from django.shortcuts import render
# from StudentList.models import Students


def Show_students(request):
    name = 'Sasha'
    print('hiiii')
    return render(request, 'StudentList/index.html', context={'students': name})


# Create your views here.
