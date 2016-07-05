import logging
import platform
import signal
import subprocess as sp

import tkinter as tk


class VideoRecorder:
    def __init__(self, filename):
        self.filename = filename
        self.proc = None
        self.video_enabled = True

    def start_recording(self):
        is_windows = platform.system() == 'Windows'
        source = 'gdigrab' if is_windows else 'x11grab'
        window = 'desktop' if is_windows else ':0.0'
        command = ['ffmpeg',
                   '-y',  # (optional) overwrite output file if it exists
                   '-f', source,  # grab video from source
                   '-video_size', self.get_screen_size(),  # screen size
                   '-r', '24',  # frames per second
                   '-i', window,  # The imput comes from a pipe
                   '-an',  # Tells FFMPEG not to expect any audio
                   self.filename]

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
