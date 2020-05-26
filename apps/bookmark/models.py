from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
