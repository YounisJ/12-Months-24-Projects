import subprocess
import pyfiglet

banner = pyfiglet.figlet_format("Auto Recon !!!")
print(banner)

url = input("\nEnter Website Url Please :")

cmd = subprocess.run(f"sublist3r -d {url}", shell=True, capture_output=True, text=True)
print(cmd.stdout)