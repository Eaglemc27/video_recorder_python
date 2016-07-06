from time import sleep

from pytest import fail

from test_recorder.decorator import video, video_recorder


@video_recorder(video(enabled=True))
class TestGoogleSearch(object):
    def test_1(self):
        sleep(5)
        fail()

    def test_2(self):
        sleep(5)
        fail()

    def test_3(self):
        sleep(5)
        fail()
