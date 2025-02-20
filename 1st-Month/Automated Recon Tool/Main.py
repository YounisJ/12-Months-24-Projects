import subprocess
import pyfiglet
import os

banner = pyfiglet.figlet_format("Auto Recon !!!")
print(banner)

url = input("\nEnter Website URL Please: ").strip()

output_dir = f"Auto_Recon_For_{url}"
os.makedirs(output_dir, exist_ok=True)

print("Wait ... Running Sublist3r")

cmd = subprocess.run(["sublist3r", "-d", url], capture_output=True, text=True)

# Save the output to a file
output_file = os.path.join(output_dir, f'SubDomainsfor_{url}.txt')

with open(output_file, 'w') as f:
    f.write(cmd.stdout)

print(f"Done! Subdomains saved in: {output_file}")
