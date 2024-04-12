from .test_setup import TestSetup
from django.urls import reverse
from ..models import Task


class TestViews(TestSetup):

    def test_user_is_not_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {''}")
        resp = self.client.get(reverse("check_auth"))

        self.assertEqual(resp.status_code, 401)

    def test_user_is_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.get(reverse("check_auth"))

        self.assertEqual(resp.status_code, 200)

    def test_user_can_create_category(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.post(self.categorys_url, {"name": "test", "color": "#12345"})

        self.assertEqual(resp.status_code, 201)
        self.assertIn("name", resp.data)

    def test_user_can_get_request_user_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.get(self.user_list_url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("id", resp.data[0])
        self.assertIn("initials", resp.data[0])
        self.assertIn("color", resp.data[0])

    def test_user_can_get_request_categorys_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.get(self.categorys_url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("name", resp.data[0])

    def test_user_can_create_task(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.post(self.tasks_url, self.dummy_task)

        self.assertEqual(resp.status_code, 201)

    def test_user_can_get_request_tasks(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.get(self.tasks_url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("title", resp.data[0])

    def test_user_can_get_request_single_task(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.patch(self.single_tasks_url, self.dummy_task)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("id", resp.data)

    def test_user_can_delete_task(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.delete(self.single_tasks_url, self.dummy_task)

        self.assertEqual(resp.status_code, 204)
        self.assertEqual(resp.data["message"], "Task deleted successfully")

    def test_user_can_create_contact(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.post(self.contacts_url, self.dummy_contact)

        self.assertEqual(resp.status_code, 201)
        self.assertIn("id", resp.data)

    def test_user_can_patch_contact(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        self.dummy_contact["name"] = "Hans"
        resp = self.client.patch(self.contacts_with_id_url, self.dummy_contact)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["name"], "Hans")
        self.assertIn("id", resp.data)

    def tes_user_can_delete_contact(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.delete(self.contacts_with_id_url, self.dummy_contact)

        self.assertEqual(resp.status_code, 204)
        self.assertEqual(resp.data["message"], "Contact deleted successfully")

    def test_user_can_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        resp = self.client.post(self.logout_url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["message"], "logout successful")
