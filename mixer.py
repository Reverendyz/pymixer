from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import tkinter as tk
from tkinter import StringVar, ttk, DoubleVar
from random import randint

INTERVAL = 2000  # 2 seconds

class WindowsAudioProcess:
    def __init__(self, name, frame) -> None:
        self.name = name
        self.volume = DoubleVar()
        self.frame = frame

    def create_panel(self, x: int):
        name = ttk.Label(self.frame, text=self.name,foreground='white', background='black')
        name.grid(row=2, column=x)

        scale = ttk.Scale(self.frame, from_=1, to=0, orient='vertical', variable=self.volume)
        scale.grid(row=3, column=x, sticky="NEWS")

        value = ttk.Label(self.frame, text=f"{self.volume.get():.2f}", foreground="red", font=("Arial", 15))
        value.grid(row=4, column=x)

    def set_volume(self, volume: float):
        self.volume = volume

    def get_volume(self) -> float:
        return self.volume


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

        self.random = ttk.Label(
            self.mainframe, text="", background='black', foreground='white', font=("Arial", 30))
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
            self.processes.append(WindowsAudioProcess(
                process.split('.')[0], self.mainframe))
        return self.processes

    def get_process_names(self) -> list:
        process_names = []
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name():
                process_names.append(session.Process.name())
        return process_names


if __name__ == "__main__":
    VolumeControllerApp()

#     volume = session._ctl.QueryInterface(ISimpleAudioVolume)
#         f"volume.GetMasterVolume(): {volume.GetMasterVolume()} and {type(session.Process.name())}")
#     volume.SetMasterVolume(1, None)
