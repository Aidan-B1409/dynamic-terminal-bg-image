# Display Dynamic Terminal Background Image (Windows) 

# Pre-requisties

1. Install new Terminal on windows machine

2. open ```profiles.json``` by clicking settings icon in terminal window

3. Add a key ```backgroundImage``` in profiles array @t specific window section.

    ```
    {
            "name": "Ibrahim Sha Personal",
            "commandline": "cmd.exe",
            "hidden": false,
            "startingDirectory": "C:/",
            "backgroundImage": "***Loc****",
            "backgroundImageStretchMode": "fill"
    }

    ```

4. Python2/3 should be installed in your machine.

5. Run ```python main.py``` (before running script, validate your profile.json)

Note: Validate the profiles.json content by using (https://jsonlint.com/) and remove the unwanted escape characters.
