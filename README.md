# signal-strength
Prints out the signal strength of a specific WIFI device

##
you should convert to monitor mode 

     sudo ifconfig wlx588694f39e8b down
     sudo ip link set wlx588694f39e8b name mon0
     sudo iwconfig mon0 mode monitor
     sudo ifconfig mon0 up
     sudo systemctl restart NetworkManager


## code

    sudo python3 signal-strength.py [interface] [mac]

 
---

