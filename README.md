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

In the directory is a led-randomness.service, to add that:
1. Modify the path if needed (by default it assumes ~/git/candy-led/, be aware you might want to change that for security )
2. sudo systemctl enable ~/git/candy-led/led-randomness.service
3. Enjoy! 

This is actually quite useful to tell when it goes to sleep, or if a machine has turned off at a glance. 
