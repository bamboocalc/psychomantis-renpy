init python:
    import os
    import platform
    
    def is_game_installed(game_name):
        # Define common RenPy installation locations
        paths_to_check = []

        # Windows
        if os.name == 'nt' or platform.system() == 'Windows':
            paths_to_check = [
                os.path.expandvars(r'%APPDATA%\RenPy'),
                os.path.expandvars(r'%LOCALAPPDATA%\RenPy')
            ]
        # macOS
        elif platform.system() == 'Darwin':
            paths_to_check = [
                os.path.expanduser('~/Library/RenPy')
            ]
        # Linux
        elif platform.system() == 'Linux':
            paths_to_check = [
                os.path.expanduser('~/.renpy')
            ]

        # Check if the game directory exists for any of these paths
        for path in paths_to_check:
            if os.path.exists(path):
                for directory in os.listdir(path):
                    if game_name in directory:
                        return True
        return False

define narration = Character(None, what_xalign=0.5, what_textalign=0.5, what_color="#FFFFFF")


label start:
    if is_game_installed("TaxHeaven3000"):
        narration "Wow, you must really like doing your 2022 taxes."
    else:
        narration "Hi."