#!/usr/bin/env python3

import subprocess
import shlex


def main():
    current_metamode = get_metamode()
    gsync_state = determine_gsync_state(current_metamode)
    flip_gsync_mode(gsync_state, current_metamode)
    exit(0)


def get_metamode():
    current_metamode = subprocess.run(["nvidia-settings", "-q", "CurrentMetaMode"], universal_newlines=True,
                                      stdout=subprocess.PIPE)
    return current_metamode.stdout.replace('\n', '').replace('  ', ' ').strip()


def determine_gsync_state(current_metamode):
    """
    Returns if gsync is on or off for the monitor.
    :param current_metamode:
    :return:

    >>> determine_gsync_state('Attribute \\'CurrentMetaMode\\' (pc:1.0): id=50, switchable=no, source=nv-control :: DPY-4: 2560x1440_120 @2560x1440 +0+0 {ViewPortIn=2560x1440, ViewPortOut=2560x1440+0+0}')
    'ON'
    >>> determine_gsync_state('Attribute \\'CurrentMetaMode\\' (pc:1.0): id=50, switchable=no, source=nv-control :: DPY-4: 2560x1440_120 @2560x1440 +0+0 {AllowGSYNC=Off, ViewPortIn=2560x1440, ViewPortOut=2560x1440+0+0}')
    'OFF'
    """
    if "Attribute \'CurrentMetaMode\'" in current_metamode:
        if 'AllowGSYNC=Off' in current_metamode:
            return "OFF"
        else:
            return "ON"
    else:
        exit(1)


def flip_gsync_mode(gsync_state, current_metamode):
    nvidia_command = 'nvidia-settings --assign CurrentMetaMode='
    current_metamode = current_metamode.split("::", 1)[1].strip()
    if gsync_state == "OFF":
        nvidia_command = ''.join([nvidia_command, '"', current_metamode.replace("AllowGSYNC=Off,", "AllowGSYNC=On,"), '"'])
    elif gsync_state == "ON":
        nvidia_command = ''.join([nvidia_command, '"', current_metamode.replace("{", "{AllowGSYNC=Off, "), '"'])
    else:
        exit(1)
    nvidia_command = shlex.split(nvidia_command)
    subprocess.run(nvidia_command, universal_newlines=True, stdout=subprocess.PIPE)


if __name__ == '__main__':
    main()
