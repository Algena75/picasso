from django.db import models


class File(models.Model):
    name = models.CharField(
        max_length=254,
        verbose_name='File name',
        null=True
    )
    file = models.FileField(
        upload_to='files/',
        null=False,
        unique=True,
        verbose_name='File'
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date/time loading'
    )
    processed = models.BooleanField(
        default=False,
        verbose_name='Status'
    )

    def __str__(self):
        return self.name[:30]

    def save(self, **kwargs):
        self.name = self.file.name
        return super().save(**kwargs)

    class Meta:
        ordering = ('-uploaded_at',)
        verbose_name = 'File'
        verbose_name_plural = 'Files'
