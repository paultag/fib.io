Title: kml to csv
Date: 2012-12-06
Tags: gis, kml
Category: hacks
Slug: kml-to-csv
Author: Paul Tagliamonte
Summary: Convert KML to CSV

Abstract
--------

[Google Latitude](https://latitude.google.com/) allows you to export your
history into [KML](http://en.wikipedia.org/wiki/Keyhole_Markup_Language),
the markup used by [Keyhole](http://en.wikipedia.org/wiki/Keyhole,_Inc), which
Google aquired back in the day.

Most tools sorta suck at working with KML data, so this hack is handy to export
Latitude's KML dump into a CSV.


Implementation
--------------

Nothing special. Code below:


    :::Python
    from lxml import etree
    import sys

    root = etree.fromstring(open(sys.argv[1], 'r').read())
    track = root.xpath("//*[local-name()='Track']")[0]

    coord = None
    when = None


    print "time,lat,lon"

    for node in track.iter():
        name = node.xpath("local-name()")
        if name == 'coord':
            lon, lat, z = node.xpath("text()")[0].split()
            coord = {
                "lat": lat,
                "lon": lon,
                "zee": z
            }
        elif name == 'when':
            when = node.xpath("text()")[0]

        if coord and when:
            print "%s,%s,%s" % (
                when,
                coord['lat'],
                coord['lon']
            )
            coord, when = None, None
