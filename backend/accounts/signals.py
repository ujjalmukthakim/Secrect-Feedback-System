from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CoustomUser,Link
import uuid

@receiver(post_save,sender=CoustomUser)
def create_user_link(sender,instance,created,**kwargs):
    if created:
        Link.objects.create(
            user=instance,
            link=str(uuid.uuid4())[:8]
        )


