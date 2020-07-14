# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from getarticle import GetArticle
import appscript

def parse_args():
    parser = ArgumentParser(description='getarticle CLI for Safari')
    parser.add_argument('-o', '--output', required=False, \
        help='download direction')
    args = parser.parse_args()
    return args


def main(args):
    ga = GetArticle()
    ga.input_article(appscript.app("Safari").windows.first.current_tab.URL())
    ga.download(direction=args.output)


def entry_point():
    args = parse_args()
    main(args)


if __name__ == '__main__':
    entry_point()
