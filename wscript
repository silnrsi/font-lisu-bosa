#!/usr/bin/python
# this is a smith configuration file

# set the font name, version, licensing and description
APPNAME = "Bosa"
fontfamily=APPNAME

DESC_SHORT = "Font for the Lisu (Fraser) script"
DESC_NAME = "BosaLisu"

getufoinfo('source/' + fontfamily + 'Lisu-Regular' + '.ufo')
BUILDLABEL = "alpha"

for dspace in ('Upright', ):
    designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
    )
