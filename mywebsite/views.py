

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from posts.models import BlogPost

#---১. হোম পেজ (লগইন থাকা ইউজাররাই শুধু পোস্ট করতে পারবে এবং ছবির ফাইলও রিসিভ হবে) ---
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title_data = request.POST.get('title')
            content_data = request.POST.get('content')

            # ছবির ফাইল রিছিভ করার বিশেষ ড্যাঙ্গো কোড
            image_data = request.FILES.get('image_file') if request.FILES else None

            # ডাটাবেজে লেখা এবং ছবি একসাথে সেভ করা
            BlogPost.objects.create(title=title_data, content=content_data, image=image_data)
        return redirect('home')

    # সাধারণ অবস্থায় ডাটাবেজের সব পোস্ট তুলে আনা
    all_posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': all_posts})

#---২. সাইন আপ বা নতুন অ্যাকাউন্ট তৈরির ভিউ ---

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # ডাটাবেজে নতুন ইউজার সেভ হলো
            return redirect('login') # সফল হলে লগইন পেজে নিয়ে যাবে
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#---৩. সাইন ইন বা লগইন ভিউ ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) # সেশন চালু হলো
            return redirect('home') # সফল হলে হোম পেজে নিয়ে যাবে
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#---৪. লগআউট ভিউ ---
def logout_view(request):
    logout(request)
    return redirect('home')

#---৫. পোস্ট ডিলিট করার অ্যাডভান্স ভিউ ---
def delete_post(request, pk):
    if request.user.is_authenticated: # শুধুমাত্র লগইন থাকা ইউজাররাই ডিলিট করতে পারবে
        post = BlogPost.objects.get(id=pk)
        post.delete() # ডাটাবেজ থেকে চিরতরে মুছে যাবে
    return redirect('home')

#---৬. পোস্ট এডিট বা পরিবর্তন করার অ্যাডভান্সড ভিউ ---
def edit_post(request, pk):
    post = BlogPost.objects.get(id=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')

            # যদি নতুন কোনো ছবি আপলোড করা হয়, তবেই শুধু ছবি পরিবর্তন হবে
            if request.FILES.get('image_file'):
                post.image = request.FILES.get('image_file')

            post.save() # ডাটাবেজে আপডেট ডেটা সেভ হলো
            return redirect('home')

    return render(request, 'edit.html', {'post': post})