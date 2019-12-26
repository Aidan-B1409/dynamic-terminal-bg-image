import os 
import random 
import json 

terminal_profile_name = "Motivational"
image_storage_loc = "***Loc****"
"""
 Terminal profile setting location can be obtained by clicking copy path on file(When file is opened in VS code
  - To open settings file,  click settings in new terminal 
"""
terminal_profile_settings_loc = "***Loc***"

pattern = ('.jpg', '.jpeg', '.gif', '.png')

items = []


for root, dirs, files in os.walk(image_storage_loc):
    for filename in files:
        if filename.endswith(pattern):
            items.append(os.path.join(root, filename))

random_slot = random.randint(0, len(items)-1)
random_image = items[random_slot]
print("Following image going to be updated")
print(random_image)

profile_data = None

with open(terminal_profile_settings_loc) as read_profile_data:
    profile_data = json.load(read_profile_data)
    for profile_info in profile_data["profiles"]:
        if profile_info["name"] == terminal_profile_name:
            profile_info["backgroundImage"] = random_image

with open(terminal_profile_settings_loc, 'w') as write_profile:
    json.dump(profile_data, write_profile)


print("Terminal Profile updated successfuly")

