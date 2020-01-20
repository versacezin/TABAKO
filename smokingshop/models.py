from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
#ここまでがカテゴリのモデル

class Shop(models.Model):
    name = models.CharField('店舗名', max_length=255)
    Address = models.CharField('住所入力', max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey( #←ここから
        Category,  verbose_name='ジャンル',               #カテゴリとショップモデルを関連付けしてる項目ショップからカテゴリを参照しているのでカテゴリから記述する必要がある
        on_delete=models.PROTECT,  #category変数はマイグレーションすると勝手にcategoryIDというカラムを作成してくれる
    )                             #←ここまで
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('smokingshop:detail', kwargs={'pk': self.pk})