from rest_framework import serializers
from .models import User,Photo,Post

# сериалайзер нужен для того что бы конвертировать любые типы данных,или предоставлять информацию
# о модели

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField('posts',view_name='userpost-list',
                                                 lookup_field='username')
    # для пользователя мы открыли все поля кроме пароля и эмейла
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','posts',)

# для постсериалайзерс мы выбрали вставку данных автора сразу в пост
# до этого в поле автор была ссылка на данные автора
class PostSerializers(serializers.ModelSerializer):
    # что бы привязать данные автора к постсериалайзер нам придется сделать данные под АПИ
    # поэтому мы делаем поле автора необязательным required=False в сериализаторе поста и делаем
    # его не исключением валидации
    author = UserSerializer(required=False)
    photos = serializers.HyperlinkedIdentityField('photos',view_name='postphoto-list')

    def get_validation_exclusion(self):

        exclusions = super(PostSerializers,self).get_validation_exclusions()
        return exclusions + ['author']

    class Meta:
        model = Post


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.Field('image.url')

    # для фото мы конвертируем таким способом чтобы возвращалась ссылка на изображение
    # а не путь на медиа каталог
    class Meta:
        model = Post