from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406354152',
        'name': 'Felesia Junelus',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)