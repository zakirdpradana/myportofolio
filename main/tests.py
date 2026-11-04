import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, 'id="experience-search-form"')
        self.assertContains(response, 'id="grid"')

        api_response = self.client.get(reverse("api:experience-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.data[0]["title"], self.experience.title)
        self.assertEqual(api_response.data[0]["description"], self.experience.description)
        self.assertEqual(api_response.data[0]["category"], "part-time")
        self.assertTrue(api_response.data[0]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan atau ditemukan.")

        api_response = self.client.get(reverse("api:experience-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.data, [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        self.assertFalse(self.experience.is_ongoing)

        api_response = self.client.get(
            reverse("api:experience-detail", args=[self.experience.id])
        )
        self.assertEqual(api_response.status_code, 200)
        self.assertFalse(api_response.data["is_ongoing"])

class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution_name="Universitas Indonesia",
            description="Mahasiswa S1 Ilmu Komputer",
            thumbnail="https://example.com/ui.png",
            started_at=datetime.date(2024, 9, 1),
            ended_at=None,
        )

    def test_education_url_and_template(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

    def test_education_page_shows_data(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="education-search-form"')
        self.assertContains(response, 'id="list"')

        json_response = self.client.get(reverse("main:get_education_json"))
        self.assertEqual(json_response.status_code, 200)
        data = json_response.json()
        self.assertEqual(data[0]["fields"]["institution_name"], self.education.institution_name)
        self.assertEqual(data[0]["fields"]["description"], self.education.description)

    def test_empty_education_page(self):
        Education.objects.all().delete()

        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada riwayat pendidikan yang ditambahkan atau ditemukan.")

        json_response = self.client.get(reverse("main:get_education_json"))
        self.assertEqual(json_response.status_code, 200)
        self.assertEqual(json_response.json(), [])