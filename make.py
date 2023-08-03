import sys
import os
import argparse

import script.configbuilder as cbuild
import script.databuilder as dbuild

def main():
    parser = argparse.ArgumentParser(description="Python script to build the application data")
    parser.add_argument('--config', action='store_true', help='build configuration file and apply to raw data')
    parser.add_argument('--data', action='store_true', help='build raw data and put into asset path')
    parser.add_argument('--external', action='store_true', help='put an external property into specific folder and update')
    parser.add_argument('--override', action='store_true', help='replace content on a master path into some path')
    parser.add_argument('--apply-data', action='store_true', help='replace raw data from asset path (src/...) as it may be modified by editor')
    
    args = parser.parse_args()
    
    if (args.config):
        cbuild.appconfig_builder.run()
    
    if (args.data):
        print(".")
        print(".")
        print("===========================================================")
        print("Convert some files")
        print("===========================================================")
        dbuild.export_strings.run()
        dbuild.export_database.run()
        dbuild.export_resources.run()
        
        print(".")
        print(".")
        print("===========================================================")
        print("Cloning assets to /src")
        print("===========================================================")        
        dbuild.file_overrider.clone_data2source()

    if (args.external):
        print(".")
        print(".")
        print("===========================================================")
        print("Apply svn externals into specific folder")
        print("===========================================================")

    if (args.override):
        print(".")
        print(".")
        print("===========================================================")
        print("Override files from /_master_ into local")
        print("===========================================================")        
        dbuild.file_overrider.override_source()
        
    if (args.apply_data):
        print(".")
        print(".")
        print("===========================================================")
        print("Cloning /src to /data (reverse cloning)")
        print("===========================================================")
        dbuild.file_overrider.clone_source2data()
        
if __name__ == "__main__":
    main()