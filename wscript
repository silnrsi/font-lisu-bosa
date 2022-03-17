#!/usr/bin/python3
# -*- coding: utf-8 -*-

APPNAME = "LisuBosaTestE"
sourcefontfamily = "LisuBosa"

DESC_SHORT = "Font for the Lisu (Fraser) script"

# build axis-based family
getufoinfo('source/masters/' + sourcefontfamily + '-Regular' + '.ufo')

for dspace in ('Upright', 'Italic'):
    designspace('source/' + sourcefontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
                opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/master.feax", to_ufo = 'True'),
                woff = woff('web/${DS:FILENAME_BASE}',
                    metadata = f'../source/{sourcefontfamily}-WOFF-metadata.xml'),
    )

# build auxiliary 'Lt' RIBBI family
ribbipackage = package(appname = "LisuBosaLtTestE")

getufoinfo('source/masters/' + sourcefontfamily + '-Regular' + '.ufo', ribbipackage)

for dspace in ('Upright', 'Italic'):
    designspace('source/' + sourcefontfamily + 'Lt' + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi"),
                opentype = fea("generated/${DS:FILENAME_BASE}.fea", master="source/master.feax", to_ufo = 'True'),
                #woff = woff(),
                package = ribbipackage
    )
