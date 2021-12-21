from django.shortcuts import render
from subprocess import run, PIPE
import sys


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def compute(request):
    rnd = request.POST.get('rnd')
    admn = request.POST.get('admn')
    mks = request.POST.get('mks')
    loc = request.POST.get('loc')
    indv = request.POST.get('indv')

    
    out = run([sys.executable, 'D:\\College notes\\Sem_5\\BDA\PBL\\Django\\bdaproject\\demo.py', rnd, admn, mks, loc, indv], shell=False, stdout=PIPE)
    print(out)
    return render(request, 'home.html', {'predicted':out.stdout.decode("utf-8")})