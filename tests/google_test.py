from time import sleep

from pytest import fail

from com.automation.remarks.decorator import video, video_recorder
from tests.base_test import *


@video_recorder(video(enabled=True))
class TestGoogleSearch(BaseTest):
    def test_1(self):
        sleep(5)
        fail()

    def test_2(self):
        sleep(5)
        fail()

    def test_3(self):
        sleep(5)
        fail()
