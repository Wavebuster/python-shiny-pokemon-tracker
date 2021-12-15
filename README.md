# python-shiny-pokemon-tracker
Welcome to the Python Shiny Pokemon Tracker version 1.0!

This file will explain the functionalities of the program as well as provide instructions for setup of the program.

I wrote this program in Python 3.8.5 so I would recommend having that version or higher of Python installed to run this.

!!If you need help installing Python reference https://www.python.org for further instruction!!

To begin using this program, you will first have to edit a couple lines within one of the included Python files. Open shiny_tracker_methods.py in any text editor. Notepad will work just fine. In that file, right beneath the line saying "import csv" you will see a comment explaining to enter file paths. You will need to enter the file paths for the data.csv file included after file_location and the location of the pokemon_names.txt file after names. The file path will go in the quotes. You should be able to copy the path directly from File Explorer in Windows, Finder in Mac or Files in Linux. Paste that inside the quotes, followed by the appropriate file's name.

After this step your files should be ready to go. Just run the shiny_pkmn_tracker.py file, and select the appropriate options from the menu to interact with it.

If you get a FileNotFoundError, the most likely cause is that the file paths in the shiny_tracker_methods.py file are not correct.

If, for whatever reason, you need to use option 4 to reset the CSV file, you will need to do just a couple more steps to re-ready that file for the program. After running command 4 you will open the CSV file in a text editor. From there, you will first find and replace quotation marks " with nothing. You will then find and replace '\n' (no quotes) with nothing. These two find and replace steps will re-ready the file for the program.
