from django.shortcuts import render

# Create your views here.


def read_json():
    with open('XP\animals\info\info.json' 'r') as f:
    data = json.load(f)
    return data

def family(request, family_id):
    data = read_json()

    return render(request,'family.html',context={})

def animal(request, animal_id):
     data = read_json()

    return render(request,'animal.html',context={})
   