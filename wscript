#!/usr/bin/python
# this is a smith configuration file

# set the font name, version, licensing and description
APPNAME = "LisuNew"
fontfamily=APPNAME

DESC_SHORT = "Font for the Lisu (Fraser) script"
DESC_NAME = "LisuNew"

getufoinfo('source/' + fontfamily + '-Regular' + '.ufo')
BUILDLABEL = "alpha"

for dspace in ('Roman', 'Italic'):
    designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
    )
