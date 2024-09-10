from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245440',
        'name': 'Dinda Dinanti',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)