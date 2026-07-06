'''
extract-transform-load script for everloop's csv databases -> supabase

Needs to take multiple csv files as input (preferably via a tolerable GUI),
validate the csv files, transform them with lowercase/property priority/keys,
and finally load them into supabase.
'''
import extract as ex

def main():
    ex.verify_csv_files(ex.EXPECTED_DIRECTORY, ex.EXPECTED_FILENAMES)

if __name__ == "__main__":
    main()