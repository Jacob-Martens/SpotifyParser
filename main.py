import json

class ArtistRecord:
    def __init__(self):
        self.artist = ""
        self.songs = []
        self.play_count = []

with open('./Streaming_History_Audio_2022-2023_1.json', encoding="utf8") as f:
    raw_json = json.load(f)

unique_artists = []
artist_records = []

for entry in raw_json:
    index = -1
    new_record = ArtistRecord()
    
    cur_artist = entry['master_metadata_album_artist_name']
    cur_song = entry['master_metadata_track_name']
    
    if cur_artist not in unique_artists:
        unique_artists.append(cur_artist)
        new_record.artist = cur_artist
        artist_records.append(new_record)
    else:
        index = unique_artists.index(cur_artist)
    
    if cur_song not in artist_records[index].songs:
        artist_records[index].songs.append(cur_song)
        artist_records[index].play_count.append(1)
    else:
        song_index = artist_records[index].songs.index(cur_song)
        artist_records[index].play_count[song_index] += 1
        
    

for record in artist_records:
    print(record.artist)
    
    for track, count in zip(record.songs, record.play_count):
        print("\t" + str(track) + "\t" + str(count))
    