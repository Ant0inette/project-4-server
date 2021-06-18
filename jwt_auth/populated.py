from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from dreams.serializers import DreamSerializer
from dreams.serializers import CommentSerializer

User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    favorites = DreamSerializer(many=True)
    comments = CommentSerializer(many=True)
    created_Dreams = DreamSerializer(many=True)

class Meta:
    model = User
    fields = (
        'id',
        'username',
        'profile_image',
        'email',
        'favorites',
        'comments',
        'created_dreams'
    )    
