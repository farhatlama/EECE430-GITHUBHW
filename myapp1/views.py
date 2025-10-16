from django.shortcuts import render

# Create your views here.
# mysite1/myapp1/views.py
# mysite1/myapp1/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Video
from .forms import VideoForm

def menu(request):
    return render(request, "myapp1/menu.html")
   # return render(request, "myapp1/menu.html", {"message": "Hello from Jenkins"}) , delete the one before
def video_list(request):
    q = request.GET.get("q", "")
    qs = Video.objects.all().order_by("-id")
    if q:
        qs = qs.filter(
            Q(movie_title__icontains=q) |
            Q(actor1_name__icontains=q) |
            Q(actor2_name__icontains=q) |
            Q(director_name__icontains=q) |
            Q(movie_id__icontains=q) |
            Q(movie_genre__icontains=q) |
            Q(release_year__icontains=q)  
        )
    return render(request, "myapp1/video_list.html", {"videos": qs, "q": q})

def video_create(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp1:list")
    else:
        form = VideoForm()
    return render(request, "myapp1/video_form.html", {"form": form, "mode": "Add New"})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, "myapp1/video_detail.html", {"video": video})

def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect("myapp1:detail", pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, "myapp1/video_form.html", {"form": form, "mode": "Update"})

def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect("myapp1:list")
    return render(request, "myapp1/video_confirm_delete.html", {"video": video})

