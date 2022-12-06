from django.test import TestCase, Client
from django.urls import reverse

class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.signup_url = reverse('signup')
        self.signin_url = reverse('signin')
        self.openings_url = reverse('openings')
        self.candidates_url = reverse('candidates')
        self.pipeline_url = reverse('pipeline')
        self.placement_url = reverse('placement')
        self.account_url = reverse('account')


    def test_home(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/index.html')

    def test_signup(self):
        response = self.client.get(self.signup_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/signup.html')

    def test_signin(self):
        response = self.client.get(self.signin_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/signin.html')

    def test_openings(self):
        response = self.client.get(self.openings_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/openings.html')

    def test_candidates(self):
        response = self.client.get(self.candidates_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/candidates.html')

    def test_pipeline(self):
        response = self.client.get(self.pipeline_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/pipeline.html')

    def test_placement(self):
        response = self.client.get(self.placement_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/placement.html')

    def test_account(self):
        response = self.client.get(self.account_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ApplicantTracking/account.html')