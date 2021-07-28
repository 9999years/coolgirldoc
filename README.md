# cool girl doc

**Note: cool girl doc is little more than a glimmer in my eye.**

A Python API documentation generator (for cool girls & their friends) written in Rust.

Minimum viable product:
- A super-speedy and ✨parallel✨ Rust CLI
- Write your docs in markdown
- Link to items in intersphinx inventories

Bonuses:
- Current-year niceties like live reloads, a development server, file watching
- Intersphinx inventory exports, for Sphinx compatability
- Vendor intersphinx inventories to build docs offline
- Some RST compatability for interop; I don't want to write a Sphinx-compatible
  or feature-complete RST parser, though
- Include markdown files by name / write narrative-form docs
- Doctests
- LaTeX support with something like [KaTeX][katex]
- Some equivalent of [RST's admonitions/callouts][rst-admonitions] (warning, note,
  hint, etc.)
- Development tools to parse/introspect on docs; in particular, a language server to
  highlight, provide hover information, and preview docs would be super useful.  

[katex]: https://katex.org/
[rst-admonitions]: https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions


## why?

1. Sphinx generates very mediocre HTML with minimal markup that's difficult or
   impossible to style with CSS. I say "impossible" because many elements that
   should be styled (such as argument lists) contain text outside of elements,
   so lots of text is impossible to select for styling with CSS.

   This doesn't account for all the poor graphic design decisions in Sphinx
   themes, but it prevents many improvements that would make Python
   documentation more legible and easier to navigate.

2. Sphinx uses reStructuredText (RST), which doesn't have a specified grammar
   or parser, making tooling nearly impossible to write; there's no canonical
   tokenizer, syntax tree, or parsing algorithm for RST.

3. Python tooling tends to be slow, unoptimized, unplanned, and crufty. We can
   improve the situation by moving as much of the logic as possible into Rust.


## architecture

    ┌───────────────────┐
    │file tree traversal│
    └───────────────────┘
      ↓ module paths
    ┌───────────────────┐
    │docstring retrieval│
    └───────────────────┘
      ↓ docstrings, types
    ┌───────────────────┐
    │output formatter   │
    └───────────────────┘

(This architecture is preliminary and will change through development.)

There will be a file tree traversal module which exports a list of modules to
document to a docstring retrieval script.

The docstring retrieval module will shell out to a Python script that imports a
module, grabs its docstrings, and prints the relevant data to stdout as JSON.

Finally, the output formatter will receive a data structure describing all the
modules, types, locations, etc. to be documented and transform them into a file
or set of files. At first, cool girl doc will only target HTML, but the
architecture should be neutral enough that other mediums can be implemented.

I would like users to be able to swap out the docstring retrieval Python script
and output formatters at runtime.


## design

A lot of tricky design decisions haven't been made yet.

- What's the syntax for linking to other items?

  I'll look to [rustdoc's link syntax][rustdoc-links] for inspiration. [Apple's
  DocC][docc-structure] is also interesting.
  
- How do themes work? What are theme templates like?

  I want to _start_ from a graphic design standpoint here, and design APIs that
  enable good design. I think rustdoc/mdbook makes pretty good output. Racket's
  Scribble ([example Racket docs][racket-pattern-matching]) also produces
  excellent output, thanks to [Matthew Butterick's][butterick] work.
  
[rustdoc-links]: https://doc.rust-lang.org/rustdoc/linking-to-items-by-name.html
[docc-structure]: https://developer.apple.com/documentation/Xcode/adding-structure-to-your-documentation-pages
[racket-pattern-matching]: https://docs.racket-lang.org/reference/match.html
[butterick]: https://en.wikipedia.org/wiki/Matthew_Butterick
