from collections import OrderedDict

tag_lookup = OrderedDict(
    {
        "track_title": "\xa9nam",
        "album": "\xa9alb",
        "artist": "\xa9ART",
        "album_artist": "aART",
        "composer": "\xa9wrt",
        "year": "\xa9day",
        "comment": "\xa9cmt",
        "description (usually used in podcasts)": "desc",
        "purchase date": "purd",
        "grouping": "\xa9grp",
        "genre": "\xa9gen",
        "lyrics": "\xa9lyr",
        "podcast_URL": "purl",
        "podcast_episode GUID": "egid",
        "podcast_category": "catg",
        "podcast_keywords": "keyw",
        "encoded_by": "\xa9too",
        "copyright": "cprt",
        "album_sort_order": "soal",
        "album_artist_sort_order": "soaa",
        "artist_sort_order": "soar",
        "title_sort_order": "sonm",
        "composer_sort_order": "soco",
        "show_sort_order": "sosn",
        "show_name": "tvsh",
        "work": "\xa9wrk",
        "movement": "\xa9mvn",
        "track_number_total_tracks": "trkn",
        "disk_number_total_disks": "disk",
    }
)
"Tag keys in mutagen are not human-readable. This dict maps human-readable keys to mutagen keys."

reverse_tag_lookup = OrderedDict({v: k for (k, v) in tag_lookup.items()})
"This dict allows you to lookup human-readable tags from mutagen keys."
