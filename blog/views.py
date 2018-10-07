from django.shortcuts import render


def post_list(request):
    print("post list view")
    return render(request, 'blog/post_list.html', {})