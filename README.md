# candy-led
Dell Chromebook 11 (candy) activity led control utility

Usage: 
python3 led.py (color) number 

or for continuous randomness:
python3 led.py 

color is one of: 
'red','green','blue','cyan','magenta','yellow','white'
or special: 
'black' - off
'gay' or 'rainbow' - Rainbow colors
'ace' - Ace colors
'nb' - NB colors
'bi' - Bi colors
'<3' - all of the above

In the directory is a led-randomness.service to use it (options in () are optional/depending on how your system is, make sure you know what they do before running them):
1. Modify the USER= and PATH= if needed (by default it assumes ~/git/candy-led/, See note below for security)
2. (sudo) systemctl (--user) enable ~/git/candy-led/led-randomness.service
3. (sudo) systemctl (--user) start ~/git/candy-led/led-randomness.service
4. Enjoy! 

This is actually quite useful to tell when it goes to sleep, or if a machine has turned off at a glance if done globally.

NOTE on permissions/security:
The device (/dev/hidrawX) may or may not have permissions to use it, which gives 2 options:
1: Change the device so that your user can write to it. (You need to make sure it's the right one, and potential security issue depending on how things get setup as hidraw devices as opposed to normal setup. Different distros seem to have different permissions on it.) 
2: Run as sudo/root (This IS a potential security issue.) 

I personally do #1 most of the time, but have done #2, depending on the system. However, I wrote some of it, and know what the rest does, and running a script you don't know what it does is generally a bad idea. Whichever one you choose to do is your choice. I would suggest if you do use #2, to put it in /root and make sure root owns it. (Otherwise modification of the script is trivial as a user.)
