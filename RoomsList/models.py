from django.db import models


class Rooms(models.Model):
    increment = models.AutoField(primary_key=True, db_index=True)
    num_room = models.SmallIntegerField()
    num_build = models.SmallIntegerField()
    count_places = models.SmallIntegerField()
    count_resident = models.SmallIntegerField()
