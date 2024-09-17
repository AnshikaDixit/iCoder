from django.shortcuts import render

from blog.models import Post

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request, "blog/blog_home.html", context)

def blogPost(request, slug):
     post = Post.objects.filter(slug=slug).first()
     context = {'post' : post }
     return render(request, "blog/blog_post.html", context)