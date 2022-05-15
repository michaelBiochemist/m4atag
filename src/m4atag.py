#!/usr/bin/python3
import argparse
from mutagen.mp4 import MP4
from tags import tag_dict


arg_dict = {
    "t": "track_title",
    "b": "album",
    "a": "artist",
    "aa": "album_artist",
    #'': 'composer',
    "y": "year"
    #'c': 'comment',
    #'': 'description (usually used in podcasts)',
    #'': 'purchase date',
    #'': 'grouping',
    #'': 'genre',
    #'': 'lyrics',
    #'': 'podcast URL',
    #'': 'podcast episode GUID',
    #'': 'podcast category',
    #'': 'podcast keywords',
    #'': 'encoded by',
    #'': 'copyright',
    #'': 'album sort order',
    #'': 'album artist sort order',
    #'': 'artist sort order',
    #'': 'title sort order',
    #'': 'composer sort order',
    #'': 'show sort order',
    #'': 'show name',
    #'': 'work',
    #'': 'movement'
}


def get_tags(filename: str):
    tags = dict()
    for akey in arg_dict.keys():
        print(
            arg_dict[akey]
            + ": "
            + (MP4(filename).tags.get(tag_dict[arg_dict[akey]], [None])[-1] or "")
        )


def set_description(filename: str, description: str):
    tags = MP4(filename).tags
    tags["desc"] = description
    tags.save(filename)


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


def main():
    args = parse_args()
    if args.get_tags:
        get_tags(args.filename)
    else:
        set_tags(args)


if __name__ == "__main__":
    main()
