from django.db import models
import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse


class Students(models.Model):
    name = models.CharField(max_length=250)
    slug=models.SlugField(unique=True,max_length=200, default='',null=True,blank=True)
    roll=models.IntegerField()
    classes=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('studentapi', kwargs={'slug': self.slug})
    
def create_slug(instance,new_slug=None):
    slug=slugify(instance.name) 
    if new_slug is not None:
        slug=new_slug
    qs=Students.objects.filter(slug=slug).order_by('-id')
    exists=qs.exists()
    if exists:
        new_slug="%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Students)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    pre_save.connect(pre_save_receiver,Students)
    
        