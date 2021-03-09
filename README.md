# VideoEditor
 Short python.exe for editing video with moviepy and tkinter GUI


**Currently the only active file is gui_basics.py**

07/03/21 Update:
New source video is now funcitonal. 
can find a clip and import it.
    Duration,name and initial frame of the clip are displayed on the main window.

09/03/21 Update:
    Current functionality

1.  Main GUI Window
    1. Can upload source video
    2. Tutorial Button - does nothing yet (terminal print)
    3. Can enter export video name details and the export name is displayed
        1. Video Date (default: Todays date)
        2. Athlete name
        3. Session type (default: Flatwater)
    4. New subclip button opens child window new subclip
        - Only opens if user has selected source video clip
    5. Close button
        - Quits application
2. New Subclip Window
    1. Enter Start/end/duration times
        - Cannot exceed the bounds of the source video
    2. Enter subclip name/number
    3. Create subclip
        - Shows start and end frames of the subclip 
        - Prints the subclip details in the window below
    4. Close button
        - Sends user back to the main GUI
    

Subclip list to be added to front page

