from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Dream, Comment
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = '__all__'

class PopulatedCommentSerializer(CommentSerializer):
    author = UserSerializer() 


class PopulatedDreamSerializer(DreamSerializer):
    comments = PopulatedCommentSerializer(many=True)
    favorited_by = UserSerializer(many=True)
    author = UserSerializer()                          