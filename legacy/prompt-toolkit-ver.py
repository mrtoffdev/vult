
# Prompt Toolkit
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import button_dialog

import subprocess
import os

if __name__ == '__main__':
    # Identifiers
    DEVICE_DIR = ""
    DEVICE_ID = ""

    file_list = subprocess.check_output(['ls']).decode('ASCII')
    dialogue = "Sankaku Compression Script\n\n" + \
               "Files in Directory:\n" + \
               file_list

    os.system('clear')
    print(dialogue)

    fl_comp = WordCompleter(file_list.split('\n'))
    selection = prompt('Select File: ', completer=fl_comp)

    encoder = button_dialog(
        text='Select Video Encoder',
        buttons=[
            ('yeps', True),
            ('nopes', False)
        ]
    ).run()

    # if selection != '':
    # mt_encode()
    # else:
    # print("Invalid Selection")
