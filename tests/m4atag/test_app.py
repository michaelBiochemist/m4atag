import sys
import pytest
from m4atag.app import parse_args, get_tags, set_tags


def test_set_tags(capsys):
    sys.argv = ["m4atag.py", "-t", "Scape Main", "-b", "RS2", "-a", "Jagex", "tests/m4atag/runscape.m4a"]
    args = parse_args()
    set_tags(args)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Setting tag 'track_title' to 'Scape Main'...\nSetting tag 'album' to 'RS2'...\nSetting tag 'artist' to 'Jagex'...\n"
    )


def test_get_tags(capsys):
    sys.argv = ["m4atag.py", "-g", "tests/m4atag/runscape.m4a"]
    args = parse_args()
    get_tags(args.filename)
    captured = capsys.readouterr()
    assert captured.out == "track_title: Scape Main\nalbum: RS2\nartist: Jagex\nencoded_by: Lavf58.29.100\n"
