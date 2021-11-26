from django.db import models
from django.core.exceptions import ValidationError
import re
import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse





def validate(value):
    pattern = '^[0-3]'
    if not  re.match(pattern, str(value)):
        raise ValidationError(f"{value} values can not be greater than 2")
    return value

class Course(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=150,null=True,blank=True,unique=True)
    credits=models.IntegerField(validators=[validate])
    
    def __str__(self):
        return self.title
    def absolute_url(self):
        return reverse ("genericview-detail", kwargs={"id":self.id,"slug":self.slug})
    
def create_slug(instance, new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs=Course.objects.filter(slug=slug).order_by('-id')
    exists=qs.exists()
    if exists:
        new_slug="%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_course_reciver(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)
pre_save.connect(pre_save_course_reciver,sender=Course)
    
    
