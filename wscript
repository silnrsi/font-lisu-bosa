#!/usr/bin/python3
# -*- coding: utf-8 -*-

APPNAME = "LisuBosa"
fontfamily=APPNAME

DESC_SHORT = "Font for the Lisu (Fraser) script"

getufoinfo('source/masters/' + fontfamily + '-Regular' + '.ufo')
#BUILDLABEL = "beta"
#BUILDVERSION = BUILDLABEL

# build axis-based family
for dspace in ('Upright', 'Italic'):
    designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
                opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/master.feax", to_ufo = 'True'),
                woff = woff()
    )

# build auxiliary 'Lt' RIBBI family
for dspace in ('Upright', 'Italic'):
    designspace('source/' + fontfamily + 'Lt'+dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
                opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/master.feax", to_ufo = 'True'),
                woff = woff()
    )
