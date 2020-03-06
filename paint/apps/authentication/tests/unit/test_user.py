from django.db.utils import IntegrityError
from django.test import TestCase

from paint.apps.authentication.models import User


class TestUser(TestCase):

    def test_user_creation_should_work_correctly(self):
        try:
            u: User = User.objects.create_user('abc123')
            self.assertEqual(u.identifier, 'abc123')
        except Exception as e:
            self.fail(e)

    def test_user_creation_should_raise_value_error_if_identifier_is_not_passed(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(None)

    def test_user_creation_should_raise_xxx_if_a_user_with_that_id_already_exists(self):
        User.objects.create_user('abc123')
        with self.assertRaises(IntegrityError):
            User.objects.create_user('abc123')