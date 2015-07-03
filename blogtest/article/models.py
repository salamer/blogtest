from django.db import models
from pagedown.widgets import AdminPagedownWidget

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    data_time=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    editor=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title
        
        
class Comment(models.Model):
    commentator=models.CharField(max_length=100)
    comment=models.TextField(max_length=200)
    data_time=models.DateTimeField(auto_now_add=True)
    link=models.ForeignKey(Article)
    
    def __uniode__(self):
        return self.commentator
        





