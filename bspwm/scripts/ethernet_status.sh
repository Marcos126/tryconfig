#!/bin/bash

ifs=(usb0 eth0)
ip_addresses=()

function usb(){
    (/usr/sbin/ifconfig $is) &>/dev/null
    if [ $? -eq 0 ];then
        ip=$(/usr/sbin/ifconfig $is | grep "inet " | awk '{print $2}')
        if [ -n "$ip" ]; then
            ip_addresses+=("$ip")
        fi
    fi
}

for is in ${ifs[@]}; do
    usb $is
done

if [ ${#ip_addresses} -eq 0 ] ; then
    echo %{F#2495e7}󰌙    %{F#ffffff} "Disconnected"%{u-}
else 
    echo %{F#2495e7}󰈀    %{F#ffffff} "$ip_addresses"%{u-}
fi
