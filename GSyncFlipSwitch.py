#!/usr/bin/env python3

import sys
import subprocess


def main(argv):
    current_metamode = subprocess.run(["nvidia-settings", "-q", "CurrentMetaMode"], universal_newlines=True,
                                      stdout=subprocess.PIPE)
    current_metamode = current_metamode.stdout.replace('\n', '').replace('  ', ' ').strip()

    gsync_state = determine_gsync_state(current_metamode)
    flip_gsync_mode(gsync_state, current_metamode)

    exit(0)


def determine_gsync_state(current_metamode):
    if "Attribute \'CurrentMetaMode\'" in current_metamode:
        if 'AllowGSYNC=Off' in current_metamode:
            return "OFF"
        else:
            # Assume GSync is on because nvidia-settings -q CurrentMetaMode
            # returned a metamode, and when GSync is on AllowGSYNC is not
            # part of the returned string. Perhaps a better way to determine
            # if GSync is enabled is needed?
            return "ON"
    else:
        # Unknown GSync state
        exit(1)


def flip_gsync_mode(gsync_state, current_metamode):
    nvidia_command = 'nvidia-settings --assign CurrentMetaMode='
    current_metamode = current_metamode.split("::", 1)[1].strip()

    if gsync_state == "OFF":
        nvidia_command = ''.join([nvidia_command, '"', current_metamode.replace("AllowGSYNC=Off,", "AllowGSYNC=On,"), '"'])
    elif gsync_state == "ON":
        nvidia_command = ''.join([nvidia_command, '"', current_metamode.replace("{", "{AllowGSYNC=Off, "), '"'])
    else:
        # How would we even get here
        exit(1)

    subprocess.run(nvidia_command, shell=True, check=True)


if __name__ == '__main__':
    main(sys.argv)