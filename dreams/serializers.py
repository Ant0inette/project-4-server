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

# class EachUserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username')
#     class Meta:
#         model = Profile
#         fields = ('id','username','profile_pic')
#         read_only_fields = ('id','username','profile_pic')

# class FollowerSerializer(serializers.ModelSerializer):
#     followers = EachUserSerializer(many=True, read_only= True)
#     following = EachUserSerializer(many=True,read_only=True)
    
#     class Meta:
#         model = Profile
#         fields = ('followers','following')
#         read_only_fields = ('followers','following')

# class BlockPendinSerializer(serializers.ModelSerializer):
#     pending_request = EachUserSerializer(many=True, read_only= True)
#     blocked_user = EachUserSerializer(many=True,read_only=True)

#     class Meta:
#         model = Profile
#         fields = ('pending_request','blocked_user')  
#         read_only_fields = ('pending_request','blocked_user')







                     