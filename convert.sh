#!/bin/bash

# if path to ffmpeg binary is not set, set to locally unpacked version
FFMPEG=${FFMPEG:-.bin/ffmpeg}
SRC=${SRC:-RAW/DAY1}

for i in "$SRC"/*.WAV; do
	echo "---[ Converting $i ]---------------------------------------------"
	"$FFMPEG" -hide_banner -i "$i" -c:a pcm_s24be -ar 48000 -af "pan=mono|FC=FL" -write_id3v2 yes "${i%.*}.aiff"
done


