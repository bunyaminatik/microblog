from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100, verbose_name='Title')
    content=models.TextField(verbose_name='Content')
    createDate=models.DateTimeField(auto_now_add=True, editable=False)
    def __unicode__(self):
	    return self.title
    class Meta:
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    content=models.TextField(verbose_name='Content')
    createDate=models.DateTimeField(auto_now_add=True, editable=False)
    parentPost = models.ForeignKey(Post)
    def __unicode__(self):
	    return ''
    class Meta:
        verbose_name_plural = 'Comments'
	