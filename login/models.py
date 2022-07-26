from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
# 扩展用户字段
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    birthday = models.DateField(null=True, blank=True)
    sex = models.CharField(null=True, max_length=5)
    age = models.CharField(max_length=3, null=True)
    telephoneNumber = models.CharField(max_length=11, null=True)

    # 模型被调用之后执行
    @receiver(post_save, sender=User)
    def create_user_extension(sender, instance, created, **kwargs):
        if created:
            # 创建用户表的
            UserExtension.objects.create(user=instance)
        else:
            instance.extension.save()
