# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Post(models.Model):
    p_id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    posttypeid = models.IntegerField(db_column='PostTypeId', blank=True, null=True)  # Field name made lowercase.
    acceptedanswerid = models.IntegerField(db_column='AcceptedAnswerId', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.TextField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True)  # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase.
    owneruserid = models.IntegerField(db_column='OwnerUserId', blank=True, null=True)  # Field name made lowercase.
    ownerdisplayname = models.TextField(db_column='OwnerDisplayName', blank=True, null=True)  # Field name made lowercase.
    lasteditoruserid = models.IntegerField(db_column='LastEditorUserId', blank=True, null=True)  # Field name made lowercase.
    lasteditdate = models.TextField(db_column='LastEditDate', blank=True, null=True)  # Field name made lowercase.
    lastactivitydate = models.TextField(db_column='LastActivityDate', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True, null=True)  # Field name made lowercase.
    answercount = models.IntegerField(db_column='AnswerCount', blank=True, null=True)  # Field name made lowercase.
    commentcount = models.IntegerField(db_column='CommentCount', blank=True, null=True)  # Field name made lowercase.
    closeddate = models.TextField(db_column='ClosedDate', blank=True, null=True)  # Field name made lowercase.
    favoritecount = models.IntegerField(db_column='FavoriteCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Post'
