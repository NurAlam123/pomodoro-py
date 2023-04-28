from datetime import datetime
import json


# utils class
class Utils():
    # clear the terminal
    def clear(self) -> None:
        print('\033c')

    # exit from the app
    def quitApp(self):
        self.clear()
        print("\n\n")
        print("\033[1m Thanks for using me! :p")
        print('\n\n\n\n')
        exit()

    # get clock emoji
    def getClockEmoji(self) -> str:
        # current hour and minute
        hour = datetime.now().hour
        minute = datetime.now().minute

        oclock = ["\U0001f55b", "\U0001f550", "\U0001f551", "\U0001f552", "\U0001f553", "\U0001f554",
                  "\U0001f555", "\U0001f556", "\U0001f557", "\U0001f558", "\U0001f559", "\U0001f55a"]
        thirty = ["\U0001f567", "\U0001f55c", "\U0001f55d", "\U0001f55e", "\U0001f55f", "\U0001f560",
                  "\U0001f561", "\U0001f562", "\U0001f563", "\U0001f564", "\U0001f565", "\U0001f566"]

        hour = hour-12 if hour > 0 else 0
        emoji = oclock[hour] if minute < 30 else thirty[hour]
        return emoji

    # show current time
    def currentTime(self) -> str:
        emoji = self.getClockEmoji()
        now = datetime.now().strftime(
            f"{emoji}\033[1m %H:%M \033[m \n\n\U0001f4c5 %B %d, %Y")
        return now

    # header of every function :p
    def header(self, title: str = '') -> None:
        self.clear()
        title = f"- {title}" if title else title
        print(f"\033[1m\033[38;5;4m \N{Watch} Pomodoro {title}\033[m")
        print("\n-------------------")
        print(self.currentTime())
        print("-------------------\n")

    # fetch time from json
    def fetchTime(self, focus) -> int:
        with open("./assets/pomodoro.json", 'r') as dataFile:
            data = json.loads(dataFile.read())
            settingsData = data["settings"]
            pomodoroTime = settingsData["focusTime"] if focus else settingsData["breakTime"]
            dataFile.close()
            return pomodoroTime

    # fetch data
    def fetchData(self, option: str = None) -> dict:
        with open("./assets/pomodoro.json", 'r') as dataFile:
            data = json.loads(dataFile.read())
            dataFile.close()
        return data if not option else data[option]

    # update data
    def updateData(self, newData: dict, option) -> bool:
        oldData = self.fetchData()
        with open("./assets/pomodoro.json", 'w') as dataFile:
            try:
                oldData[option] = newData
                data = json.dumps(oldData, indent=4)
                dataFile.write(data)
                dataFile.close()
                return oldData, None
            except Exception as e:
                return oldData, e

    # convert and format time
    def pomodoroTime(self, seconds) -> str:
        pomodoroSeconds = seconds
        minute = int(pomodoroSeconds/60)
        minute = f"0{minute}" if minute < 10 else str(minute)
        seconds = int(pomodoroSeconds % 60)
        seconds = f"0{seconds}" if seconds < 10 else str(seconds)
        pomodoroTimeStr = f"\033[38;5;255m\033[1m\N{Stopwatch} \033[38;5;9m\033[1m {minute}:{seconds} \033[m"
        return pomodoroTimeStr

    # notification
    def notification(self, focus):
        from notifypy import Notify

        focusText = "Focus time is over!\nNow, it's time to take rest."
        breakText = "Break time over.\nLet's focus again!"
        text = focusText if focus else breakText

        notify = Notify()
        notify.title = "Time over!"
        notify.message = text
        notify.audio = './assets/ting_sound.wav'
        notify.icon = './assets/pomodoro_icon.png'
        notify.send()
