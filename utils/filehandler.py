from django.conf import settings


import os


def handle_file_upload(f):
    static_dir = settings.STATICFILES_DIRS[0]
    file_path = os.path.join(static_dir, "excel", "masterfile.xlsx")
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
