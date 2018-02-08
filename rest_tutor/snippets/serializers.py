from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOISES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'linenos', 'language', 'style','owner',)



class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

    """
    Эта часть определяет поля которые становяться сериализованными а метод create & update
    создают и обновляют данные
    """
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,allow_blank=True,max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOISES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
    """
    """
        создает и возвращает новый snippet учитывая новые данные

        :param validated_data:
        :return:
        """
    #  return Snippet.objects.create(**validated_data)


    #def update(self, instance, validated_data):
    """
        Обновляет и возвращает существующий варинт учитывая утвержденные данные
        :param instance:
        :param validated_data:
        :return:
        """
    #    instance.title = validated_data.get('title',instance.title)
    #   instance.code = validated_data.get('code',instance.code)
    #    instance.linenos = validated_data.get('linenos', instance.linenos)
    #   instance.language = validated_data.get('language', instance.language)
    #    instance.style = validated_data.get('style', instance.style)
    #    instance.save()
    #    return instance