#!/usr/bin/python3

from mutagen.mp4 import MP4
import argparse
#import sys

tag_dict = {
	'track_title': "\xa9nam",
	'album': "\xa9alb",
	'artist': "\xa9ART",
	'album_artist': "aART",
	'composer': "\xa9wrt",
	'year': "\xa9day",
	'comment': "\xa9cmt",
	'description (usually used in podcasts)': "desc",
	'purchase date': "purd",
	'grouping': "\xa9grp",
	'genre': "\xa9gen",
	'lyrics': "\xa9lyr",
	'podcast URL': "purl",
	'podcast episode GUID': "egid",
	'podcast category': "catg",
	'podcast keywords': "keyw",
	'encoded by': "\xa9too",
	'copyright': "cprt",
	'album sort order': "soal",
	'album artist sort order': "soaa",
	'artist sort order': "soar",
	'title sort order': "sonm",
	'composer sort order': "soco",
	'show sort order': "sosn",
	'show name': "tvsh",
	'work': "\xa9wrk",
	'movement': "\xa9mvn",
	'track_number_total_tracks': "trkn",
	'disk_number_total_disks': "disk"
	
}
arg_dict = {
	't': 'track_title',
	'b': 'album',
	'a': 'artist',
	'aa': 'album_artist',
	#'': 'composer',
	'y': 'year'
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

def get_tags(filename):
	tags = dict();	
	for akey in arg_dict.keys():
		print(arg_dict[akey]+': '+(MP4(filename).tags.get(tag_dict[arg_dict[akey]], [None])[-1] or ''))
		#fprint('%s: %s',arg_dict[akey],tag_dict[arg_dict[akey]])
    #return MP4(filename).tags.get("desc", [None])[-1]

def set_description(filename, description):
    tags = MP4(filename).tags
    tags["desc"] = description
    tags.save(filename)

def set_tags(args):
	
	tags = MP4(args.filename).tags
	for arg in vars(args):
		val = getattr(args, arg) 
		if arg in tag_dict.keys() and val is not None: 
			print(arg)
			tags[tag_dict[arg]] = val
	tags.save(args.filename)

def get_tag():
	pass

def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("-t", "--track-title",help="It's the title of the song, you fuck!")
	parser.add_argument("-b", "--album")
	parser.add_argument("-a", "--artist")
	parser.add_argument("-A", "--album-artist",help="album artist is magically different from artist.")
	parser.add_argument("-y", "--year",help="the year the album was released")
	parser.add_argument("-T", "--track-number-total-tracks")
	parser.add_argument("-D", "--disk-number-total-disks", help="this is supposed to be a tuple?")
	parser.add_argument("-g", "--get-tags", action="store_true")
	parser.add_argument("filename")

	args = parser.parse_args()
	return args

def main():
	args = parse_args()
	if args.get_tags:
		get_tags(args.filename)
	else:
		set_tags(args)
	#import pdb; pdb.set_trace();
	
	

if __name__=='__main__':
	#get_tags(sys.argv[1])
	main()
	

"""
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
