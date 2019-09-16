from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0
    
    if 'allactivities' not in request.session:
        request.session['allactivities'] = []

    return render(request, "index.html")

def processgold(request):
    print("here is where we decide how much money you earn")
    print(request.POST['place'])
    activity = ""
    if request.POST['place'] == "farm":
        goldearned = random.randint(10,20)
        request.session['totalgold'] += goldearned
        activity = f"went to farm and earned {goldearned}"
        request.session['allactivities'].append(activity)
        print(goldearned)

    if request.POST['place'] == "cave":
        goldearned = random.randint(5,10)
        request.session['totalgold'] += goldearned
        activity = f"went to cave and earned {goldearned}"
        request.session['allactivities'].append(activity)

        print(goldearned)

    if request.POST['place'] == "house":
        goldearned = random.randint(2,5)
        request.session['totalgold'] += goldearned
        activity = f"went to house and earned {goldearned}"
        request.session['allactivities'].append(activity)
        print(goldearned)

    if request.POST['place'] == "casino":
        goldearned = random.randint(-50,50)
        request.session['totalgold'] += goldearned
        if goldearned < 0:
            activity = f"went to casino and lost {goldearned}"
        else:
            activity = f"went to casino and earned {goldearned}"
        request.session['allactivities'].append(activity)
    
    # if goldearned < 0:
    #     request.session['color'] = "red"
    # else:
    #     request.session['color'] = "green"

        print(goldearned)
    
    return redirect("/")

def reset(request):
    request.session['totalgold'] = 0
    request.session['allactivities']= []
    return redirect("/")