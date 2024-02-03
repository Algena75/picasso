from celery import shared_task

from api.models import File


@shared_task()
def handle_file(job_params):
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
