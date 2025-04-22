"""Set-up for pywebexercises

Credit:
    > This gets the webex.css and webex.js necessary for processing the
    exercises in quarto. These files are from the R webexercises package by
    Dale Barr and Lisa DeBruine (https://github.com/PsyTeachR/webexercises).

Licence:
    This project is licensed under the CC BY-SA 4.0 licence.
"""
import os
import shutil


def setup_webex_assets(force=False):
    """
    Set-up pywebexercises assets.

    Downloads the webex.css and webex.js files and saves them in a folder
    called "assets/".

    Arguments:
        force (bool)
            If True, overwrite existing files. Default is False.
    """
    # Write the path to assets/ folder in the package and current directory
    package_assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    target_assets_dir = os.path.join(os.getcwd(), "assets")

    # If assets does not exist in the current directory, then create folder
    if not os.path.exists(target_assets_dir):
        os.makedirs(target_assets_dir)

    # List the files to download
    asset_files = ["webex.css", "webex.js"]

    # Loop through the files...
    for asset_file in asset_files:

        # Create path to file in package and current directory
        src = os.path.join(package_assets_dir, asset_file)
        dst = os.path.join(target_assets_dir, asset_file)

        # If it does not exist or force=True, then create the file
        if not os.path.exists(dst) or force:
            shutil.copyfile(src, dst)
            if force:
                print(f"Overwrote {asset_file} in assets directory.")
            else:
                print(f"Copied {asset_file} to assets directory.")

        # If there is a file of that name and force=False, then print a warning
        else:
            print(f"{asset_file} already exists in assets directory. Use " +
                  "force=True to overwrite.")

    print("Setup complete.")
