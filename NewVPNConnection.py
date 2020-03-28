import os
import time

path_to_protonVPN = r"C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.exe"

while True:
    os.startfile(path_to_protonVPN)
    time.sleep(300)
    os.system("TASKKILL /F /IM ProtonVPN.exe")
    os.system("TASKKILL /F /IM ProtonVPN.UpdateService.exe")
    os.system("TASKKILL /F /IM ProtonVPNService.exe")
    os.system("TASKKILL /F /IM openvpn.exe")
