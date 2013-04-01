Title: redshift
Date: 2012-04-24 22:39
Tags: unix, lifestyle
Category: hacks
Slug: redshift
Author: Paul Tagliamonte
Summary: How I use redshift

Abstract
--------

[Redshift](https://launchpad.net/redshift) is a kickass project by
[Jon Lund Steffensen](https://launchpad.net/~jonls), which adjusts the screen
temperature along with the natrual cycle of the Sun. It helps cut down on
blue light late at night which has been shown to be harmful to our natural
sleep cycles.

The tool it's self in proper order, so this post is more documentation on
how I've set it up for myself.


Prerequesites
-------------

This note assumes you have your location syncing to a file such as
`~/.location.json`, mine syncs from my Phone.


Implementation
--------------

I wrote a small script, called `redinvoke` (how I invoke redshift), to be
started on login, that simply passes the lat/lon to the `redshift` instance.

    :::python
    from sh import redshift
    import json

    location = json.load(open("/home/tag/.location.json", 'r'))
    param = "%s:%s" % (location['latitude'], location['longitude'])
    redshift(l=param)

And, the startup entry in `~/.config/autostart`, to be started by a tool
like `fbautostart`.

    [Desktop Entry]
    Name=RedInvoke
    Exec=/home/tag/.bin/redinvoke
    Terminal=false
    Type=Application


So what?
--------

In a super sly way, now `redshift` uses my exact sync'd lat / lon to set my
screen temperature, which is helpful for whenever I travel anywhere.
I find that I can sleep better when I use redshift, and actually find myself
struggling to use non-redshifted machines. Give it a try!
