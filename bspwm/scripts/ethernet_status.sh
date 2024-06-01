#!/bin/bash

search=$(hostname -I | sed s/\ /\\n/g | grep -v 172 | xargs )

ip_addresses=$(/usr/sbin/ifconfig | grep -B1 "$search" | grep -w inet | awk '{print $2}')

if [ -z "$search" ];then
    echo %{F#2495e7}󰌙    %{F#ffffff} "Disconnected"%{u-}
else 
    echo %{F#2495e7}󰈀    %{F#ffffff} "$ip_addresses"%{u-}
fi
 


