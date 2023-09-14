from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Название')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, verbose_name=u'Автор')
    body = models.TextField(verbose_name=u'Текст')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])