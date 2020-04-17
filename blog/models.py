from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, default='Default Blog title')
    pub_date = models.DateTimeField(auto_now_add=True)
    content = RichTextField()

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title