#!/usr/bin/env python

import docopt
import sys
import text_unidecode



# functions

def read_file(filename):
  if filename is None:
    return sys.stdin.read()

  with open(filename) as file_:
    return file_.read()


def write_file(filename, text):
  if filename is None:
    sys.stdout.write(text)
    return

  with open(filename, "w") as file_:
    file_.write(text)



# main routine

def main(args):
  """
  Usage:
    unidecode [<input_file> [<output_file>]]
  """

  write_file(args["<output_file>"],
             text_unidecode.unidecode(read_file(args["<input_file>"])))





if __name__ == "__main__":
  main(docopt.docopt(main.__doc__))
