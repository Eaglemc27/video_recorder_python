import logging
import signal
import subprocess as sp

import tkinter as tk


class VideoRecorder:
    def __init__(self, filename):
        self.filename = filename
        self.proc = None

    def start_recording(self):
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        command = ['ffmpeg',
                   '-y',  # (optional) overwrite output file if it exists
                   '-f', 'x11grab',  # grab video from source
                   '-video_size', '{0}x{1}'.format(screen_width, screen_height),  # screen size
                   '-r', '24',  # frames per second
                   '-i', ':0.0',  # The imput comes from a pipe
                   '-an',  # Tells FFMPEG not to expect any audio
                   self.filename]

        self.proc = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

    def stop_recording(self):
        self.proc.send_signal(signal.SIGINT)
        err = self.proc.communicate()
        logging.info(err)
