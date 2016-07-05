from time import strftime

from com.automation.remarks.recorder.video_recorder import VideoRecorder


def video(enabled=True, name=None):
    def video_decorator(func):
        def wrapper(*args, **kwargs):
            recorder = VideoRecorder('{0}_{1}.mp4'.format(name or func.func_name, strftime("%Y_%m_%d_%H_%M_%S")))
            recorder.video_enabled = enabled
            recorder.start_recording()
            try:
                func(*args, **kwargs)
            finally:
                recorder.stop_recording()

        return wrapper

    return video_decorator
