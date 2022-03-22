#!/usr/bin/env python3
import os
import PyInstaller.__main__

if __name__ == "__main__":
    PyInstaller.__main__.run([
        "run_game.py",
        "--onefile",
        "--onedir",
        "--noconsole",
        "--noconfirm",
        "--name=Trevor",
        f"--add-data=.{os.path.sep}assets{os.pathsep}assets{os.path.sep}"
    ])
