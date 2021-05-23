from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created']
        # fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=True, max_length=200, allow_blank=False)
    # content = serializers.CharField(required=False, allow_blank=True)
    # author = serializers.CharField(required=True, max_length=200, allow_blank=False)
    # created = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance