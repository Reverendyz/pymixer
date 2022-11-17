from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import tkinter as tk
from tkinter import StringVar, ttk, DoubleVar
from random import randint

INTERVAL = 2000  # 2 seconds

class WindowsAudioProcess:
    def __init__(self, name, frame) -> None:
        self.name = name
        self.volume = 1
        self.frame = frame

    def create_panel(self, x: int):
        name = ttk.Label(self.frame, text=self.name,foreground='white', background='black')
        name.grid(row=2, column=x)

        process_volume = DoubleVar(value=self.volume)
        scale = ttk.Scale(self.frame, from_=1, to=0, orient='vertical', variable=process_volume, command=lambda x: self.set_volume(process_volume.get()))
        scale.grid(row=3, column=x, sticky="NEWS")

        value = ttk.Label(self.frame, text=f"{self.volume:.2f}", foreground="red", font=("Arial", 15))
        value.grid(row=4, column=x)

    def set_volume(self, volume):
        self.volume = volume
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == self.name+".exe":
                volume.SetMasterVolume(self.volume, None)

class VolumeControllerApp:
    def __init__(self) -> None:
        self.processes = []
        self.root = tk.Tk()
        self.root.geometry("720x480")
        self.root.resizable(False, False)
        self.root.title("Windows Volume Controller")

        self.mainframe = tk.Frame(self.root, background="black")
        self.mainframe.pack(fill='both', expand=True)
        self.process_names = self.create_process_list()

        self.random = ttk.Label(self.mainframe, text="", background='black', foreground='white', font=("Arial", 30))
        self.random.grid(row=0, column=0, sticky="NEWS")

        self.update()

        self.root.mainloop()
        return

    def update(self):
        self.random.config(text=randint(0, 100))
        self.create_panel()
        self.root.after(INTERVAL, self.update)

    def create_panel(self):
        for column, process in enumerate(self.processes):
            process.create_panel(column)

    def create_process_list(self) -> None:
        for process in self.get_process_names():
            self.processes.append(WindowsAudioProcess(process.split('.')[0], self.mainframe))
        return self.processes

    def get_process_names(self) -> list:
        process_names = []
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name():
                process_names.append(session.Process.name())
        return process_names

    def get_sessions(self) -> list:
        sessions = AudioUtilities.GetAllSessions()
        return sessions


if __name__ == "__main__":
    VolumeControllerApp()