from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

MAX = 5.0
MIN = -60

def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "chrome.exe":
            print(f"volume.GetMasterVolume(): {volume.GetMasterVolume()} and {session.Process.name()}")
            volume.SetMasterVolume(1, None)       


if __name__ == "__main__":
    main()