from django.db import models

class Post(models.Model):
    '''Post information'''
    title = models.CharField('Title', max_length=32)
    description = models.TextField('Text')
    author = models.CharField('Authors name', max_length=32)
    date = models.DateField('Publication date')
    img = models.ImageField('Image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comments(models.Model):
    '''comments'''
    email = models.EmailField()
    name = models.CharField('Name', max_length=32)
    text_comments = models.TextField("Comment text", max_length=500)
    post = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    '''Likes'''
    ip = models.CharField('IP', max_length=50)
    pos = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)
