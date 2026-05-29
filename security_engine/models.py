from django.db import models


class SecurityLog(models.Model):

    username=models.CharField(
        max_length=100
    )

    role=models.CharField(
        max_length=100
    )

    action=models.CharField(
        max_length=100
    )

    status=models.CharField(
        max_length=100
    )

    timestamp=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.username} - {self.status}"