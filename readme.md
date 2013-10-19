# Sonos Music System CLI
This is a quick CLI for the Sonos Music System.

# Install

* `python setup.py install`

# Usage

```
$ sonoscli
:: Sonos CLI ::
  Master: 1.2.3.4
Enter an IP to control from above: 1.2.3.4
> volume
  70
> track
  Nine Inch Nails: Copy of a (Hesitation Marks)
> pause
> play
> help
  
  Sonos CLI
  
  Commands:
      play: Plays current track
      next, n: Skips to next queue item
      prev, p: Skips to previous queue item
      seek, s: Seeks to specified time (i.e. "seek 00:00:00")
      pause: Pauses current track
      mute: Mutes controller
      volume, v: Gets/Sets volume (use "volume 80" to set volume level to 80)
      track, t: Shows current track info
      play_uri: Plays a track from URI
      artists: Shows artists (use "artists 0 100" to show first 100 artists)
      albums: Shows albums (use "albums 0 100" to show first 100 albums)
      tracks: Shows tracks (use "tracks 0 100" to show first 100 tracks)
      help, h: Shows help
      exit, q: Quits
  
>
```
