from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 256)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        ##after publishing the blog this method will be called
        ##we will have a publish button thats whn this method is gonna get called,coz create date and published date can be different

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)
        #we are gonna have comments, some will be approved whereas some will be non approved.
        # so using this method we are gonna have approved_comments


    def get_absolute_url(self):
        return reverse("post_detail",kwargs = {'pk':self.pk})
        ##after posting the blog where should the website take them
        #it will take them to the post_detail url page for a particular primary key

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name = 'comments',on_delete=models.CASCADE)
    author = models.CharField(max_length = 200)
    #this can be any other author
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
