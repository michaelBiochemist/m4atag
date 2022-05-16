#!/usr/bin/python3
import argparse
from mutagen.mp4 import MP4
from src.m4atag.tags import tag_lookup, reverse_tag_lookup


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--track-title", help="Title of the track")
    parser.add_argument("-b", "--album", help="Track Album")
    parser.add_argument("-a", "--artist", help="Track Artist")
    parser.add_argument("-A", "--album-artist", help="Track Album Artist")
    parser.add_argument("-y", "--year", help="Year Album was released")
    parser.add_argument("-T", "--track-number-total-tracks", nargs="+", help="Total number of tracks")
    parser.add_argument("-D", "--disk-number-total-disks", nargs="+", help="Total number of discs")
    parser.add_argument("-g", "--get-tags", action="store_true", help="Only print the tags")
    parser.add_argument("filename", help="File path to the track.")
    args = parser.parse_args()
    return args


def get_tags(filename: str) -> None:
    file_tags = MP4(filename).tags
    for mutagen_tag, normal_tag in reverse_tag_lookup.items():
        if mutagen_tag in file_tags.keys():
            print(f"{normal_tag}: {file_tags[mutagen_tag][0]}")


def set_tags(args) -> None:
    "Loops through all args that can be set as tags and sets them."
    file_tags = MP4(args.filename).tags
    for arg in vars(args):
        arg_val = getattr(args, arg)
        if arg in tag_lookup.keys() and arg_val is not None:
            print(f"Setting tag '{arg}' to '{arg_val}'...")
            mutagen_tag = tag_lookup[arg]
            file_tags[mutagen_tag] = arg_val
    file_tags.save(args.filename)


def main():
    args = parse_args()
    if args.get_tags:
        get_tags(args.filename)
    else:
        set_tags(args)


if __name__ == "__main__":
    main()
