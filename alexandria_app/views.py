from django.shortcuts import render
from django.http import HttpResponse
from alexandria_app.forms import FileForm
from alexandria_app.forms import File


# returns the rendderd index page.
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


# returns the rendderd list_files page.
def list_files(request):
    files = File.objects.all()
    context = {'files':files}
    return render(request, "list.html", context)
