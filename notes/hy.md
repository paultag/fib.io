Title: hy
Date: 2013-03-15 15:35
Tags: python, lisp
Category: hacks
Slug: hy
Author: Paul Tagliamonte
Summary: Implementation notes of Hy
GitHub: https://github.com/paultag/hy
Website: http://hy.pault.ag


Abstract
--------

I've implemented a partial Lisp variant, called "[Hy](http://hy.pault.ag/)",
which "compiles" to Python AST. This variant lets you write some pretty
standard Lisp (very [Clojure](http://clojure.org/) like), with full access to
Python internals, functions and libraries.


Implementation
--------------

Hoboy. This one is a doozy. I've broken this up into a few different parts.
Feel free to skip along to the notes on the part you're most interested in.

### Tokenizing / Lexing

I wrote a small & trivial stack-ed state based parser. A bit kludgey, and
it's not so great with uneven expressions (I don't have a clean way to parse
stuff like ``(foo)` without rewriting the lexer), so I'm not going to go into
it's implementation, since it's crap.

### Modling Lisp

I've broken down Lisp into a few different object types. They're `HyObject` as
a superclass for all the Hy models. This comes in handy for some compilation
steps. Nextly, I've added in the `HyList` type, which is similar in syntax
to a Clojure "vector". One subclass of that is the `HyExpression`, which is
a form set up for evalulation. Following all that, we have `HyDict`s, (pretty
easy to guess at what that's for), and the (fairly standard) `HySymbol`,
`HyString`, and `HyInteger` types.

Typing things internally is helpful for our compilation steps later.

### Compiling Hy into Python

All the magic happens in `hy.compiler`, where we use a faux-recusive method
of iterating over the Hy model tree. The compiler class uses decorated methods
to help divide up the entries in the `HyASTCompiler.compile` method.
Here's an example:

    :::python
        @builds(HyString)
        def compile_string(self, string):
            return ast.Str(s=str(string), lineno=string.start_line,
                           col_offset=string.start_column)

By "recusing" back to the `HyASTCompiler.compile` method, we can interate over
the Hy tree in order, and build up the AST as we iterate through the Hy tree.

### Evaluating the Python AST

We take the AST from the steps above, and run it through some code that
looks a bit like:

    :::python
        eval(compile(ast, fpath, "exec"), mod.__dict__)

This evaluates the code object produced from the Python AST (called `ast`)
in the `mod` namespace.


### Making Lisp importable

We can abuse a little known PEP called
[PEP 302](http://www.python.org/dev/peps/pep-0302/), which allows us to write
"meta importers". Meta importers are (in this case) run upon failure to load
a module (so I didn't have to worry about importing Python modules as well.)

For more information on the importer setup, feel free to check out the
[code](https://github.com/paultag/hy/blob/master/hy/importer.py).

At it's core, it basically converts the Python to a code object, then drops
the processed code into `sys.modules`.

### Some examples

Look, it's functional!

    :::clojure
    => (max (map (lambda [x] (len x)) ["hi" "my" "name" "is" "paul"]))
    4

And, now, using some [python-sh](http://amoffat.github.com/sh/) voodoo:

    :::clojure
    (import-from sh cat grep)
    (-> (cat "/usr/share/dict/words") (grep "-E" "bro$"))


How do I play with it?
----------------------

I'd personally setup a virtualenv (`mkvirtualenv hy`), and install Hy into
the virtualenv (`pip install hy`).

After this is done, you should have access to `hy(1)`, the interactive REPL
(with some slamn' readline bits).

    :::clojure
    => (print (.join ", " ["Hello" "World"]))
    Hello, World
    => 
