from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return (f'{self.text[:15]}; Author: {self.author};'
                f' Group: {self.group}; Pub_date: {self.pub_date}')


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return (f'{self.text[:15]}; Author: {self.author};'
                f' Post: {self.post.id}; Created: {self.created}')


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower",
        verbose_name="Подписчик",
        help_text="Этот пользователь подписан на автора"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following",
        verbose_name="Автор", help_text="Ваша подписка"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_following'),
            models.CheckConstraint(
                name="prevent_self_follow",
                check=~models.Q(user=models.F("following")),
            ),
        ]
        ordering = ['following']

    def __str__(self):
        return f'User {self.user} following {self.following}'
