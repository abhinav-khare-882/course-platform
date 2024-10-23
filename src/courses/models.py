from django.db import models

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON="soon","Coming Soon"
    DRAFT = "draft", "Draft"

class AcessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email required"

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    #image
    access=models.CharField(
        max_length=10,
        choices=AcessRequirement.choices,
    )
    status=models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )