#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Created By  : 
# Created Date: 2024/02/11
# version ='1.0'
# ----------------------------------------------------------------------
# USAGE
# It also requires running doi2bib
# pip install doi2bib
# The commands are as follows:
#  py doi2bib.py -c mydoi.csv --output mybib.bib
# ----------------------------------------------------------------------

from __future__ import unicode_literals, print_function, absolute_import
import argparse
import textwrap
import csv
from doi2bib.crossref import get_bib_from_doi
import io


def save_output_bibs(bibs, output_file):
    try:
        with io.open(output_file, 'w', encoding="utf-8") as bibfile:
            for bib in bibs:
                bibfile.write("{}\n".format(bib))

    except TypeError:
        print("Can't save in output file\n")
        print(bibs)


def main():
    parser = argparse.ArgumentParser(
        prog="doi2bib",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Convert a list of DOIs in a bibfile.
        You also can convert a simple DOI, like:
        $ doi2bib  10.1063/1.3149495
        -----------------------------------------------------
            @author: Bruno Messias
            @email: messias.physics@gmail.com
            @telegram: @brunomessias
            @github: https://github.com/bibcure/doi2bib
        ''')
    )

    parser.add_argument(
        "--input", "-i",
        type=argparse.FileType("r"),
        help="input file"
    )

    parser.add_argument(
    "--input_csv", "-c",
    type=argparse.FileType("r", encoding="utf-8"),
    help="input CSV file with DOI in the first column"
)

    parser.add_argument(
        "--output", "-o",
        help="bibtex output file"
    )

    parser.add_argument(
        "--abstract",
        action='store_true',
        help="try to import the abstract info"
    )

    args = parser.parse_args()

    if args.input_csv:
        dois = []
        try:
            csv_reader = csv.reader(args.input_csv)
            for row in csv_reader:
                if row:  # Ensure it's not an empty row
                    dois.append(row[0])
        finally:
            args.input_csv.close()
    elif args.input:
        dois = args.input.read().splitlines()
        args.input.close()
    else:
        print("No input provided.")
        return

    bibs = []
    for doi in dois:
        found, bib = get_bib_from_doi(doi, add_abstract=args.abstract)
        if found:
            bibs.append(bib)

    if len(bibs) > 0:
        save_output_bibs(bibs, args.output)
    else:
        print("No valid DOIs found.")


if __name__ == "__main__":
    main()