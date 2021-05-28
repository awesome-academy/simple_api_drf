from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    