import uuid

from django.db import models

from user.models import User


class File(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming your custom user model is named `User`
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=50)
    file_size = models.PositiveIntegerField()  # in bytes
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically set file_type and file_size when saving
        if self.file:
            self.file_type = self.file.name.split('.')[-1]
            self.file_size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
