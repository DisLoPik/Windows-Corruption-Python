# funny.py

**⚠️ WARNING: This script is destructive and intended for educational or testing purposes only. Do not run it on a production or personal system unless you are fully aware of the consequences and have backups.**

## Description

`funny.py` is a Windows-only Python script that:

- Creates the file: `C:\Windows\System32\config\OSDATA` with 120 KB of random binary data. (This file is unused but crashes windows if there is invalid data)
- Forces an immediate system reboot (`shutdown /r /t 0`).

The target file resides in the Windows registry hive directory (`config`). Corrupting or overwriting this file can render the operating system unbootable and cause permanent data loss. The script is intentionally simple and demonstrates the use of administrative privilege escalation and low-level file operations.

## Requirements

- **Windows operating system** (the script checks `os.name` and exits on non‑Windows platforms).
- **Python 3** (with the standard library modules `ctypes`, `os`, and `sys`).
- **Administrator privileges** – the script automatically requests elevation via UAC if not already running as admin.

## Usage

1. Save the script as `funny.py`.
2. Open a command prompt or terminal.
3. Run the script:

   ```bash
   python funny.py
   ```
4. If not already elevated, a UAC prompt will appear. Click Yes to grant administrator rights.
5. The script writes random data to the target file and then immediately reboots the computer.
-# Note: There is no confirmation prompt. Execution leads directly to system reboot.

# How It Works
1. Administrator Check – `is_admin()` uses `ctypes.windll.shell32.IsUserAnAdmin()` to verify if the process has admin rights.
2. Elevation – If not admin, `elevate()` relaunches the script with the runas verb using ShellExecuteW, passing the original command‑line arguments.
3. File Overwrite – `os.urandom(FILE_SIZE)` generates 120 KB of cryptographically random bytes, which are written to `TARGET_FILE`.
4. Reboot – After writing, the script calls `os.system("shutdown /r /t 0")` to force an immediate restart.

# Warning
- Data loss: Overwriting OSDATA corrupts the registry hive, making Windows unable to boot. You will likely need to reinstall the operating system or restore from a backup.
- No recovery: The script does not create a backup or prompt for confirmation.
- Use at your own risk: The author assumes no liability for any damage caused by this script.

If you intend to test this script, do so only in a virtual machine or on a disposable system with no important data.
