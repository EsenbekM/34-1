from django.db import models

# ORM - Object Relational Mapper


class HashTag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Хештег"
        verbose_name_plural = "Хештеги"


class Post(models.Model):
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(
        HashTag,
        blank=True,
        related_name='posts'
    )

    def __str__(self) -> str:
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(
        'post.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарий"


class Category(models.Model):
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title