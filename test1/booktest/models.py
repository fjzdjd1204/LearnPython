from django.db import models


# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)

    # publish date
    bpub_date = models.DateField()

    def __str__(self):
        #返回书名
        return self.btitle

# test file
class HeroInfo(models.Model):
    '''人物'''
    hname = models.CharField(max_length=20)

    hgender = models.BooleanField(default=False)

    hcomment = models.CharField(max_length=128)

    hbook= models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        #返回书名
        return self.hname