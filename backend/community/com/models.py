from django.db import models

# Create your models here.


class Community(models.Model):

    parties={
        "ANC":"African National Congress",
        "IFP":"Inkatha Freedom Party",
        "EFF":"Economic Freedom Fighter",
    }

    person_name=models.CharField(max_length=50)
    person_surname=models.CharField(max_length=50)
    person_area=models.IntegerField()
    person_party=models.CharField(max_length=5,choices=parties)
