from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def create(requset):
    if requset.method == 'GET':
        form = MovieForm
    else:
        form = MovieForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    
    context = {'form': form}
    return render(requset, 'movies/create.html', context)
