from django.contrib import admin
from .models import BlogPost  # আমাদের মডেলটি এখানে আনা হলো

admin.site.register(BlogPost) # অ্যাডমিন প্যানেলে এটি রেজিস্টার করা হলো