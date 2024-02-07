from django.shortcuts import render
from django.http import HttpResponse
from alexandria_app.forms import FileForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

# def serve_index(request):
#    return render(request, "index.html")

def serve_index(request):
    print(f"request {request}")
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, "index.html", context)

    context = {'form': FileForm()}
    return render(request, "index.html", context)



