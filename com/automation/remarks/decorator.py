from time import strftime

from com.automation.remarks.recorder.video_recorder import VideoRecorder


def video(func):
    def wrapper(*args, **kwargs):
        recorder = VideoRecorder('{0}_{1}.mp4'.format(func.func_name, strftime("%Y_%m_%d_%H_%M_%S")))
        recorder.start_recording()
        try:
            func(*args, **kwargs)
        finally:
            recorder.stop_recording()

    return wrapper
