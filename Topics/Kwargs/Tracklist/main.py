def tracklist(**kwargs):
    for artist in kwargs:
        print(artist)
        for album, track in kwargs[artist].items():
            print('ALBUM:', album, 'TRACK:', track)
