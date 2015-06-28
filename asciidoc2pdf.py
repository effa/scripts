#!/usr/bin/env python
# encoding: utf-8

from subprocess import call
import argparse


def main():
    parser = argparse.ArgumentParser(description="Transform Asciidoc to PDF.")
    parser.add_argument('--lang', '-l', default='cs', help='language')
    parser.add_argument('--frontpage', '-f', action='store_true',
                        help='include frontpage')
    parser.add_argument('sources', nargs='+', help='Asciidoc source file')
    args = parser.parse_args()
    if args.frontpage:
        generic_command = r'a2x -d article -a lang={lang} -a ascii-ids' \
            r' --dblatex-opts " -P doc.layout=\"coverpage frontmatter mainmatter\"' \
            r' -P doc.publisher.show=0 -P latex.output.revhistory=0' \
            r' -s \"/home/tom/.asciidoc/asciidoc-dblatex-with-author.sty\""' \
            r' {source}'
    else:
        generic_command = r'a2x -a lang={lang} -a ascii-ids' \
            r' --dblatex-opts " -P doc.layout=\"frontmatter mainmatter\"' \
            r' -P doc.publisher.show=0 -P latex.output.revhistory=0"' \
            r' {source}'
    for source in args.sources:
        call(generic_command.format(lang=args.lang, source=source),
             shell=True)


if __name__ == '__main__':
    main()
