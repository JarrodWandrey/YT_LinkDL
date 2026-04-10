import argparse
from . import clipboard, history, download, gui

def main():
    # Creates an arugment to allow for the program to run headless for multiple downloads, or with a GUI for single downloads
    parser = argparse.ArgumentParser(description="YouTube Link Downloader")
    parser.add_argument('--watch', action='store_true', help='Watch clipboard for links')
    args = parser.parse_args()

    if args.watch:
        clipboard.watch_clipboard()
    else:
        pass

if __name__ == "__main__":
    main()