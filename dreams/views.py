from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Dream, Comment
from .serializers import DreamSerializer, PopulatedDreamSerializer, CommentSerializer
# Create your views here.

class DreamListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        dreams = Dream.objects.all()
        serialized_dreams = PopulatedDreamSerializer(dreams, many=True)
        return Response(serialized_dreams.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['author'] = request.user.id
        new_dream = DreamSerializer(data=request.data)
        if new_dream.is_valid():
            new_dream.save()
            return Response(new_dream.data, status=status.HTTP_201_CREATED)
        return Response(new_dream.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY) 

class DreamDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_dream(self,pk):
        try :
            return Dream.objects.get(pk=pk)
        except Dream.DoesNotExist:
            raise NotFound() 

    def get(self, _request, pk):
        dream = self.get_dream(pk=pk)
        serialized_dream = PopulatedDreamSerializer(dream)  
        return Response(serialized_dream.data, status=status.HTTP_200_OK) 

    def put(self, request, pk ):
        dream_to_update = self.get_dream(pk=pk)
        if dream_to_update.author != request.user:
            raise PermissionDenied()
        request.data['author'] = request.user.id
        updated_dream = DreamSerializer(dream_to_update, data=request.data)
        if updated_dream.is_valid():
            updated_dream.save() 
            return Response(updated_dream.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_dream.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY) 

    def delete(self, request, pk):
        dream_to_delete = self.det_dream(pk=pk)
        if dream_to_delete.author != request.user:
            raise PermissionDenied()
        dream_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            

class DreamFavoriteView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):
        try:
            dream_to_favorite = Dream.objects.get(pk=pk)
            if request.user in dream_to_favorite.favorited_by.all():
                dream_to_favorite.favorited_by.remove(request.user.id)
            else:
                dream_to_favorite.favorited_by.add(request.user.id)
            dream_to_favorite.save()
            serialized_dream = PopulatedDreamSerializer(dream_to_favorite)
            return Response(serialized_dream.data, status=status.HTTP_202_ACCEPTED)
        except Dream.DoesNotExist:
            raise NotFound()  



class CommentListView(APIView):
    permission_classes = (IsAuthenticated, ) 
    def post(self, request, drm_pk):
        request.data['dream'] = drm_pk
        request.data['author'] = request.user.id
        serialized_comment = CommentSerializer(data=request.data)
        if serialized_comment.is_valid():
            serialized_comment.save()
            return Response(serialized_comment.data, status=status.HTTP_201_CREATED)
        return Response(serialized_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY) 

class CommentDetailView(APIView):

    def delete(self, request, _drm_pk, comment_pk):
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            if comment_to_delete.author != request.user:
                raise PermissionDenied() 
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound()                                       


# class FollowUnfollowView(APIView):
#         permission_classes = [IsAuthenticated]
        
#         def current_profile(self):
#             try:
#                 return Profile.objects.get(user = self.request.user)
#             except Profile.DoesNotExist:
#                 raise NotFound()
            
#         def other_profile(self,pk):
#             try:
#                 return Profile.objects.get(id = pk)
#             except Profile.DoesNotExist:
#                 raise NotFound()
        
#         def post(self, request,format=None):    
            
#             pk = request.data.get('id')              # Here pk is other user 
#             req_type = request.data.get('type')        
            
#             current_profile = self.current_profile()
#             other_profile = self.other_profile(pk)
            
            
#             if req_type == 'follow':
#                 if other_profile.private_account:
#                     other_profile.panding_request.add(current_profile)
#                     return Response({"Requested" : "Follow request has been send!!"},status=status.HTTP_200_OK)
#                 else:
#                     if other_profile.blocked_user.filter(id = current_profile.id).exists():
#                         return Response({"Following Fail" : "You, have been blocked !!"},status=status.HTTP_400_BAD_REQUEST)
#                     current_profile.following.add(other_profile)
#                     other_profile.followers.add(current_profile)
#                     return Response({"Following" : "Following success!!"},status=status.HTTP_200_OK) 
            
#             elif req_type == 'accept':
#                 current_profile.followers.add(other_profile)
#                 other_profile.following.add(current_profile)
#                 current_profile.pending_request.remove(other_profile)
#                 return Response({"Accepted" : "Follow request successfuly accepted!!"},status=status.HTTP_200_OK)
            
#             elif req_type == 'decline':
#                 current_profile.pending_request.remove(other_profile)
#                 return Response({"Decline" : "Follow request successfully declined!!"},status=status.HTTP_200_OK)
            
#             elif req_type == 'unfollow':
#                 current_profile.following.remove(other_profile)
#                 other_profile.followers.remove(current_profile)
#                 return Response({"Unfollow" : "Unfollow success!!"},status=status.HTTP_200_OK)
                

#     # fetch followers data ,following detail and blocked user,pending request,sended request.. 
    
#         def patch(self, request,format=None):
        
#             req_type = request.data.get('type')
        
#             if req_type == 'follow_detail':
#                 serializer = FollowerSerializer(self.current_profile())
#                 return Response({"data" : serializer.data},status=status.HTTP_200_OK)
        
#             elif req_type == 'block_pending':
#                 serializer = BlockPendinSerializer(self.current_profile())
#                 pf = list(Profile.objects.filter(panding_request = self.current_profile().id).values('id','user__username','profile_pic','overall_pr'))
#                 return Response({"data" : serializer.data,"Sended Request" :pf},status=status.HTTP_200_OK)

#     # BLOCK O" CLOCK

#         def put(self, request,format=None):
#             pk = request.data.get('id')              # Here pk = person to be blocked's ID
#             req_type = request.data.get('type')
        
#             if req_type == 'block':
#                 self.current_profile().blocked_user.add(self.other_profile(pk))
#                 return Response({"Blocked" : "This user blocked successfuly"},status=status.HTTP_200_OK)
#             elif req_type == 'unblock':
#                 self.current_profile().blocked_user.remove(self.other_profile(pk))
#                 return Response({"Unblocked" : "This user unblocked successfuly"},status=status.HTTP_200_OK)
