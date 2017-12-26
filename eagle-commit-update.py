#!/env/python3
import os
import argparse
import xml.etree.ElementTree as ET


class MyParser(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="")
        self.parser.add_argument("filename")
        self.parser.add_argument("--tag", "-T", help="updating tag", default="a5a5a5a")
        self.parser.add_argument("--verbose", "-V", help="print more message", default=False)
        self.args = self.parser.parse_args(namespace=self)


def main(filename, tag, verbose):
    search_strings = [".//elements/element[@library='git-revision']",
                      ".//parts/part[@library='git-revision']"
                      ]

    title, ext = os.path.splitext(filename)
    newname = "{0}-{1}{2}".format(title, tag, ext)
    print(newname)
    for search_string in search_strings:
        board = ET.parse(filename)
        tree = board.getroot()
        elements = tree.findall(search_string)
        if elements:
            if verbose:
                print("{0} found".format(search_string))
            [elem.set("value", tag) for elem in elements]
            board.write(newname)
        else:
            if verbose:
                print("{0} not found".format(search_string))


if __name__ == '__main__':
    parser = MyParser()
    main(parser.filename, parser.tag, parser.verbose)
