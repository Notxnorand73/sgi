import os
import sys
import winreg

extension = '.sgi'
icon_path = 'C:\\Users\\notxn\\commands\\SGI.ico'

if not os.path.isfile(icon_path):
    raise FileNotFoundError(f"Icon file not found: {icon_path}")

try:
    # Step 1: Create a ProgID for the extension
    prog_id = extension[1:].upper() + "_file"

    # Link extension to ProgID
    with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, extension) as ext_key:
        winreg.SetValue(ext_key, "", winreg.REG_SZ, prog_id)

    # Step 2: Set the default icon for the ProgID
    icon_key_path = f"{prog_id}\\DefaultIcon"
    with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, icon_key_path) as icon_key:
        winreg.SetValue(icon_key, "", winreg.REG_SZ, icon_path)

    print(f"Icon for '{extension}' set to '{icon_path}'")
    print("You may need to restart Explorer or log out/in to see changes.")

except PermissionError:
    print("Permission denied. Please run this script as Administrator.")
except Exception as e:
    print(f"Error: {e}")
