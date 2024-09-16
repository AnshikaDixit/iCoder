from django.shortcuts import render

# Create your views here.
def blogHome(request):
    return render(request, "blog/blog_home.html")

def blogPost(request, slug):
     return render(request, "blog/blog_post.html")