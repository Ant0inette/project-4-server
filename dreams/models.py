from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import  MinValueValidator, MaxValueValidator
# from django.utils import timezone

class Dream(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=6000)
    caption = models.CharField(max_length=60)
    image_url = models.CharField(max_length=800)
    coherence_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=0
    )

    favorited_by = models.ManyToManyField(
    'jwt_auth.User',
    related_name='favorites',
    blank=True
    )
    author = models.ForeignKey(
        'jwt_auth.User',
        related_name='created_dreams',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    dream = models.ForeignKey(
        Dream,
        related_name='comments',
        on_delete=models.CASCADE
        )
    
    author = models.ForeignKey(
        'jwt_auth.User',
        related_name='comments',
        on_delete=CASCADE
    )

    def __str__(self): 
        return f'Comment {self.id} on {self.dream}'


# class Type(models.model):

