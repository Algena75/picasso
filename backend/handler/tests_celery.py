from django.test import TestCase
from django.test.utils import override_settings
from handler.tasks import get_handler


class AddTestCase(TestCase):
    def setUp(self):
        self.data = {"db_id": 1, "file_name": "small.gif"}

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       CELERY_BROKER_URL="memory://")
    def test_get_handler(self):
        """Тестирование постановки задачи."""
        self.assertTrue(get_handler.delay(self.data))
