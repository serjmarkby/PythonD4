from django.forms import ModelForm, BooleanField
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля.
    # Мы уже делали что-то похожее с фильтрами.
    check_box = BooleanField(label='Согласие')

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'postCategory', 'postPhoto']