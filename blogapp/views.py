from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.core.mail import send_mail
from .models import Category, Post, Comment, Email
from .forms import CommentForm, EmailForm



# Create your views here.


def welcome(request):
    categories = Category.objects.all()
    former_posts = Post.objects.order_by('created')[:3]
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request, 'blogapp/blog.html', {'posts':posts, 'categories':categories, 'page':page,'former_posts':former_posts } )



def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.all()
    former_posts = Post.objects.order_by('created')[:3]
    comments = post.comments.filter(active=True)
    if request.method=='POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blogapp/blog-single.html', {'post':post,'categories':categories, 'comment_form':comment_form, 'comments':comments , 'former_posts':former_posts})

def category_view(request, name):
    category = get_object_or_404(Category, name=name )
    former_posts = Post.objects.order_by('created')[:3]
    categories = Category.objects.all()
    return render(request, 'blogapp/category.html', {'category':category, 'categories':categories, 'former_posts':former_posts})

def contact_view(request):
    categories = Category.objects.all()
    former_posts = Post.objects.order_by('created')[:3]

    if request.method=="POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'willsphonodiction mail received, reply {} immediately'.format(cd['email_address'])
            send_mail(subject, cd['body'], cd['email_address'], ['akanavaro@gail.com'])

            form.save()
    else:
        form = EmailForm()
    return render(request, 'blogapp/contact.html', {'categories':categories, 'form':form, 'former_posts':former_posts})