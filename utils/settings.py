# settings functions
from .utils import Utils


class Settings():
    utils = Utils()

    # change focus or break time
    def timeChange(self, focus=True, error: str = '') -> None:
        from .pomodoro import Pomodoro

        suffix = "focus" if focus else "break"
        data = self.utils.fetchData('settings')
        timeStr = self.timeHeader(suffix, data)
        print(timeStr)
        print(f"\n\033[38;5;9m {error} \033[m")
        userTime = input(
            "\033[38;5;232m (mm:ss) \N{Black Right-Pointing Triangle}\033[m ").strip()
        if userTime == "q":
            self.utils.quitApp()
        elif userTime == 'b':
            Pomodoro().settings()

        if not (userTime[:2].isnumeric() and userTime[3:].isnumeric() and ':' in userTime):
            self.timeChange('Invalid time format.')
        else:
            userTime = userTime.split(':')
            minute = int(userTime[0])
            seconds = int(userTime[1])
            totalSeconds = (minute*60)+seconds
            data[f"{suffix}Time"] = totalSeconds
            update, e = self.utils.updateData(data, 'settings')
            if update:
                print(self.timeHeader(suffix, data))
                update = input(
                    "\nPress enter to continue.\n\033[38;5;232mq: quit \033[m")
                if update == 'q':
                    self.utils.quitApp()
                else:
                    Pomodoro().main()
            else:
                print(f"There is an error -> {e}")

    def timeHeader(self, suffix: str, data: dict) -> str:
        self.utils.header("Settings")
        time = data[f'{suffix}Time']
        timeStr = self.utils.pomodoroTime(time)
        return f"Your current {suffix} time ->\n\n{timeStr}"
