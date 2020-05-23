from django.db import models

# Create your models here.


class MqttData(models.Model):

    topic = models.CharField(max_length=100, verbose_name="话题")
    msg = models.CharField(max_length=300, verbose_name="消息")

    def __str__(self):
        return self.msg

    # def delete(self, using=None, keep_parents=False):
    #     self.is_deleted = True
    #     # some actions
    #     self.save()
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     # some actions
    #     self.name = self.name.capitalize()  # 首字母大写
    #     return super().save(force_insert=force_insert, force_update=force_update, using=using,
    #                         update_fields=update_fields)
    #
    # def __repr__(self):
    #     return "UserProfile:{}".format(self.name)


    # class Meta:
    #     ordering = ['-time_added']
    #     verbose_name = "用户信息"
    #     verbose_name_plural = verbose_name
    #     db_table = "student_info"
    #     unique_together = ("name", "gender")
