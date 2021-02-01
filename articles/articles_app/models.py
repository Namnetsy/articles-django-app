from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = RichTextField(config_name='awesome_ckeditor')
    
    def __str__(self):
        return self.title
