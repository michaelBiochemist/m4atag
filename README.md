# m4atag
a command-line metadata editor for m4a files

# Tag Lookup
'track title': ‘\xa9nam’,
'album': ‘\xa9alb’,
'artist': ‘\xa9ART’,
'album artist': ‘aART’,
'composer': ‘\xa9wrt’,
'year': ‘\xa9day’,
'comment': ‘\xa9cmt’,
'description (usually used in podcasts)': ‘desc’,
'purchase date': ‘purd’,
'grouping': ‘\xa9grp’,
'genre': ‘\xa9gen’,
'lyrics': ‘\xa9lyr’,
'podcast URL': ‘purl’,
'podcast episode GUID': ‘egid’,
'podcast category': ‘catg’,
'podcast keywords': ‘keyw’,
'encoded by': ‘\xa9too’,
'copyright': ‘cprt’,
'album sort order': ‘soal’,
'album artist sort order': ‘soaa’,
'artist sort order': ‘soar’,
'title sort order': ‘sonm’,
'composer sort order': ‘soco’,
'show sort order': ‘sosn’,
'show name': ‘tvsh’,
'work': ‘\xa9wrk’,
'movement': ‘\xa9mvn’,

Tuples of ints (multiple values per key are supported):

‘trkn’ - track number, total tracks
‘disk’ - disc number, total discs
Integer values:

‘tmpo’ - tempo/BPM
‘\xa9mvc’ - Movement Count
‘\xa9mvi’ - Movement Index
‘shwm’ - work/movement
‘stik’ - Media Kind
‘hdvd’ - HD Video
‘rtng’ - Content Rating
‘tves’ - TV Episode
‘tvsn’ - TV Season
‘plID’, ‘cnID’, ‘geID’, ‘atID’, ‘sfID’, ‘cmID’, ‘akID’ - Various iTunes Internal IDs
Others:

‘covr’ - cover artwork, list of MP4Cover objects (which are tagged strs)
‘gnre’ - ID3v1 genre. Not supported, use ‘\xa9gen’ instead.
"""
