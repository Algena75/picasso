import logging
from pathlib import Path

from celery import shared_task
from api.models import File


def handle_image_file(job_params):
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as image file.'
    )


def handle_media_file(job_params):
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as media file.'
    )


def handle_text_file(job_params):
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as text file.'
    )


def handle_pdf_file(job_params):
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as pdf file.'
    )


def handle_other_file(job_params):
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as other file.'
    )


FILE_TYPES = {
    ('jpg', 'gif', 'bmp'): handle_image_file,
    ('doc','docx', 'txt'): handle_text_file,
    ('pdf',): handle_pdf_file,
    ('mkv', 'mp3', 'avi'): handle_media_file
}


@shared_task()
def get_handler(job_params):
    file_name = job_params["file_name"]
    ext = Path(file_name).suffix[1:]
    handler = handle_other_file
    for ext_list in FILE_TYPES.keys():
        if ext in ext_list:
            handler = FILE_TYPES.get(ext_list)
            break
    return handler(job_params)
