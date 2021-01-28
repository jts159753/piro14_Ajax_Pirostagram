from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def post_list(request):
  
    return render(request,'instagram/post_list.html')