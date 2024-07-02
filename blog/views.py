from django.shortcuts import render

# Create your views here.
#create post_list function, takes a request as a argument/parameter
def post_list(request):
    #returns the request, the HTML file you want to send, and any data you want to pass
    return render(request, 'blog/post_list.html', {})