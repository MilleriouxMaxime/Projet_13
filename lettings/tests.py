# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class AddressModelTest(TestCase):
    def test_str(self):
        address = Address.objects.create(
            number=123,
            street="Main St",
            city="Testville",
            state="TS",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.assertEqual(str(address), "123 Main St")


class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="Test St",
            city="City",
            state="ST",
            zip_code=11111,
            country_iso_code="USA",
        )

    def test_str(self):
        letting = Letting.objects.create(title="Test Letting", address=self.address)
        self.assertEqual(str(letting), "Test Letting")


class LettingsViewsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="Test St",
            city="City",
            state="ST",
            zip_code=11111,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", address=self.address
        )

    def test_index_view(self):
        url = reverse("lettings:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")

    def test_letting_view(self):
        url = reverse("lettings:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Letting")
        self.assertContains(response, "Test St")


class LettingsURLsTest(TestCase):
    def test_index_url(self):
        url = reverse("lettings:index")
        self.assertEqual(url, "/lettings/")

    def test_letting_url(self):
        # Create dummy objects to get a valid id
        address = Address.objects.create(
            number=1,
            street="Test St",
            city="City",
            state="ST",
            zip_code=11111,
            country_iso_code="USA",
        )
        letting = Letting.objects.create(title="Test Letting", address=address)
        url = reverse("lettings:letting", args=[letting.id])
        self.assertEqual(url, f"/lettings/{letting.id}/")
