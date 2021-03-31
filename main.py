import os 
import random
import argparse
import json5 as json

terminal_profile_name = "Ubuntu"
image_storage_loc = "/mnt/c/Users/Aidan/Documents/cluster"
"""
 Terminal profile setting location can be obtained by clicking copy path on file(When file is opened in VS code)
  - To open settings file,  click settings in new terminal 
"""
terminal_profile_settings_loc = "/mnt/c/Users/Aidan/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--random', dest='random', action='store_true', help="Get a random image from location folder.")
    parser.add_argument('-p', '--path', dest='path', help='The path to the image. Make this a directory if using -r')
    args = parser.parse_args()

    img = args.path
    if args.random:
        img = getrandom(args.path)
    profile_data = None

    with open(terminal_profile_settings_loc) as read_profile_data:
        profile_data = json.load(read_profile_data)
        for profile_info in profile_data["profiles"]["list"]:
            if profile_info["name"] == terminal_profile_name:
                profile_info["backgroundImage"] = img

    with open(terminal_profile_settings_loc, 'w') as write_profile:
        json.dump(profile_data, write_profile, quote_keys=True, indent=4,)


def getrandom(path): 
    pattern = ('.jpg', '.jpeg', '.gif', '.png')

    items = []

    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(pattern):
                items.append(os.path.join(root, filename))

    random_slot = random.randint(0, len(items)-1)
    random_image = items[random_slot]


if __name__ == '__main__':
    main()

