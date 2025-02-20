import subprocess
import pyfiglet
import os
import re

# Fancy banner
banner = pyfiglet.figlet_format("Auto Recon !!!")
print(banner)

# Get website URL
url = input("\nEnter Website URL Please: ").strip()

# Create a directory for the website's recon results
output_dir = f"Auto_Recon_For_{url}"
os.makedirs(output_dir, exist_ok=True)

print("Wait ... Running Sublist3r")

# Run Sublist3r and capture output
cmd = subprocess.run(["sublist3r", "-d", url], capture_output=True, text=True)

# Remove ANSI color codes (escape sequences)
clean_output = re.sub(r"\x1B\[[0-9;]*[mK]", "", cmd.stdout)

# Extract only subdomains using regex
subdomains = re.findall(rf"[a-zA-Z0-9.-]+\.{url}", clean_output)

# Save only subdomains to a file
output_file = os.path.join(output_dir, f'SubDomainsfor_{url}.txt')

with open(output_file, 'w') as f:
    f.write("\n".join(subdomains))

print(f"Done! Subdomains saved in: \n {output_file}")
