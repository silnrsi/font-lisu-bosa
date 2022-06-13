#!/usr/bin/python3
# -*- coding: utf-8 -*-

APPNAME = "LisuBosa"
sourcefontfamily = "LisuBosa"

DESC_SHORT = "Font for the Lisu (Fraser) script"

# build axis-based family
getufoinfo('source/masters/' + sourcefontfamily + '-Regular' + '.ufo')

for dspace in ('Upright', 'Italic'):
    designspace('source/' + sourcefontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                version = VERSION,
                pdf = fret(params="-r -oi"),
                opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/master.feax", to_ufo = 'True'),
                woff = woff('web/${DS:FILENAME_BASE}',
                    metadata = f'../source/{sourcefontfamily}-WOFF-metadata.xml'),
                shortcircuit = False
    )

# build auxiliary 'Lt' RIBBI family
ribbipackage = package(appname = "LisuBosaLt")

getufoinfo('source/masters/' + sourcefontfamily + '-Regular' + '.ufo', ribbipackage)

for dspace in ('Upright', 'Italic'):
    designspace('source/' + sourcefontfamily + 'Lt' + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                version = VERSION,
                pdf = fret(params="-r -oi"),
                opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/master.feax", to_ufo = 'True'),
                #woff = woff(),
                package = ribbipackage
    )
