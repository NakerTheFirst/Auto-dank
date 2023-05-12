# Auto-dank
Discord Dank Memer bot automated command posting via Python script

## Purpose
The main goal was to experiment with automation and Discord API. The ToS do not allow use of user's personal token, so the automation process relies on accessing the Discord's interface "by hand" via `pyautogui` library. In other words - writing commands and navigating Discord is automated, so as to maximuse the income of virutal currency the Dank Memer bot introduces. 

## Usage
The script requires the user to have Dicord open. 
1. Modify the x, y coordinates of the active `DISCORD_WINDOW_COORDINATES` key, to click on the Discord interface without interacting with any messages or pictures
2. Change the name of `CHANNEL_NAME` constant to match the text channel you wish to run commands on
3. Run the programme in IDE of choice

Additionally, you could store the script locally and make a .bat script to run it from your desktop. 

## Commands used
- `/dig`
- `/hunt`
- `/fish`
- `/beg`

Additional commands can be added by modifying the `COMMANDS` dictionary. Keep in mind the first 3 commands require the user to have the shovel, hunting rifle and fishing rod items respectively. <br>
Keep in mind commands might have different cooldown timers depending on the user having default or a premium type of account. Right now the code calls the commands every 10s maximise income and to prevent discrepencies. 
