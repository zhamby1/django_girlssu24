from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
#create post_list function, takes a request as a argument/parameter
def post_list(request):
    #create variable called posts that grabs all objects that have a published date less than or equal to (lte) the current time.  order it by published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #returns the request, the HTML file you want to send, and any data you want to pass
    return render(request,'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})