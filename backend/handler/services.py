import logging

from api.models import File


def handle_image_file(job_params: dict) -> None:
    """Функция обработки графического файла"""
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as image file.'
    )


def handle_media_file(job_params: dict) -> None:
    """Функция обработки медиа файла"""
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as media file.'
    )


def handle_text_file(job_params: dict) -> None:
    """Функция обработки текстового файла"""
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as text file.'
    )


def handle_pdf_file(job_params: dict) -> None:
    """Функция обработки pdf файла"""
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as pdf file.'
    )


def handle_other_file(job_params: dict) -> None:
    """Функция обработки файла, не обработанного ранее."""
    file = File.objects.get(pk=job_params["db_id"])
    file.processed = True
    file.save()
    logging.info(
        f'File {file.name} was processed as other file.'
    )


FILE_TYPES = {
    ('jpg', 'gif', 'bmp'): handle_image_file,
    ('doc', 'docx', 'txt'): handle_text_file,
    ('pdf',): handle_pdf_file,
    ('mkv', 'mp3', 'avi'): handle_media_file
}
