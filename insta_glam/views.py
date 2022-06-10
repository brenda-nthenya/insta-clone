from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    comments = Comment.objects.all()
    user_profile = Profile.objects.get(user=user)
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    context = {
        "comments":comments,
        "posts": posts,
        "profiles": profiles,
        # "user_profile":user_profile
    }

    return render(request, 'index.html', context)

@login_required
def add_comment(request):
    current_user = request.user

    if request.method == 'POST':
        c_form = CommentForm(request.POST, instance=request.user)
    else:
        c_form = CommentForm(instance=request.user)

    if c_form.is_valid():
        # print(c_form)

        c_form.save()

        messages.success(
            request, f'comment created successfully')
        return redirect('index')
    context = {
        'c_form': c_form
    }
    return render(request, 'insta_glam/comment_form.html', context)

@login_required
def profile_info(request):
    current_user = request.user
    if request.method == 'POST':
        p_form = ProfileEditForm(
            request.POST, request.FILES,instance=request.user.profile
        )
    else:
        p_form = ProfileEditForm(instance=request.user.profile)

    if  p_form.is_valid():
        p_form.save()

        messages.success(
            request, f'Your profile has been updated successfully')
        return redirect('profile_edit')
    context = {
        'p_form': p_form
    }
    return render(request, 'profile/profile.html', context)



class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['author', 'post', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def profile_edit(request):
    current_user = request.user

    if request.method == 'POST':
        p_form = ProfileEditForm(
            request.POST, request.FILES,instance=request.user.profile
        )
    else:
        p_form = ProfileEditForm(instance=request.user.profile)

    if  p_form.is_valid():
        p_form.save()

        messages.success(
            request, f'Your profile has been updated successfully')
        return redirect('profile_edit')
    context = {
        'p_form': p_form
    }
    return render(request, 'profile/profile.html', context)

@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search_results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search_results.html', {'message': message})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            messages.success(f'account for {username} created successfully')
            print(form.cleaned_data)
            profile = Profile.objects.create(user=form.cleaned_data)
            profile.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'django_registration/registration_form.html', {form:form})