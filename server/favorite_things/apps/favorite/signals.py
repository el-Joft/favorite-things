from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import receiver

from favorite_things.apps.favorite.models import AuditLog, Favorite, Category


@receiver(pre_save, sender=Favorite)  # noqa: C901
def audit_log(sender, instance, **kwargs):
    """
    Method to generate notifications for proposed change in batch quantity.
    """
    try:
        table_pk = instance._meta.pk.name
        table_pk_value = instance.__dict__[table_pk]
        query_kwargs = dict()
        query_kwargs[table_pk] = table_pk_value
        prev_instance = sender.objects.get(
            **query_kwargs)
        excluded_keys = ['_state', 'created', 'modified_at']
        d1, d2 = prev_instance.__dict__, instance.__dict__
        old, new = {}, {}
        table_fields = {}
        for k, v in d1.items():
            if k in excluded_keys:
                continue
            if k == 'id':
                v = str(v)
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})
        table_fields['old'] = old
        table_fields['new'] = new
        table_name = sender.__name__
        action = f'Updated a {prev_instance} {table_name}'
        AuditLog.objects.create(
            table_name=table_name,
            table_fields=table_fields,
            action=action
        )
    except ObjectDoesNotExist:
        table_name = sender.__name__
        action = f'Created a new {table_name}'
        table_fields = {}
        exempted_values = ['modified_at', 'created_at', '_state']
        for key, value in instance.__dict__.items():
            if key in exempted_values:
                continue
            if key == 'id':
                value = str(value)
            if key == 'category_id':
                category = Category.objects.get(id=value)
                value = category.name
                key = 'category'
            table_fields[key] = value
        AuditLog.objects.create(
            table_name=table_name,
            table_fields=table_fields,
            action=action
        )

    return
