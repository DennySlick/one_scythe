from django.shortcuts import render

def balance_calculator(request):
    return render(request, 'calculator/balance_calculator.html', {})
