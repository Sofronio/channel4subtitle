# channel4subtitle
Support Channel4 subtitle download and convert

# c4d.py
c4d.py could download subtitles and thumbnails using Channel4's XML file. You can find it here, like this:
If you're browsing
  http://www.channel4.com/programmes/jamies-30-minute-meals
you can find the xml file here
  www.channel4.com/programmes/service/brand/jamies-30-minute-meals.xml
which contains all the infomation you'll need.

#c4ass.py
c4ass.py could convert Channel4's plain text to ASS subtitle. Or, if you look into the file, it's a SAMI or SMI file.

# Note c4d.py
This version requires you to manually download the program XML file.

# Note c4ass.py
This version requires you to manually replace all the <br> label to <br />
As I use XML structure for subtilte processing, the <br> label is not a valid XML label.

# Usage
c4d.py channel4program.xml
c4ass.py channel4subtitle.xml
