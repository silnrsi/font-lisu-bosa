#!/usr/bin/python3
# -*- coding: utf-8 -*-

APPNAME = "Bosa"
fontfamily=APPNAME

DESC_SHORT = "Font for the Lisu (Fraser) script"

getufoinfo('source/masters/' + fontfamily + 'LisuMaster-Regular' + '.ufo')
BUILDLABEL = "alpha"

for dspace in ('Upright', 'Italic'):
    designspace('source/' + fontfamily + dspace + 'Test.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
    )
