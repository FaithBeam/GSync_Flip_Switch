#!/bin/bash

determine_gsync_state() {
    CURRENTMETAMODE="$(nvidia-settings -q CurrentMetaMode)"
    
    if [[ "${CURRENTMETAMODE}" == *"AllowGSYNC=Off"* ]]; then
        GSYNCSTATE="OFF"
    else
        GSYNCSTATE="ON"
    fi
}

flip_gsync_mode() {
    CURRENTMETAMODE="${CURRENTMETAMODE##*:: }"
    NVIDIACOMMAND="nvidia-settings --assign CurrentMetaMode=\""

    if [[ "${GSYNCSTATE}" == "OFF" ]]; then
        NVIDIACOMMAND+=${CURRENTMETAMODE//{AllowGSYNC=Off,/{AllowGSYNC=On, }
    else
        NVIDIACOMMAND+=${CURRENTMETAMODE//{/{AllowGSYNC=Off, }
    fi

    NVIDIACOMMAND+='"'
    eval "$NVIDIACOMMAND"
}

determine_gsync_state
flip_gsync_mode
