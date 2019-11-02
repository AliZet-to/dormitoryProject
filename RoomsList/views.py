from django.shortcuts import render
from RoomsList.models import Rooms


def Show_room(request):
    name = 'Sasha'
    obj01 = Rooms.objects.all()
    # return render(request, 'RoomsList/index_old.html', context={'num_room': obj01.num_room,
    #                                                         'num_build': obj01.num_build,
    #                                                         'count_places': obj01.count_places,
    #                                                         'count_resident': obj01.count_resident})
    # return render(request, 'RoomsList/index.html', context={'rooms': obj01})
    return render(request, 'base.html', context={'rooms': obj01})


# Create your views here.
