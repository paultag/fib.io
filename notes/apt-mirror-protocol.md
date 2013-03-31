Title: Using the apt mirror protocol
Date: 2013-03-30 21:32
Tags: debian, apt
Category: hacks
Slug: apt-mirror-protocol
Author: Paul Tagliamonte

Abstract
--------

It's sometimes helpful to keep your machines using a list of apt archives
to use, rather then a single mirror, because redudency is good.

Rather then using (the great) services like `http.debian.net` or
`ftp.us.debian.org`, you can set your own mirror lists using apt's
`mirror://` protocol.


Why?
----

If you have a local network mirror, it's helpful to have your machines default
to the local mirror, and fall back to your local friendly mirror.


Practical Bits
--------------

You've got three core things to do:

  * Pick your mirrors
  * Put them in a public place you can always get to (I use
    [static.pault.ag](http://static.pault.ag/debian/mirrors.txt).
  * Configure your `sources.list` to use the mirror.txt file by pointing
    to the text file with the `mirror://` protocol.

Here's an example `sources.list`:

    deb mirror://static.pault.ag/debian/mirrors.txt unstable main
    deb mirror://static.pault.ag/debian/mirrors.txt experimental main
    deb-src mirror://static.pault.ag/debian/mirrors.txt unstable main
    deb-src mirror://static.pault.ag/debian/mirrors.txt experimental main

Problems
--------

`update-command-not-found` will blow up like:

W: Don't know how to handle mirror
W: Don't know how to handle mirror
W: Don't know how to handle mirror
W: Don't know how to handle mirror
W: Don't know how to handle mirror
W: Don't know how to handle mirror
