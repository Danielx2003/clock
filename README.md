# clock
a digital clock that shows timezones and can be changed when buttons are pressed

When the program opens it starts with your own timezone, for me that is GMT.
There are 4 different buttons to press that change the clock from CEST, EST, CST and GMT.
When you press one button it changes the clock to the correctly displayed time in digital 24 hr clock form (HRS,MINS,SECS).
The issue is when you press a button to change time zone, and then you press another button, the clock flickers between the 2 time zones as both the functions are being called, which at the moment i can't fix.
I added a back button in the hopes that when you press the back button, it was supposed to take you out of the function, then you can press a new button,but the back button doesn't work cause i don't know how to get out of the function.
Then I added a function so when you press the back button the program completely restarts so you can choose a new timezone, however the program only closes and doesn't reopen.


