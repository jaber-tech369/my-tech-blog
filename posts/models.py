from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200) # শিরোনামের জন্য সর্বোচ্চ ২০০ অক্ষরের বক্স
    content = models.TextField()             # মূল লেখার জন্য আনলিমিটেড বড় বক্স
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title