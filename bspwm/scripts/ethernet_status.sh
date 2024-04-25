echo "%{F#2495e7}󰈀 %{F#ffffff}$(/usr/sbin/ifconfig enp9s0 | grep "inet " | awk '{print $2}')%{u-}"
