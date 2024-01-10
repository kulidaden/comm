from django.contrib.auth import authenticate, login
from .forms import AuthorRegistrationForm, CommentForm
from .models import Author, Comment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def register_author(request):
    if request.method == 'POST':
        form = AuthorRegistrationForm(request.POST)
        if form.is_valid():

            user = User.objects.create_user(username=form.cleaned_data['name'], password=form.cleaned_data['password'])


            author = Author.objects.create(user=user, name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            author.save()
            login(request, user)
            return redirect('success')
    else:
        form = AuthorRegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            return HttpResponse("Name/Password is not valid")

    return render(request, 'login.html')



def success_view(request):
    comments = Comment.objects.all().order_by("-id")

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            content = form.cleaned_data['content']
            comment_file = request.FILES.get('comment_file')
            parent_comment_id = form.cleaned_data.get('parent_comment_id')

            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                comment = Comment.objects.create(author=author, content=content, comment_file=comment_file, parent_comment=parent_comment)
            else:
                comment = Comment.objects.create(author=author, content=content, comment_file=comment_file)

            comment.save()
            return redirect('success')
    else:
        form = CommentForm()

    return render(request, 'success.html', {'comments': comments, 'form': form})




def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if comment.author.user == request.user:
            form.save()
            return redirect('success')
        else:
            pass

    else:
        form = CommentForm(instance=comment)

    return render(request, 'update.html', {'form': form, 'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        if comment.author.user == request.user:
            comment.delete()
        else:
            pass

    return redirect('success')