import os
import subprocess
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter

# ASCII Art for startup
ASCII_ART = """  
⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⡞⡀⣤⣬⣴⠀⠀⢳⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡇⠀⢸⣿⠿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀
⠀⠀⢠⡾⣫⣿⣻⣿⣽⣿⡇⠀⠈⢿⣧⡝⠟⠀⠀⢸⣿⣿⣿⣿⣿⣟⢷⣄⠀⠀
⠀⢠⣯⡾⢿⣿⣿⡿⣿⣿⣿⣆⣠⣶⣿⣿⣷⣄⣰⣿⣿⣿⣿⣿⣿⣿⢷⣽⣄⠀
⢠⣿⢋⠴⠋⣽⠋⡸⢱⣯⡿⣿⠏⣡⣿⣽⡏⠹⣿⣿⣿⡎⢣⠙⢿⡙⠳⡙⢿⠄
⣰⢣⣃⠀⠊⠀⠀⠁⠘⠏⠁⠁⠸⣶⣿⡿⢿⡄⠈⠀⠁⠃⠈⠂⠀⠑⠠⣈⡈⣧
⡏⡘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡥⢄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⢸
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢨
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡳⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# Terminal color themes
COLORS = {
    "default": "",
    "red": "\033[91m",
    "green": "\033[92m",
    "cyan": "\033[96m",
    "blue": "\033[94m",
}

class NyxShell:
    def __init__(self):
        self.session = PromptSession(
            history=FileHistory(".nyx_history"),
            auto_suggest=AutoSuggestFromHistory(),
            completer=WordCompleter(["exit", "clear", "whoami", "theme"])
        )
        self.color = COLORS["default"]

    def run(self):
        print(self.color + ASCII_ART + "\033[0m")  # Display ASCII art on startup

        while True:
            try:
                command = self.session.prompt("nyx> ").strip()
                if not command:
                    continue

                args = command.split()
                cmd = args[0]

                if cmd == "exit":
                    print("Exiting...")
                    break
                elif cmd == "clear":
                    os.system("clear")
                elif cmd == "whoami":
                    print(os.getlogin())
                elif cmd == "theme" and len(args) > 1:
                    self.set_theme(args[1])
                else:
                    self.execute_command(command)

            except KeyboardInterrupt:
                print("\nUse 'exit' to quit.")
            except Exception as e:
                print(f"Error: {e}")

    def set_theme(self, color):
        """Change terminal theme dynamically."""
        if color in COLORS:
            self.color = COLORS[color]
            print(f"Theme changed to {color}.")
        else:
            print("Available themes: default, red, green, cyan, blue.")

    def execute_command(self, command):
        """Execute any system command (including sudo, reboot, etc.)."""
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")

# Run the shell
if __name__ == "__main__":
    NyxShell().run()
