from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'pages/blog_form.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.all()
    if not blogs:
        message = "No hay páginas aún"
        return render(request, 'blogs/blog_list.html', {'message': message})
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def blog_detail(request, pageId):
    blog = get_object_or_404(Blog, id=pageId)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

