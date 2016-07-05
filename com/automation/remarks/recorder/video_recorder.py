import logging
import os
import signal
import subprocess as sp

import tkinter as tk

from com.automation.remarks.utils.file_utils import create_dir
from os.path import expanduser


class VideoRecorder:
    def __init__(self, filename):
        self.filename = filename
        self.proc = None
        self.video_enabled = True

    def start_recording(self):
        dir_path = expanduser("~") + os.sep + 'video'  # video folder path
        create_dir(dir_path)  # create video folder if not exists

        command = ['ffmpeg',
                   '-y',  # (optional) overwrite output file if it exists
                   '-f', 'x11grab',  # grab video from source
                   '-video_size', self.get_screen_size(),  # screen size
                   '-r', '24',  # frames per second
                   '-i', ':0.0',  # The imput comes from a pipe
                   '-an',  # Tells FFMPEG not to expect any audio
                   dir_path + os.sep + self.filename]

        if self.video_enabled:
            self.proc = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

    def stop_recording(self):
        if self.video_enabled:
            self.proc.send_signal(signal.SIGINT)
            err = self.proc.communicate()
            logging.info(err)

    def get_screen_size(self):
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        return '{0}x{1}'.format(screen_width, screen_height)
