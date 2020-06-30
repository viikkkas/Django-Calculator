from django.shortcuts import render

# Create your views here.
def options(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')
    
def sub(request):
    return render(request, 'sub.html')

def mul(request):
    return render(request, 'mul.html')

def div(request):
    return render(request, 'div.html')

def nuts(request):
    return render(request, 'nuts.html')

def calsub(request):
    res = int(request.GET['one']) - int(request.GET['two'])
    return render(request, 'result.html', {'result':res})


def caladd(request):
    res = int(request.GET['num1']) + int(request.GET['num2'])
    return render(request, 'result.html', {'result':res})


def calmul(request):
    res = int(request.GET['num1']) * int(request.GET['num2'])
    return render(request, 'result.html', {'result':res})

def caldiv(request):
    res = int(request.GET['num1']) / int(request.GET['num2'])
    return render(request, 'result.html', {'result':res})

def calnuts(request):
    return render(request, 'error.html')