from django import forms
from post.models import Post, Review, Products


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=256,
        label='Название поста'
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label='Описание поста'
    )
    image = forms.ImageField(
        required=False,
        label='Изображние поста'
    )
    rate = forms.IntegerField(
        label='Рейтинг поста'
    )


class ProductForm(forms.Form):
    title = forms.CharField(
        max_length=256,
        label='Название продукта'
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 4
            }
        ),
        label='Описание продукта'
    )
    image = forms.ImageField(
        required=False,
        label='Изображение продукта'
    )
    price = forms.IntegerField(
        label='Цена продукта'
    )


class CategoryForm(forms.Form):
    type = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 1
            }
        ),
        label='Категория'
    )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['product']
        fields = ('text',)

        labels = {
            'product': 'Продукт',
            'text': 'Отзыв',
        }

        help_texts = {
            'product': 'Выберите продукт',
            'text': 'Введите ваш отзыв'
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'python' not in title.lower():
    #         raise forms.ValidationError('Ну и где "python" в названии а???')
    #     return title

    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get('title')
    #     text = cleaned_data.get('text')
    #


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'rate')
        labels = {
            'title': 'Название поста',
            'text': 'Текст поста',
            'image': 'Картинка',
            'rate': 'Рейтинг',
        }
        help_texts = {
            'title': 'Введите название поста',
            'text': 'Введите текст поста',
            'image': 'Загрузите картинку',
            'rate': 'Введите рейтинг',
        }


class ProductForm2(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('title', 'description', 'image', 'price')
        labels = {
            'title': 'Название продукта',
            'description': 'Описание продукта',
            'image': 'Картинка',
            'price': 'Цена',
        }
        help_texts = {
            'title': 'Введите название продукта',
            'description': 'Введите описание продукта',
            'image': 'Загрузите картинку',
            'price': 'Введите цену',
        }