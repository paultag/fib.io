Title: libolla
Date: 2013-03-31 11:06
Tags: c, domains, unix
Category: hacks
Slug: libolla
Author: Paul Tagliamonte
Summary: How to shorten domain names
GitHub: https://github.com/paultag/libolla/

Abstract
--------

Typing domain names sucks. I hate having to type `debian.org` all the time, when
something like `d.o` is what we use in casual conversation. As a result, I've
hacked up a small library, to be `LD_PRELOAD`ed that allows for such domains.
I've called this library `libolla`, both a fitting name and a nod to my
[alma mater](http://jcu.edu/).


Implementation
--------------

I implemented `libolla` as a straight C library that implements `getaddrinfo`.
The call is actually a pass-through to the "real" `getaddrinfo` by using
`dlsym`'s `RTLD_NEXT`.

The actual implementation looks a bit like:

    int getaddrinfo ( const char * node, const char * service,
        const struct addrinfo * hints, struct addrinfo ** res
    ) {
        int (*orig_addr)(const char *, const char *, const struct addrinfo *,
            struct addrinfo **) = dlsym(RTLD_NEXT, "getaddrinfo");
        char * result;
        if ( expand_domain( node, &result ) > 0 ) {
            return orig_addr(result, service, hints, res );
        }
        return orig_addr(node, service, hints, res);
    }

This basically allows us to intercept calls to our "shorthand" domains, and
expand out the "inner" call to `getaddrinfo`.


Issues with the Implementation
------------------------------

The biggest issue with the implementation is that the system thinks domains
like `master.d.o` are real, so stuff like webbrowsers will send it in the
request headers (e.g. something like `Host: master.d.o`), which will, of course
break most webserver's virtual host entries.

It is, however, still great for `ssh`!
