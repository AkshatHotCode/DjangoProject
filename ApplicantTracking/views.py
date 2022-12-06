from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Openings, Candidates, Pipeline, Placements, Account
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "ApplicantTracking/index.html")


#Signup--> Registering new Users in the database
def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username', False)
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some another username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "email already exist!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password didn't match")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name

        myuser.save()

        # messages.success(request, "Your account has been successfully created")

        return redirect('signin')

    return render(request, "ApplicantTracking/signup.html")


#SignIn --> User signin, authentication form django admin database.
def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # name = user.name
            return render(request, "ApplicantTracking/dashboard.html")

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request, "ApplicantTracking/signin.html")


#Signout request
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')


#Database calling from the django-admin for opening data
def opening(request):
    op = Openings.objects.all()
    context = {
        'op': op
    }
    print(context)
    return render(request, 'ApplicantTracking/openings.html', context)


#Database calling from the django-admin for candidates data
def candidates(request):
    can = Candidates.objects.all()
    context = {
        'can': can
    }
    print(context)
    return render(request, 'ApplicantTracking/candidates.html', context)


#Database calling from the django-admin for pipeline data
def pipeline(request):
    pipe = Pipeline.objects.all()
    context = {
        'pipe': pipe
    }
    print(context)
    return render(request, 'ApplicantTracking/pipeline.html', context)


#Database calling from the django-admin for placements data
def placement(request):
    place = Placements.objects.all()
    context = {
        'place': place
    }
    print(context)
    return render(request, 'ApplicantTracking/placement.html', context)


#Database calling from the django-admin for accounts data
def account(request):
    acc = Account.objects.all()
    context = {
        'acc': acc
    }
    print(context)
    return render(request, 'ApplicantTracking/account.html', context)


#Data calling form database calling.
def dashboard(request):
    topi = Openings.objects.all()
    date = datetime.now()
    y = date.strftime('%d-%m-%Y')
    context = {
        'top': topi,
        'date': y
    }
    print(context)
    return render(request, 'ApplicantTracking/dashboard.html', context)

def addopenings(request):
    if request.method == "POST":
        opetitle = request.POST['opetitle']
        status = request.POST['status']
        pipelined = int(request.POST['pipelined'])
        site = request.POST['site']
        rec = request.POST['rec']
        priority = int(request.POST['priority'])
        totope = int(request.POST['totope'])
        postdate = request.POST['postdate']
        new_ope = Openings(OpeningTitle=opetitle, Status=status, Pipelined=pipelined, PublishedSites=site, PrimaryRecruiter=rec, Priority=priority,
                 TotalOpening=totope, PostDate=postdate)
        new_ope.save()
        # return HttpResponse("New Opening Added")
        return render(request, 'ApplicantTracking/success.html')

    elif request.method == "GET":
        return render(request, 'ApplicantTracking/addopenings.html')
    else:
        return HttpResponse("An Error Happened!")

def addcandidates(request):
    if request.method == "POST":
        candname = request.POST['candname']
        score = request.POST['score']
        sourcedby = request.POST['sourcedby']
        email = request.POST['email']
        status = request.POST['status']
        jtitle = request.POST['jtitle']
        sofrom = request.POST['sofrom']
        monumb = request.POST['monumb']
        if Candidates.objects.filter(Email=email):
            # return HttpResponse("Email already exist! Invalid")
            return render(request, 'ApplicantTracking/email_already_exist.html')
        if Candidates.objects.filter(Name=candname):
            # return HttpResponse("Name already exist! Invalid")
            return render(request, 'ApplicantTracking/name_already_exist.html')
        new_can = Candidates(Name=candname, Score=score, SourcedBy=sourcedby, Email=email,
                             Status=status, JobTitle=jtitle, SourcedFrom=sofrom, Mobile=monumb)
        new_can.save()
        # return HttpResponse("New Candidate Added")
        return render(request, 'ApplicantTracking/success.html')
    elif request.method == "GET":
        return render(request, 'ApplicantTracking/addcandidates.html')
    else:
        return HttpResponse("An Error Happened!")

def addpipeline(request):
    can = Candidates.objects.all()
    ope = Openings.objects.all()
    context = {
        'can': can,
        'ope': ope
    }
    if request.method == "POST":
        candname = request.POST['candname']
        subdate = request.POST['subdate']
        status = request.POST['status']
        optit = request.POST['optit']
        opid = request.POST['opid']
        accname = request.POST['accname']
        oppodate = request.POST['oppodate']
        opstat = request.POST['opstat']
        sofrom = request.POST['sofrom']
        mob = request.POST['mob']
        quali = request.POST['quali']
        mail = request.POST['mail']
        new_pipe = Pipeline(CandidateName=candname, SubmittedDate=subdate, Status=status, OpeningTitle=optit, OpeningID=opid,
                            AccountName=accname, OpeningPostDate=oppodate, OpeningStatus=opstat,
                            SourcedFrom=sofrom, Mobile=mob, Qualification=quali, Email=mail)
        new_pipe.save()
        # return HttpResponse("New Pipeline Added", context)
        return render(request, 'ApplicantTracking/success.html')
    elif request.method == "GET":
        return render(request, 'ApplicantTracking/addpipeline.html', context)
    else:
        return HttpResponse("An Error Happened!", context)

def addplacement(request):
    can = Candidates.objects.all()
    ope = Openings.objects.all()
    context = {
        'can': can,
        'ope': ope
    }
    if request.method == "POST":
        plname = request.POST['plname']
        brate = request.POST['brate']
        candname = request.POST['candname']
        optit = request.POST['optit']
        ecl = request.POST['ecl']
        proenddate = request.POST['proenddate']
        prostdate = request.POST['prostdate']
        sofrom = request.POST['sofrom']
        nmarg = request.POST['nmarg']
        smarg = request.POST['smarg']
        opid = request.POST['opid']
        stat = request.POST['stat']
        plaby = request.POST['plaby']
        plaon = request.POST['plaon']
        new_place = Placements(PlacementName=plname, BillRate=brate, CandidateName=candname, OpeningTitle=optit,
                               EndClient=ecl, ProjectEndDate=proenddate, ProjectStartDate=prostdate, SourcedFrom=sofrom,
                               NetMargin=nmarg, SalesMargin=smarg, OpeningID=opid, Status=stat, PlacedBy=plaby,
                               PlacedOn=plaon)
        new_place.save()
        # return HttpResponse("New Pipeline Added", context)
        return render(request, 'ApplicantTracking/success.html')
    elif request.method == "GET":
        return render(request, 'ApplicantTracking/addplacement.html', context)
    else:
        return HttpResponse("An Error Happened!", context)

def addaccount(request):
    if request.method == "POST":
        name = request.POST['name']
        accown = request.POST['accown']
        accod = request.POST['accod']
        cate = request.POST['cate']
        acce = request.POST['acce']
        stat = request.POST['stat']
        pho = request.POST['pho']
        state = request.POST['state']
        new_acc = Account(Name=name, AccountOwner=accown, AccountCode=accod,
                          Category=cate, Access=acce, Status=stat,
                          Phone=pho, State=state)
        new_acc.save()
        # return HttpResponse("New Pipeline Added")
        return render(request, 'ApplicantTracking/success.html')
    elif request.method == "GET":
        return render(request, 'ApplicantTracking/addaccount.html')
    else:
        return HttpResponse("An Error Happened!")