import platform

is_windows = platform.system() == 'Windows'
is_mac = platform.system() == 'Darwin'


def get_source():
    if is_mac:
        return 'avfoundation'
    elif is_windows:
        return 'gdigrab'
    else:
        return 'x11grab'


def get_window():
    return 'desktop' if is_windows else ':0.0'


def get_screen_size():
    if is_windows:
        import ctypes
        user32 = ctypes.windll.user32
        return __format__(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    else:
        import tkinter as tk
        root = tk.Tk()
        return __format__(root.winfo_screenwidth(), root.winfo_screenheight())


def __format__(screen_width, screen_height):
    return '{0}x{1}'.format(screen_width, screen_height)
