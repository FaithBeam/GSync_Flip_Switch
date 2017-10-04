#!/bin/bash

determine_gsync_state() {
    CURRENTMETAMODE="$(nvidia-settings -q CurrentMetaMode)"
    
    if [[ "${CURRENTMETAMODE}" == *"Attribute 'CurrentMetaMode'"* ]]; then
        if [[ "${CURRENTMETAMODE}" == *"AllowGSYNC=Off"* ]]; then
            GSYNCSTATE="OFF"
        else
            # Assume GSync is on because nvidia-settings -q CurrentMetaMode
            # returned a metamode, and when GSync is on AllowGSYNC is not
            # part of the returned string. Perhaps a better way to determine
            # if GSync is enabled is needed?
            GSYNCSTATE="ON"
        fi
    else
        # Unknown GSync state
        exit 1
    fi
    
}

flip_gsync_mode() {
    CURRENTMETAMODE="${CURRENTMETAMODE##*:: }"
    NVIDIACOMMAND="nvidia-settings --assign CurrentMetaMode=\""

    if [[ "${GSYNCSTATE}" == "OFF" ]]; then
        NVIDIACOMMAND+=${CURRENTMETAMODE//{AllowGSYNC=Off,/{AllowGSYNC=On, }
    elif [[ "${GSYNCSTATE}" == "ON" ]]; then
        NVIDIACOMMAND+=${CURRENTMETAMODE//{/{AllowGSYNC=Off, }
    else
        # How would we even get here
        exit 1 
    fi

    NVIDIACOMMAND+='"'
    eval "$NVIDIACOMMAND"
}

determine_gsync_state
flip_gsync_mode
