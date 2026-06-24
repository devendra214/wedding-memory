from django.shortcuts import render, redirect
from .forms import MemoryForm
from .models import Memory
from django.db.models import Q
from .models import GallerySettings

def upload_memory(request):

    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/success/')

    else:
        form = MemoryForm()

    return render(request, 'upload.html', {'form': form})


def success(request):
    return render(request, 'success.html')





def gallery(request):

    settings = GallerySettings.objects.first()

    if settings and not settings.is_public:

        if not request.session.get('gallery_access'):

            return redirect('/gallery-login/')

    query = request.GET.get('q')

    if query:
        memories = Memory.objects.filter(
            Q(name__icontains=query) |
            Q(city__icontains=query)
        ).order_by('-id')
    else:
        memories = Memory.objects.all().order_by('-id')

    return render(
        request,
        'gallery.html',
        {
            'memories': memories,
            'query': query
        }
    )

def gallery_login(request):

    settings = GallerySettings.objects.first()

    if request.method == 'POST':

        password = request.POST.get('password')

        if password == settings.password:

            request.session['gallery_access'] = True

            return redirect('/gallery/')

        else:

            return render(
                request,
                'gallery_login.html',
                {'error': 'Wrong Password'}
            )

    return render(request, 'gallery_login.html')