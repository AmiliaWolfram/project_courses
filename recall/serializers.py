from rest_framework import serializers


from recall.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['student', 'created_at', 'updated_at']
