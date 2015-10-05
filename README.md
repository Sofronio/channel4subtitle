# channel4subtitle
Support Channel4 subtitle download and convert<br />

------------------------
v0.1.1 Support `<br>` to `<br />` replacement.<br />
V0.1.0 First version.<br />

## c4d.py
c4d.py could download subtitles and thumbnails using Channel4's XML file. You can find it here, like this:<br />
If you're browsing<br />
  http://www.channel4.com/programmes/jamies-30-minute-meals<br />
you can find the xml file here<br />
  www.channel4.com/programmes/service/brand/jamies-30-minute-meals.xml<br />
which contains all the infomation you'll need.<br />

##c4ass.py
c4ass.py could convert Channel4's plain text to ASS subtitle. Or, if you look into the file, it's a SAMI or SMI file.

## Note c4d.py
This version requires you to manually download the program XML file.

## Usage
c4d.py channel4program.xml<br />
c4ass.py channel4subtitle.xml<br />
