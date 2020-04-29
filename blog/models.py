from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, default='Default Blog title')
    description = models.CharField(max_length=200, blank=False, default='default')
    image = models.CharField(max_length=1000, blank=False, default='https://wpdean.com/wp-content/uploads/2015/10/Useful-WordPress-Tools.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    content = RichTextField()

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title