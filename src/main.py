import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.shell import NyxShell   # ✅ Ensure this matches `class NyxShell`

if __name__ == "__main__":
    shell = NyxShell()
    shell.run()
