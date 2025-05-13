#!/usr/bin/env python
import argparse
from mutagen.mp4 import MP4,MP4Cover
import imghdr as im
#from m4atag.tags import tag_lookup, reverse_tag_lookup
from tags import tag_lookup, reverse_tag_lookup

import pdb

def parse_args():
    parser = argparse.ArgumentParser(description="M4A Tag Editor")
    parser.add_argument("filename", help="File path to the track.")

    subparsers=parser.add_subparsers(dest="command",required=True)

    parser_get = subparsers.add_parser("get",help="Get tags")

    parser_set = subparsers.add_parser("set",help="Set tags")
    parser_set.add_argument("-t", "--track-title", help="Title of the track")
    parser_set.add_argument("-b", "--album", help="Track Album")
    parser_set.add_argument("-a", "--artist", help="Track Artist")
    parser_set.add_argument("-A", "--album-artist", help="Track Album Artist")
    parser_set.add_argument("-y", "--year", help="Year Album was released")
    parser_set.add_argument("-T", "--track-number-total-tracks", nargs="+", help="Total number of tracks")
    parser_set.add_argument("-D", "--disk-number-total-disks", nargs="+", help="Total number of discs")

    parser_cov = subparsers.add_parser("im",help="Handle image cover art")
    parser_cov.add_argument("image_file",help="Name of image file")
    #parser.add_argument("-g", "--get-tags", action="store_true", help="Only print the tags")
    #parser.add_argument("-im", "--track-image", nargs="+", help="Total number of tracks")
    args = parser.parse_args()
    return args

def get_cover(file_name):
    im_type = im.what(file_name)

    filetypes = {'jpeg':MP4Cover.FORMAT_JPEG,
            'png': MP4Cover.FORMAT_PNG}

    if im_type not in filetypes.keys():
        print(f'File type {im_type} not suitable for cover art. Acceptable ones are PNG and JPEG')
        return None

    with open(file_name,'rb') as O:
        cov = MP4Cover(O.read(),filetypes[im_type])
    return cov

    
def set_image(args):
    mp4_file = MP4(args.filename)
    covr = get_cover(args.image_file)
    mp4_file['covr'] = [covr]
    mp4_file.save(args.filename)


def get_tags(filename: str) -> None:
    file_tags = MP4(filename).tags
    for mutagen_tag, normal_tag in reverse_tag_lookup.items():
        if mutagen_tag in file_tags.keys():
            tag_value = file_tags[mutagen_tag][0]
            if type(tag_value) != str:
                print(f"{normal_tag}: {len(tag_value)/1000:.0f} kilobytes")
            else:
                print(f"{normal_tag}: {tag_value}")


def set_tags(args) -> None:
    "Loops through all args that can be set as tags and sets them."
    file_tags = MP4(args.filename).tags
    if file_tags == None:
        file_tags = MP4.MP4Tags()
    for arg in vars(args):
        arg_val = getattr(args, arg)
        if arg in tag_lookup.keys() and arg_val is not None:
            print(f"Setting tag '{arg}' to '{arg_val}'...")
            mutagen_tag = tag_lookup[arg]
            file_tags[mutagen_tag] = arg_val
    file_tags.save(args.filename)


def main():
    args = parse_args()
    if args.command == "get":
        get_tags(args.filename)
    elif args.command == "set":
        set_tags(args)
    elif args.command == "im":
        set_image(args)
    else:
        print("Whee!")
        
    """
    if args.get_tags:
        get_tags(args.filename)
    else:
        set_tags(args)
    """


if __name__ == "__main__":
    main()
