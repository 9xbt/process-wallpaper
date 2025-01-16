import ctypes
import os

absolute_path = os.path.abspath("wallpaper.png")

if not os.path.exists(absolute_path):
    raise FileNotFoundError(f"wallpaper.png not found!")

ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path, 3)
print("wallpaper.png set as current wallpaper")