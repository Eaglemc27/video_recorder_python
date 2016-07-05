from selene.conditions import *
from com.automation.remarks.decorator import video
from tests.base_test import *
from tests.pages.google_page import GooglePage


class TestGoogleSearch(BaseTest):
    @video(name="demo")
    def test_selene_demo(self):
        google = GooglePage().open()
        search = google.search("selene")
        search.results[0].assure(text("In Greek mythology, Selene is the goddess of the moon"))

    @video()
    def test_selene_demo2(self):
        google = GooglePage().open()
        search = google.search("selene")
        search.results[1].assure(text("In Greek mythology, Selene is the goddess of the moo"))
