from django.db import models
from RoomsList.models import Rooms


# class Rooms(models.Model):
#     increment = models.AutoField(primary_key = True, db_index=True)
#     num_room = models.SmallIntegerField()
#     num_build = models.SmallIntegerField()
#     count_places = models.SmallIntegerField()
#     count_resident = models.SmallIntegerField()


class Students(models.Model):
    id_student = models.CharField(primary_key=True, db_index=True, max_length=100)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    num_year = models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])
    department = models.CharField(max_length=200)
    specialty = models.CharField(max_length=300)
    num_room = models.ForeignKey(Rooms, on_delete=models.PROTECT, default=1)
