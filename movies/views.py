from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def create(requset):
    if requset.method == 'GET':
        form = MovieForm
    else:
        form = MovieForm(requset.POST)
        if form.is_valid():
            form.save(pk=pk)
            return redirect('movies:detail', pk)
    
    context = {'form': form}
    return render(requset, 'movies/create.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'Movie': movie}
    return render(request, 'movies:detail.html', context)
