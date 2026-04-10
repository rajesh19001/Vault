from django.shortcuts import render
from .models import UserMedia

def home(request):
    query = request.GET.get('q') # This catches what you type in the box
    results = None
    if query:
        results = UserMedia.objects.filter(name_code__iexact=query)
    return render(request, 'home.html', {'results': results, 'query': query})