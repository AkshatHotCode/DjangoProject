#python manage.py test ApplicantTracking
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ApplicantTracking.views import (home, signup, signin, signout, opening, candidates,
                                     pipeline, placement, account, dashboard, addopenings,
                                     addcandidates, addpipeline, addplacement, addaccount)

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signup)

    def test_signin_url_is_resolved(self):
        url = reverse('signin')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signin)

    def test_signout_url_is_resolved(self):
        url = reverse('signout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signout)

    def test_openings_url_is_resolved(self):
        url = reverse('openings')
        print(resolve(url))
        self.assertEqual(resolve(url).func, opening)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signup)

    def test_candidates_url_is_resolved(self):
        url = reverse('candidates')
        print(resolve(url))
        self.assertEqual(resolve(url).func, candidates)

    def test_pipeline_url_is_resolved(self):
        url = reverse('pipeline')
        print(resolve(url))
        self.assertEqual(resolve(url).func, pipeline)

    def test_placement_url_is_resolved(self):
        url = reverse('placement')
        print(resolve(url))
        self.assertEqual(resolve(url).func, placement)

    def test_account_url_is_resolved(self):
        url = reverse('account')
        print(resolve(url))
        self.assertEqual(resolve(url).func, account)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEqual(resolve(url).func, dashboard)

    def test_addopenings_url_is_resolved(self):
        url = reverse('addopenings')
        print(resolve(url))
        self.assertEqual(resolve(url).func, addopenings)

    def test_addcandidates_url_is_resolved(self):
        url = reverse('addcandidates')
        print(resolve(url))
        self.assertEqual(resolve(url).func, addcandidates)

    def test_addpipeline_url_is_resolved(self):
        url = reverse('addpipeline')
        print(resolve(url))
        self.assertEqual(resolve(url).func, addpipeline)

    def test_addplacement_url_is_resolved(self):
        url = reverse('addplacement')
        print(resolve(url))
        self.assertEqual(resolve(url).func, addplacement)

    def test_addaccount_url_is_resolved(self):
        url = reverse('addaccount')
        print(resolve(url))
        self.assertEqual(resolve(url).func, addaccount)