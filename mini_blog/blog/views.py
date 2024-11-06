from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, blogs



# Create your views here.
def home(request):
    categories= Category.objects.all()
    featured_post =  blogs.objects.filter(is_featured=True)
    Post = blogs.objects.filter(is_featured=False)
    # print(featured_post)
    context = {
        'categories': categories,
        'featured_post':featured_post,
        'Post': Post
    }
    return render(request,"home.html", context)
