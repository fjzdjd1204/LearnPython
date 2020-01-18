from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)

    bpub_date = models.DateField()

    bread = models.IntegerField(default=0)

    bcomment = models.IntegerField(default=0)

    # 软删除
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=False)

    hcomment = models.CharField(max_length=200)

    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    # 软删除
    isDelete = models.BooleanField(default=False)
