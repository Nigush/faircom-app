from django.shortcuts import render

def post_list(request):
    return render(request, 'faircom/post_list.html', {})
