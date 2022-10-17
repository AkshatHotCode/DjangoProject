from django.db import models

# Create your models here.


class Openings(models.Model):
    OpeningTitle = models.CharField(max_length=100)
    Status = models.CharField(max_length=50)
    Pipelined = models.IntegerField(default=0)
    PublishedSites = models.CharField(max_length=50)
    PrimaryRecruiter = models.CharField(max_length=50)
    Priority = models.IntegerField(default=0)
    TotalOpening = models.IntegerField(default=0)
    PostDate = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.OpeningTitle, self.Status, self.Pipelined)


