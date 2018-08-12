# Tools for research

## Converting xls to csv

To convert an Excel <= 2003 (`*.xls`) file to `csv`, first install the libraries you need. Start the command line and run

    conda install --yes --file requirements.txt

Next, run the python converter

    ./xls_to_csv.py --source_path path/to/xls --output-path path/to/csv
