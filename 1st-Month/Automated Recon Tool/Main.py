import subprocess
import pyfiglet
import os
import re

banner = pyfiglet.figlet_format("Auto Recon !!!")
print(banner)

# Collecting Subdomains Using sublister

url = input("\nEnter Website URL Please: ").strip()

output_dir = f"Auto_Recon_For_{url}"
os.makedirs(output_dir, exist_ok=True)

print("Wait ... Running Sublist3r")

cmdSublister = subprocess.run(["sublist3r", "-d", url], capture_output=True, text=True)
clean_output = re.sub(r"\x1B\[[0-9;]*[mK]", "", cmdSublister.stdout)
subdomains = re.findall(rf"[a-zA-Z0-9.-]+\.{url}", clean_output)
output_file = os.path.join(output_dir, f'SubDomainsfor_{url}.txt')

with open(output_file, 'w') as f:
    f.write("\n".join(subdomains))

print(f"Done! Subdomains saved in: \n {output_file}")

# Checking for open ports

# cmdNmap = subprocess.run(["nmap", url], capture_output=True, text=True)
