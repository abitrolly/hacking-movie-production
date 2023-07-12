### Hacking Movie Production

There is a legacy. A lot of legacy. A lot of people. Dreamers, who became blackmailers.
Not because they wanted it, but because the world consumes money.

### Scripts

    `./bootstrap`    - downloads and unpacks FFMPEG into `.bin/`

### Hacking Audio

Movie format for audio is 48kHz/24bit. Often moved as
[AIFF](https://abitrolly.hashnode.dev/aiff-48-24) files.

Voices are recorded in mono and then panned if needed to left or right. When stereo
recording device saves sound from mono mic, it may create stereo file with voice in the
left channel and noise in the right (Zoom H1 Handy Recorder does this).

**To discard the noisy right channel** and save into 48kHz/24Bit AIFF format, use
[FFMPEG](https://ffmpeg.org/) tool. Made by awesome folks I can only hope that they are
good and have enough cash to go on. The command to do so:

    ffmpeg -i ZOOM0038.WAV -c:a pcm_s24be -ar 48000 -af "pan=mono|FC=FL" output.aiff

