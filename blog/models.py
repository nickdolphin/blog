from django.db import models

class Post(models.Model):
    '''данные о записи'''
    title = models.CharField('Заголовок', max_length=32)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя Автора', max_length=32)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''комментарии'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=32)
    text_comments = models.TextField("Текст комментария", max_length=500)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адрес', max_length=50)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
