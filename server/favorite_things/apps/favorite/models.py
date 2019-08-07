import uuid
from django.contrib.postgres.fields import JSONField
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True,
                            null=False, blank=False)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(
        max_length=7000)
    ranking = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, related_name='favorite', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class MetaData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    favorite = models.ForeignKey(Favorite, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.key


class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    table_name = models.CharField(max_length=132, null=False, blank=True)
    table_fields = JSONField(default=dict)
    action = models.CharField(
        max_length=200, null=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "favorite"
        db_table = "audit_log"
