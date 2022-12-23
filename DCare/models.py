# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Counsel(models.Model):
    objects = models.Manager() #views.py에서 objects 찾을 수 없다 경고 뜰 때 추가해줌
    cnselno = models.AutoField(primary_key=True)
    cnselask = models.CharField(max_length=300)
    cnselanswer = models.CharField(max_length=600)

    class Meta:
        managed = False
        db_table = 'counsel'


class Members(models.Model):
    memno = models.AutoField(primary_key=True)
    mempid = models.CharField(max_length=100)
    memmail = models.CharField(max_length=300)
    mempwd = models.CharField(max_length=100)
    memnm = models.CharField(max_length=100)
    memnick = models.CharField(max_length=100)
    memage = models.IntegerField()
    memgender = models.CharField(max_length=100)
    memtel = models.CharField(max_length=100)
    memaddr = models.CharField(max_length=300)
    memrule = models.IntegerField()
    memimg = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'
