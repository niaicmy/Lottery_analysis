from django.db import models


# Create your models here.
class SsqInfo(models.Model):
    # 开奖期数
    number = models.PositiveIntegerField(primary_key=True)
    # 一个SsqNum记录 对应一个SsqInfo记录
    # ssq_num = models.OneToOneField("SsqNum", on_delete=models.CASCADE, to_field="number")

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
        ordering = ["number"]


class SsqNum(models.Model):
    number = models.PositiveIntegerField(primary_key=True)

    red1 = models.CharField(max_length=2)
    red2 = models.CharField(max_length=2)
    red3 = models.CharField(max_length=2)
    red4 = models.CharField(max_length=2)
    red5 = models.CharField(max_length=2)
    red6 = models.CharField(max_length=2)
    blue = models.CharField(max_length=2)
    # ssqinfo = models.ForeignKey("SsqInfo", on_delete=models.CASCADE)
    # 一个SsqNum记录 对应一个SsqInfo记录
    # ssqinfo = models. OneToOneField("SsqInfo", on_delete=models.CASCADE)

    class Meta:
        # db_table = "ssq_num"
        ordering = ["number"]
