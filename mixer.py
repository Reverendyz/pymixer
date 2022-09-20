from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

MAX = 5.0
MIN = -60

devices = AudioUtilities.GetAllSessions()
for dev in devices:
    print(dev)
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# volume.GetVolumeRange()



# volume.SetMasterVolumeLevel(5, None)