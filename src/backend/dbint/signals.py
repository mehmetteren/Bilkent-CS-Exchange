from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from dbint.constants import *
from dbint.models.ActorModels import Student
from dbint.models.SystemModels import Notification
from django.dispatch import receiver


@receiver(post_save, sender='dbint.User')
def add_user_to_default_group(sender, instance, created=False, **kwargs):
    if created:
        my_group = Group.objects.get(name='Users')
        my_group.user_set.add(instance)
        print(my_group.user_set)
        my_group.save()
    my_group = Group.objects.get(name='a')
    my_group.user_set.add(instance)
    print(my_group.user_set)
    my_group.save()
    print(instance.groups)

@receiver(post_save, sender='dbint.Reply')
@receiver(post_delete, sender='dbint.Reply')
def update_thread_reply_count(sender, instance, created=False, **kwargs):
    if created:
        # Increment the reply_count field of the associated thread
        instance.thread.reply_count += 1

        notificationText = instance.user.first_name + instance.user.last_name + " replied your thread!"
        notificationCreated = Notification.objects.create(text=notificationText, user=instance.thread.user,
                                                          seen=False, type='Reply')
        notificationCreated.save()
    else:
        # Decrement the reply_count field of the associated thread
        instance.thread.reply_count -= 1

    instance.thread.save()


@receiver(post_save, sender='dbint.Review')
def increment_uni_review_count(sender, instance, created=False, **kwargs):
    if created:
        if not instance.reviewer.entered_review:
            instance.university.review_count += 1
            instance.university.calculate_rating()

    else:
        pass
    instance.reviewer.save()
    instance.university.save()


@receiver(post_delete, sender='dbint.Review')
def decrement_uni_review_count(sender, instance, created=False, **kwargs):
    instance.university.review_count -= 1
    if not instance.reviewer.fstu_reviews.all():
        instance.reviewer.entered_review = False
        instance.university.calculate_rating()
        instance.reviewer.save()


@receiver(post_save, sender='dbint.Announcement')
def create_notf_for_announcement(sender, instance, created=False, **kwargs):
    if created:
        students = Student.objects.all()
        for tempStudent in students:
            notificationCreated = Notification.objects.create(text='There is an announcement!', user=tempStudent,
                                                              seen=False, type='Announcement')
            notificationCreated.save()


@receiver(post_save, sender='dbint.Message')
def create_notf_for_message(sender, instance, created=False, **kwargs):
    if created:
        notificationText = "You have a message from " + instance.sender.first_name + instance.sender.last_name
        notificationCreated = Notification.objects.create(text=notificationText, user=instance.receiver,
                                                          seen=False, type='Message')
        notificationCreated.save()


@receiver(post_save, sender='dbint.Document')
def create_notf_for_document(sender, instance, created=False, **kwargs):
    if created:
        student_type = instance.document_owner.user_type
        if student_type == ASTU:
            notificationText = instance.document_owner.first_name + instance.document_owner.last_name + " uploaded a file!"
            notificationCreatedDEPC = Notification.objects.create(text=notificationText, user=instance.document_owner.get_manager()
                                                                  .get(id=instance.document_owner.id).stu_depc,
                                                              seen=False, type='File Upload')
            notificationCreatedEXCC = Notification.objects.create(text=notificationText,
                                                                  user=instance.document_owner.get_manager()
                                                                  .get(id=instance.document_owner.id).stu_excc,
                                                                  seen=False, type='File Upload')
            notificationCreatedDEPC.save()
            notificationCreatedEXCC.save()
