from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def create_blog(request):
    if not request.user.is_staff:
        return redirect('blog_list')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

# Editar
@login_required
def edit_blog(request, pageId):
    blog = get_object_or_404(Blog, id=pageId)
    if not request.user.is_staff:
        return redirect('blog_list')
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pageId=pageId)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})

# Borrar
@login_required
def delete_blog(request, pageId):
    blog = get_object_or_404(Blog, id=pageId)
    if not request.user.is_staff:
        return redirect('blog_list')
    blog.delete()
    return redirect('blog_list')

