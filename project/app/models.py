from django.db import models
from ckeditor.fields import RichTextField

class Converter(models.Model):
    text = RichTextField(blank=True, null=True)
