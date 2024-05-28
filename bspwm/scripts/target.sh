#!/bin/bash
#
ip_address=$(awk '{print $1}' /home/angel/.config/bin/target)
machine_name=$(awk '{print $2}' /home/angel/.config/bin/target)


if [ $ip_address ] && [ $machine_name ]; then
     
    ping=$( (ping -c 1 $ip_address) 2>/dev/null )
 ping_output=$?
  if [ $ping_output -eq 0  ]; then 
    echo "%{F#e51d0b}󰯐  %{F#ffffff}$ip_address%{u-} - $machine_name"
  else
    echo "%{F#e51d0b}󱐝 %{u-}%{F#ffffff} No target"
  fi

else
    echo "%{F#e51d0b}󱐝 %{u-}%{F#ffffff} No target"
fi






