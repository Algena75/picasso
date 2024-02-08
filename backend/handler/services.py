import logging
import mimetypes

if __name__ != '__main__':
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


def main():
    """files_ext.txt creation"""
    types_map = mimetypes.types_map
    file_types = dict()
    for item in types_map.items():
        ext, descr = tuple(item)
        descr = descr.split('/')[0]
        if descr != 'application':
            if descr not in file_types:
                file_types[descr] = list()
            file_types[descr].append(ext)
    with open('files_ext.txt', 'w') as f:
        for line in file_types.items():
            f.write(f'{line[0]}: {tuple(line[1])}\n')


if __name__ == '__main__':
    main()
