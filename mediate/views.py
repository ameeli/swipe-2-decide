from django.shortcuts import render

# Create mediate/templates/mediate/index.html and have React try to render
# onto the root of that page?


def index(request):
    return render(request, 'mediate/index.html')
