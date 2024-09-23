from django.shortcuts import render

def shop(request):
    return render(request, 'shop.html')

def warenkorb(request):
    return render(request, 'warenkorb.html')

def kasse(request):
    return render(request, 'kasse.html')