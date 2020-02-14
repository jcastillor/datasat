from django.db import models

class Satelite2(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    genbank_id = models.CharField(blank=True, null=True, max_length=225)
    name = models.CharField(blank=True, null=True, max_length=225)
    type = models.CharField(blank=True, null=True, max_length=225)
    indice = models.CharField(max_length=225)
    satlength = models.IntegerField(blank=True, null=True)
    numrep = models.IntegerField(blank=True, null=True)
    replength = models.IntegerField(blank=True, null=True)
    seed = models.CharField(max_length=225)
    seq = models.CharField(max_length=225)

    class Meta:
        managed = True
        db_table = 'satellite'
