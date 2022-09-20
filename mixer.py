from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

from tkinter import ttk


MAX = 1
MIN = .5

def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "chrome.exe":
            print(f"volume.GetMasterVolume(): {volume.GetMasterVolume()} and {session.Process.name()}")
            volume.SetMasterVolume(MAX, None)       


if __name__ == "__main__":
    main()