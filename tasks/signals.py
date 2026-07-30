from django.db.models.signals import post_save, pre_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from tasks.models import Task
import logging

logger = logging.getLogger(__name__)


@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employees_on_task_creation(sender, instance, action, **kwargs):
    if action == 'post_add':
        # print(instance, instance.assigned_to.all())

        assigned_emails = [emp.email for emp in instance.assigned_to.all()]
        # print("Checking....", assigned_emails)

        if not assigned_emails:
            return

 

@receiver(post_delete, sender=Task)
def delete_associate_details(sender, instance, **kwargs):
    if instance.details:
        # print(isinstance)
        instance.details.delete()

        # print("Deleted successfully")