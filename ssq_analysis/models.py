from django.db import models


# Create your models here.
# 注意：Django 1.7 及以上的版本需要连续执行以下命令
# python manage.py makemigrations
# python manage.py migrate
# 问题 https://blog.csdn.net/pipisorry/article/details/45727309
# django.db.utils.ProgrammingError: (1146

class SsqInfo(models.Model):
    # 开奖期数 primary_key
    number = models.PositiveIntegerField(primary_key=True)

    # 一个SsqOrig记录 对应一个SsqInfo记录
    # ssq_num = models.OneToOneField("SsqOrig", on_delete=models.CASCADE, to_field="number")

    red01 = models.PositiveIntegerField()
    red02 = models.PositiveIntegerField()
    red03 = models.PositiveIntegerField()
    red04 = models.PositiveIntegerField()
    red05 = models.PositiveIntegerField()
    red06 = models.PositiveIntegerField()
    red07 = models.PositiveIntegerField()
    red08 = models.PositiveIntegerField()
    red09 = models.PositiveIntegerField()
    red10 = models.PositiveIntegerField()
    red11 = models.PositiveIntegerField()
    red12 = models.PositiveIntegerField()
    red13 = models.PositiveIntegerField()
    red14 = models.PositiveIntegerField()
    red15 = models.PositiveIntegerField()
    red16 = models.PositiveIntegerField()
    red17 = models.PositiveIntegerField()
    red18 = models.PositiveIntegerField()
    red19 = models.PositiveIntegerField()
    red20 = models.PositiveIntegerField()
    red21 = models.PositiveIntegerField()
    red22 = models.PositiveIntegerField()
    red23 = models.PositiveIntegerField()
    red24 = models.PositiveIntegerField()
    red25 = models.PositiveIntegerField()
    red26 = models.PositiveIntegerField()
    red27 = models.PositiveIntegerField()
    red28 = models.PositiveIntegerField()
    red29 = models.PositiveIntegerField()
    red30 = models.PositiveIntegerField()
    red31 = models.PositiveIntegerField()
    red32 = models.PositiveIntegerField()
    red33 = models.PositiveIntegerField()

    blue01 = models.PositiveIntegerField()
    blue02 = models.PositiveIntegerField()
    blue03 = models.PositiveIntegerField()
    blue04 = models.PositiveIntegerField()
    blue05 = models.PositiveIntegerField()
    blue06 = models.PositiveIntegerField()
    blue07 = models.PositiveIntegerField()
    blue08 = models.PositiveIntegerField()
    blue09 = models.PositiveIntegerField()
    blue10 = models.PositiveIntegerField()
    blue11 = models.PositiveIntegerField()
    blue12 = models.PositiveIntegerField()
    blue13 = models.PositiveIntegerField()
    blue14 = models.PositiveIntegerField()
    blue15 = models.PositiveIntegerField()
    blue16 = models.PositiveIntegerField()

    class Meta:
        # db_table = "ssq_info"
        # abstract = True
        db_table = "ssq_info"
        ordering = ["-number"]


# 原始数据类
class SsqOrig(models.Model):
    number = models.PositiveIntegerField(primary_key=True)

    red1 = models.CharField(max_length=2)
    red2 = models.CharField(max_length=2)
    red3 = models.CharField(max_length=2)
    red4 = models.CharField(max_length=2)
    red5 = models.CharField(max_length=2)
    red6 = models.CharField(max_length=2)
    blue = models.CharField(max_length=2)

    # parity 奇偶比
    mparity = models.CharField(max_length=4)
    # totality 和值
    mtotal = models.CharField(max_length=4)
    # ssqinfo = models.ForeignKey("SsqInfo", on_delete=models.CASCADE)
    # 一个SsqOrig记录 对应一个SsqInfo记录
    # ssqinfo = models. OneToOneField("SsqInfo", on_delete=models.CASCADE)

    class Meta:
        # db_table = "ssq_num"
        # abstract = True
        db_table = "ssq_orig"
        ordering = ["-number"]


# 数据活跃度  vitality 存储 红球, 篮球, 奇偶比, 和值  还是动态分析 存储不方便
# class SsqVital(models.Model):
#     # 开奖期数 primary_key
#     number = models.PositiveIntegerField(primary_key=True)
#
#     red01 = models.FloatField()
#     red02 = models.FloatField()
#     red03 = models.FloatField()
#     red04 = models.FloatField()
#     red05 = models.FloatField()
#     red06 = models.FloatField()
#     red07 = models.FloatField()
#     red08 = models.FloatField()
#     red09 = models.FloatField()
#     red10 = models.FloatField()
#     red11 = models.FloatField()
#     red12 = models.FloatField()
#     red13 = models.FloatField()
#     red14 = models.FloatField()
#     red15 = models.FloatField()
#     red16 = models.FloatField()
#     red17 = models.FloatField()
#     red18 = models.FloatField()
#     red19 = models.FloatField()
#     red20 = models.FloatField()
#     red21 = models.FloatField()
#     red22 = models.FloatField()
#     red23 = models.FloatField()
#     red24 = models.FloatField()
#     red25 = models.FloatField()
#     red26 = models.FloatField()
#     red27 = models.FloatField()
#     red28 = models.FloatField()
#     red29 = models.FloatField()
#     red30 = models.FloatField()
#     red31 = models.FloatField()
#     red32 = models.FloatField()
#     red33 = models.FloatField()
#
#     blue01 = models.FloatField()
#     blue02 = models.FloatField()
#     blue03 = models.FloatField()
#     blue04 = models.FloatField()
#     blue05 = models.FloatField()
#     blue06 = models.FloatField()
#     blue07 = models.FloatField()
#     blue08 = models.FloatField()
#     blue09 = models.FloatField()
#     blue10 = models.FloatField()
#     blue11 = models.FloatField()
#     blue12 = models.FloatField()
#     blue13 = models.FloatField()
#     blue14 = models.FloatField()
#     blue15 = models.FloatField()
#     blue16 = models.FloatField()
#
#     class Meta:
#         abstract = True
#         db_table = "ssq_vital"
#         ordering = ["-number"]
