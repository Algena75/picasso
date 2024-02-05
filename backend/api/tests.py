import shutil
import tempfile

from django.test import TestCase, Client
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from api.models import File


class TestApi(TestCase):
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_api_endpoint_main(self):
        response = self.guest_client.get("/")
        assert response.status_code == 200

    def test_api_endpoint_files(self):
        response = self.guest_client.get("/files/")
        self.assertEqual(response.status_code, 200)

    def test_api_endpoint_upload(self):
        response = self.guest_client.get("/upload/")
        self.assertEqual(response.status_code, 405)


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)

@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class FileCreateRecordTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        File.objects.create(file='test.txt')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        self.guest_client = Client()

    def test_create_file(self):
        """Валидная форма создает запись в File."""
        filess_count = File.objects.count()
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00'
            b'\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00'
            b'\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        file_data = {
            'file': uploaded,
        }
        response = self.guest_client.post(
            '/upload/',
            data=file_data
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(File.objects.count(), filess_count+1)
        self.assertTrue(
            File.objects.filter(
                name='small.gif',
                file='files/small.gif'
                ).exists()
        )
