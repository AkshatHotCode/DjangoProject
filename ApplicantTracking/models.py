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

class Candidates(models.Model):
    Name = models.CharField(max_length=50)
    Score = models.IntegerField(default=0)
    SourcedBy = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Status = models.CharField(max_length=50)
    JobTitle = models.CharField(max_length=50)
    SourcedFrom = models.CharField(max_length=50)
    Mobile = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s" %(self.Name, self.Email, self.Status)

class Pipeline(models.Model):
    CandidateName = models.CharField(max_length=100)
    SubmittedDate = models.DateField()
    Status = models.CharField(max_length=50)
    OpeningTitle = models.CharField(max_length=50)
    OpeningID = models.CharField(max_length=10)
    AccountName = models.CharField(max_length=50)
    OpeningPostDate = models.DateField()
    OpeningStatus = models.CharField(max_length=50)
    SourcedFrom = models.CharField(max_length=50)
    Mobile = models.IntegerField(max_length=15)
    Qualification = models.CharField(max_length=150)
    Email = models.EmailField(max_length=50)

    def __str__(self):
        return "%s %s %s" %(self.CandidateName, self.Status, self.OpeningTitle)

class Placements(models.Model):
    PlacementName = models.CharField(max_length=100)
    BillRate = models.CharField(max_length=25)
    CandidateName = models.CharField(max_length=100)
    OpeningTitle = models.CharField(max_length=100)
    EndClient = models.CharField(max_length=100)
    ProjectEndDate = models.DateField()
    ProjectStartDate = models.DateField()
    SourcedFrom = models.CharField(max_length=50)
    NetMargin = models.CharField(max_length=50)
    SalesMargin = models.CharField(max_length=50)
    OpeningID = models.CharField(max_length=10)
    Status = models.CharField(max_length=50)
    PlacedBy = models.CharField(max_length=50)
    PlacedOn = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s" %(self.CandidateName, self.PlacementName, self.OpeningTitle)