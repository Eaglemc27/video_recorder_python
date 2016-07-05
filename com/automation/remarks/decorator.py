import os
from os.path import expanduser
from time import strftime

from com.automation.remarks.recorder.video_recorder import VideoRecorder
from com.automation.remarks.utils.file_utils import create_dir
import inspect


def video(enabled=True, name=None):
    def video_decorator(func):

        def wrapper(*args, **kwargs):
            file_path = get_file_path(name, func)
            recorder = VideoRecorder(file_path)
            recorder.video_enabled = enabled
            recorder.start_recording()
            try:
                func(*args, **kwargs)
                os.remove(file_path)
            finally:
                recorder.stop_recording()

        return wrapper

    def get_file_path(expected_name, func):
        dir_path = expanduser("~") + os.sep + 'video'  # video folder path
        create_dir(dir_path)  # create video folder if not exists
        file_name = '{0}_{1}.mp4'.format(expected_name or func.func_name, strftime("%Y_%m_%d_%H_%M_%S"))  # format timestamp
        return dir_path + os.sep + file_name  # save file to user_home/video directory

    return video_decorator


def class_recorder(decorator, prefix='test_'):
    def wrapper(cls):
        for name, m in inspect.getmembers(cls, inspect.ismethod):
            if name.startswith(prefix):
                setattr(cls, name, decorator(m))
        return cls

    return wrapper
