#! /usr/bin/env python3
"""
---------------------------------------------------------------------
Project: Medicare Documentation
Program: remove-private-chunks.py
Author:  Kyle Barron <barronk@mit.edu>
Created: 1/17/2019, 5:22:42 PM
Updated: 1/17/2019, 5:22:42 PM
Purpose: Remove private parts of documentation for public site

I'm declaring the syntax
```
<!-- start private -->
<!-- end private -->
```
to start and end a private block, respectively. The `<!-- ... -->` is an HTML
comment, so that won't show up in the Markdown output of the source code before
the private parts are stripped out. There can be whitespace before the `<!--`,
but the entire start or end tag must appear on a single line. The tag plus
whitespace must be the only thing on the line.

"""

import re
from shutil import copy
from pathlib import Path


def main(public: bool=True):
    docs_dir = Path('../docs')
    out_dir = Path('../public/docs') if public else Path('../private/docs')

    for p in docs_dir.glob('**/*'):
        if p.is_dir():
            (out_dir / p.relative_to(docs_dir)).mkdir(parents=True, exist_ok=True)
            continue

        if not p.is_file():
            continue

        if (p.suffix != '.md') or not public:
            copy(p, out_dir / p.relative_to(docs_dir))
            continue

        # Should be a markdown file to be sanitized
        with p.open() as f:
            lines = f.readlines()
        lines = sanitize_file(lines)
        with (out_dir / p.relative_to(docs_dir)).open('w') as f:
            f.write(''.join(lines))

    if public:
        copy('../mkdocs.yml', '../public/mkdocs.yml')
    else:
        copy('../mkdocs.yml', '../private/mkdocs.yml')


def sanitize_file(lines):
    start_re = r'^\s*<!--\s*start\s+private\s*-->\s*$'
    end_re = r'^\s*<!--\s*end\s+private\s*-->\s*$'

    lines_final = []
    public = True
    for line in lines:
        if public:
            if re.search(start_re, line):
                public = False
                continue
            lines_final.append(line)
        else:
            if re.search(end_re, line):
                public = True

    return lines_final


if __name__ == '__main__':
    main(public=True)
    main(public=False)
