import time

from utils import Utils


class Pomodoro():
    utils = Utils()

    # pomodoro tick
    def tick(self, seconds, focus) -> None:
        self.utils.header()
        focusText = "\033[1m\033[38;5;117m\N{Black Right-Pointing Triangle} Focus!! \033[m\n"
        breakText = "\033[1m\033[38;5;117m\N{Black Right-Pointing Triangle} Ahh... Break time!! \033[m\n"
        quoteText = focusText if focus else breakText
        print(quoteText)
        print(self.utils.pomodoroTime(seconds))
        print('\n\n')
        if seconds >= 1:
            seconds -= 1
            time.sleep(1)
            self.tick(seconds, focus)
        else:
            # it's time to change focus
            focus = False if focus else True
            # notify me
            self.utils.notification(not focus)
            self.main(focus=focus)

    # main screen
    def main(self, focus=True) -> None:
        self.utils.header()

        # initial time of focus and break
        pomodoroSeconds = self.utils.fetchTime(focus)

        # show focus or break quote
        focusText = "\033[38;5;10m\N{Black Right-Pointing Triangle} It's time to focus. \033[m\n"
        breakText = "\033[38;5;10m\N{Black Right-Pointing Triangle} It's time to take rest. \033[m\n"
        textShow = focusText if focus else breakText
        print(textShow)

        print(f"{self.utils.pomodoroTime(pomodoroSeconds)}\n\n")
        print(
            "Press enter to start!\n\033[38;5;232mq: quit; s: settings\033[m")
        option = input().strip().lower()

        if option == 'q':
            self.utils.quitApp()
        if option == 's':
            self.settings()

        if option:
            self.main()
        else:
            self.tick(pomodoroSeconds, focus)

    # settings
    def settings(self):
        from settings import Settings

        self.utils.header("Settings")
        options = '''
\033[1m\033[38;5;173m Choose-\033[m
    1. Change focus time
    2. Change break time
    
    \033[38;5;232mb: back
    q: quit\033[m
        '''
        print(options)
        option = input("\N{Black Right-Pointing Triangle} ")
        if option == '1':
            Settings().timeChange(True)
        elif option == '2':
            Settings().timeChange(False)
        elif option == 'q':
            self.utils.quitApp()
        elif option == 'b':
            self.main()
        else:
            self.settings()
