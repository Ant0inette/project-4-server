from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.utils import timezone


class Dream(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    characters = models.CharField(max_length=60)
    settings = models.CharField(max_length=60)
    emotions = models.CharField(max_length=60)
    themes = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
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
        return f'{self.title}'


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


# class Profile(models.Model):
#      user = models.OneToOneField(
#          to = User,
#          on_delete=models.CASCADE,
#          related_name='profile')
        
#      followers = models.ManyToManyField(
#          'self',blank=True,
#          related_name='user_followers',
#          symmetrical=False)
#      following = models.ManyToManyField(
#          'self',
#          blank=True,
#          related_name='user_following',
#          symmetrical=False)
#      created_date = models.DateTimeField(auto_now_add=True)
#      pending_request = models.ManyToManyField(
#          'self',
#          blank=True,
#          related_name='pendingRequest',
#          symmetrical=False)
#      blocked_user = models.ManyToManyField(
#          'self',
#          blank=True,
#          related_name='user_blocked',
#          symmetrical=False)        
    
# def __str__(self):
#      return f' {self.user}''


    

