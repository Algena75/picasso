from pathlib import Path

from celery import shared_task
from handler import services


@shared_task()
def get_handler(job_params: dict) -> None:
    file_name = job_params["file_name"]
    ext = Path(file_name).suffix[1:]
    handler = services.handle_other_file
    for ext_list in services.FILE_TYPES.keys():
        if ext in ext_list:
            handler = services.FILE_TYPES.get(ext_list)
            break
    return handler(job_params)
