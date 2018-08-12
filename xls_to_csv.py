#!/bin/env python

import pandas as pd
import os
import os.path
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def convert_xls_files(source, destination):
    """ Convert all xls files in a directory to one csv file per sheet.
    csv files are saved in UTF-8 encoding.

    @param  string  source  Path to folder containing xls files
    @param  string  destination  Path to save csv files to.
    """
    # Find all xls files
    files = os.listdir(source)
    csvs = list(filter(lambda x: x.endswith('.xls'), files))

    n = len(csvs)

    logging.info("Found %d xls files", n)

    # Iterate over available excel files
    for i, xls in enumerate(csvs):
        # Get all sheets
        input_file = os.path.join(source, xls)
        sheets = pd.read_excel(input_file, None)
        logging.info("Converting %s, found %d sheets", input_file, len(sheets))
        # Strip .xls from filename
        base_outname = xls[:-4]
        # Save sheets to csv filesnn
        for sheet_name, df in sheets.items():
            outname = os.path.join(destination, base_outname + '-' + sheet_name + '.csv')
            df.to_csv(outname, index=False, encoding='utf-8', date_format='%Y-%m-%d %H:%M:%S')
        logging.info("Done converting %s.\t\t%d / %d", xls, i+1, n)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-folder', dest='source', required=True, help='Folder containing xls files to be converted.')
    parser.add_argument('-d', '--destination-folder', dest='destination', required=True, help='Folder to save csv files in.')
    args = parser.parse_args()
    convert_xls_files(args.source, args.destination)
