#!/usr/bin/python3
import argparse
from mutagen.mp4 import MP4
from tags import tag_dict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--track-title", help="Title of the track")
    parser.add_argument("-b", "--album", help="Track Album")
    parser.add_argument("-a", "--artist", help="Track Artist")
    parser.add_argument("-A", "--album-artist", help="Track Album Artist")
    parser.add_argument("-y", "--year", help="Year Album was released")
    parser.add_argument("-T", "--track-number-total-tracks", help="Total number of tracks")
    parser.add_argument("-D", "--disk-number-total-disks", help="Total number of discs")
    parser.add_argument("-g", "--get-tags", action="store_true", help="Only print the tags")
    parser.add_argument("filename", help="File path to the track.")
    args = parser.parse_args()
    return args


def set_tags(args):
    "Loops through all args that can be set as tags and sets them."
    tags = MP4(args.filename).tags
    for arg in vars(args):
        val = getattr(args, arg)
        if arg in tag_dict.keys() and val is not None:
            print(f"Setting tag {arg} to value {val}...")
            actual_tag = tag_dict[arg]
            tags[actual_tag] = val
    tags.save(args.filename)


def main():
    args = parse_args()
    if args.get_tags:
        print(MP4(args.filename).tags)
    else:
        set_tags(args)


if __name__ == "__main__":
    main()
