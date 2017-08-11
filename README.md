# pythonFinal

If using Raspberry Pi 2 and the Pi Camera this file makes work with the pi camera trivial.  There is a menu of options to select from.  The Program was writen for Python 2.

### User Menu

Options                         | Input Type  | Range                 | Action 
|-------------------------------|-------------|-----------------------|--------------------------------------------------------------------
|0. exit                        | n/a         | n/a                   | Exit the program
|1. Preview                     | n/a         | n/a                   | Preview with that camera
|2. Preview Effect              | n/a         | n/a                   | Cycle through the effcts
|3. Preview Contrast            | n/a         | n/a                   | Cycle through the contrast range
|4. Preview Brightness          | n/a         | n/a                   | Cycle through the brightness range
|5. Print Settings              | n/a         | n/a                   | Print current settings
|6. Set Alpha                   | integer     | 0 - 255               | Set alpha level
|7. Set Brightness              | integer     | 1 - 100               | Set brighness level
|8. Set Contrast                | integer     | 1 - 100               | Set contrast level
|9. Set Text Size               | integer     | 6 - 160               | Set text size
|10. Set Rotation               | integer     | 0, 90, 180, 270       | Set rotation of camera
|11. Set Sleep                  | integer     | .1 - 10 in milisecond | Set sleep length
|12. Set Effect                 | string      | effect name           | Set effect
|13. Set Save Directory         | string      | n/a                   | Set the save directory. Will create directory if one doesn't exist.
|14. Take Picture               | n/a         | n/a                   | Take a picture
|15. Take Pictures              | integer     | n/a                   | Take several time laps pictures 
|16. Take Recording             | n/a         | n/a                   | Take a recording
|17. Take Picture with Caption  | string      | n/a                   | Take a picture and annotate text
|18. Print OS information       | n/a         | n/a                   | Print system information.

### Constants

Value           | Default
----------------|---------
Sleep           | 10
Rotation        | 0
Alpha           | 255
Save Directory  | /home/pi/pics
Brightness      | 50
Contrast        | 50
Text Size       | 32
Effect          | none

