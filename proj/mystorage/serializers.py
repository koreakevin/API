from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='auhor.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='auhor.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')

class FilesSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='auhor.username')
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk', 'author_name', 'myfile', 'desc')