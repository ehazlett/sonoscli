#!/usr/bin/env python
from clint.textui import puts, indent, colored
from soco import SoCo, SonosDiscovery
import sys

HELP_STR = """
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
"""
class SonosController(object):
    def __init__(self, soco=None):
        self._soco = soco
    def play(self, *args, **kwargs):
        return self._soco.play()
    def next(self, *args, **kwargs):
        return self._soco.next()
    def n(self, *args, **kwargs):
        "Alias for next"
        return self.next(*args, **kwargs)
    def prev(self, *args, **kwargs):
        return self._soco.previous()
    def p(self, *args, **kwargs):
        "Alias for prev"
        return self.prev(*args, **kwargs)
    def seek(self, location=None, *args, **kwargs):
        return self._soco.seek(location)
    def s(self, location=None, *args, **kwargs):
        "Alias for seek"
        return self.seek(location, *args, **kwargs)
    def pause(self, *args, **kwargs):
        return self._soco.pause()
    def mute(self, *args, **kwargs):
        return self._soco.mute()
    def volume(self, level=None, *args, **kwargs):
        if level:
            level = int(level)
        return self._soco.volume(level)
    def v(self, level=None, *args, **kwargs):
        "Alias for volume"
        return self.volume(level, *args, **kwargs)
    def track(self, *args, **kwargs):
        t = self._soco.get_current_track_info()
        return "{}: {} ({})".format(t['artist'], t['title'], t['album'])
    def t(self, *args, **kwargs):
        "Alias for track"
        return self.track(*args, **kwargs)
    def play_uri(self, uri=None, *args, **kwargs):
        if not uri:
            return
        return self._soco.play_uri(uri)
    def exit(self, *args, **kwargs):
        sys.exit(0)
    def q(self, *args, **kwargs):
        "Alias for exit"
        return self.exit()
    def status(self, *args, **kwargs):
        s = self._soco.get_speaker_info()
        info = {
            "UID": s['uid'],
            "Zone": s['zone_name'],
            "Hardware Version": s['hardware_version'],
            "Software Version": s['software_version'],
            "Serial": s['serial_number'],
            "MAC": s['mac_address'],
        }
        return "\n".join(["{}: {}".format(k,v) for k,v in info.items()])
    def artists(self, *args, **kwargs):
        start = 0
        max_items = 100
        if len(args) > 1:
            start = args[0]
            max_items = args[1]
        artists = self._soco.get_artists(start=start, max_items=max_items)
        return "\n".join([x.get('title') for x in artists.get('item_list')])
    def albums(self, *args, **kwargs):
        start = 0
        max_items = 100
        if len(args) > 1:
            start = args[0]
            max_items = args[1]
        albums = self._soco.get_albums(start=start, max_items=max_items)
        return "\n".join([x.get('title') for x in albums.get('item_list')])
    def tracks(self, *args, **kwargs):
        start = 0
        max_items = 100
        if len(args) > 1:
            start = args[0]
            max_items = args[1]
        tracks = self._soco.get_tracks(start=start, max_items=max_items)
        return "\n".join(["{} ({})".format(x.get('title'), x.get('id')) for x in tracks.get('item_list')])
    def add_to_queue(self, *args, **kwargs):
        if len(args) > 0:
            self._soco.add_to_queue(args[0])
    def remove_from_queue(self, *args, **kwargs):
        if len(args) > 0:
            self._soco.remove_from_queue(args[0])
    def clear_queue(self, *args, **kwargs):
            self._soco.clear_queue()
    def help(self, *args, **kwargs):
        return HELP_STR
    def h(self, *args, **kwargs):
        return self.help(*args, **kwargs)

def p(text=None, quote=''):
    with indent(2, quote):
        puts(colored.blue(text))

def find_controllers():
    dev = SonosDiscovery()
    for ip in dev.get_speaker_ips():
        s = SoCo(ip)
        zone = s.get_speaker_info()['zone_name']
        p("{}: {}".format(zone, ip))

def repl_control(ip=None):
    sonos = SoCo(ip)
    control = SonosController(sonos)
    while True:
        try:
            c = raw_input("> ")
            cmd = c.split()
            args = []
            if len(cmd) > 0:
                args = cmd[1:]
                cmd = cmd[0]
            try:
                m = getattr(control, cmd)
                o = m(*args)
                if o:
                    p(str(o))
            except AttributeError as e:
                print(e)
                p("Unknown command")
        except KeyboardInterrupt:
            break
        except EOFError:
            break

def main(ip=None):
    print(":: Sonos CLI ::")
    if not ip:
        find_controllers()
        ip = raw_input("Enter an IP to control from above: ")
    repl_control(ip)

if __name__=='__main__':
    try:
        ip = None
        if len(sys.argv) > 1: ip = sys.argv[1]
        main(ip)
    except KeyboardInterrupt:
        pass
