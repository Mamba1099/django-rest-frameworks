from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# """creating a serializer instance """
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'}) #field that represent actual code snippet
#     linenos = serializers.BooleanField(required=False) 
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python') # represents programming language of the code
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly') # code style

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

#using model serializer
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        
        
# adding endpoints for our User models
class UserSerializer(serializers.ModelSerializer):
    """Serialize user data"""
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets'] # fields from user modelto be included in the serialized representation
        owner = serializers.ReadOnlyField(source='owner.username') # read-only field