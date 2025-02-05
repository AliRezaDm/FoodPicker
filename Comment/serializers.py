from rest_framework import serializers
from models import Comment



class CommentSerializer(serializers.ModelSerializer):

    # to show nested replies from the get_replies method 
    replies = serializers.SerializerMethodField()
    # bringing up user makes read only so i can't be modified
    user = serializers.ReadOnlyField(source='user.name')
    #bringing related recipe to the comment
    recipe = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Comment
        # replies show the replies the comment has
        fields = ['id', 'user', 'recipe', 'title', 'content', 'created_at', 'reply', 'is_reply', 'replies']
        read_only_fields = ['created_at', 'status']
    # using the related_name in the model to bring up all the reply the comment has
    def get_replies(self, obj):
        if obj.comment_reply.exists():
            return CommentSerializer(obj.comment_reply.all(), many=True).data
        return []
    # to get the comment user 
    def create(self, validated_data):
        # checks if the user exists
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user

        return super().create(validated_data)

        