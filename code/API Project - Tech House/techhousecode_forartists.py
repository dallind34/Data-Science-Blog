import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

with open('spotify_api_key.txt', 'r') as file:
    api_key = file.read().strip()
client_id = '68006493ebb54060b490b4654b84b6b5'
client_secret = api_key


auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

artists = []  

playlist_ids = ['37i9dQZF1DWVY4eLfA3XFQ', '7nppx7uLgcmkZHg70HNfOk', '0TOtvml0WfdY0OK6hcB0uV', '6yyFZPfg3pU3d3IHNpaNKI']  
unique_track_ids = set()
track_data = []

def get_tracks_from_playlist(playlist_id):
    print(f"\nGetting tracks from playlist ID: {playlist_id}\n")
    
    results = sp.playlist_tracks(playlist_id)
    for item in results['items']:
        track = item['track']
        track_id = track['id']
        
        if track_id not in unique_track_ids:
            unique_track_ids.add(track_id)
            
            audio_features = sp.audio_features(track_id)[0]
            
            tempo = audio_features.get('tempo', 0)
            if 119 <= tempo <= 140:
                track_info = {
                    'Track Name': track['name'],
                    'Artist Name': track['artists'][0]['name'],
                    'Popularity': track['popularity'],
                    'Tempo': tempo,
                    'Energy': audio_features.get('energy', 'NA'),
                    'Danceability': audio_features.get('danceability', 'NA'),
                    'Liveness': audio_features.get('liveness', 'NA'),
                    'Loudness': audio_features.get('loudness', 'NA'),
                    'Acousticness': audio_features.get('acousticness', 'NA'),
                    'Instrumentalness': audio_features.get('instrumentalness', 'NA'),
                    'Speechiness': audio_features.get('speechiness', 'NA'),
                    'Valence': audio_features.get('valence', 'NA'),
                    'Key': audio_features.get('key', 'NA'),
                    'Mode': 'Major' if audio_features.get('mode', 'NA') == 1 else 'Minor',
                    'Time Signature': audio_features.get('time_signature', 'NA'),
                    'Duration (ms)': audio_features.get('duration_ms', 'NA')
                }
                track_data.append(track_info)
            else:
                print(f"Skipping track '{track['name']}' due to tempo {tempo} BPM.")

for playlist_id in playlist_ids:
    get_tracks_from_playlist(playlist_id)
for artist in artists:
    print(f"\nGetting top tracks for {artist} (excluding remixes)...\n")

    artist_search = sp.search(q=f'artist:{artist}', type='artist', limit=1)
    if artist_search['artists']['items']:
        artist_id = artist_search['artists']['items'][0]['id']
        
        top_tracks = sp.artist_top_tracks(artist_id, country='US')
    
        filtered_tracks = [track for track in top_tracks['tracks'] if 'remix' not in track['name'].lower()]
    
        track_ids = [track['id'] for track in filtered_tracks[:10]]
        audio_features = sp.audio_features(tracks=track_ids)
        for idx, feature in enumerate(audio_features):
            track_id = filtered_tracks[idx]['id']
            
            if track_id not in unique_track_ids:
                unique_track_ids.add(track_id)
                tempo = feature.get('tempo', 0)
                if 119 <= tempo <= 140:
                    track_info = {
                        'Track Name': filtered_tracks[idx]['name'],
                        'Artist Name': filtered_tracks[idx]['artists'][0]['name'],
                        'Popularity': filtered_tracks[idx]['popularity'],
                        'Tempo': tempo,
                        'Energy': feature.get('energy', 'NA'),
                        'Danceability': feature.get('danceability', 'NA'),
                        'Liveness': feature.get('liveness', 'NA'),
                        'Loudness': feature.get('loudness', 'NA'),
                        'Acousticness': feature.get('acousticness', 'NA'),
                        'Instrumentalness': feature.get('instrumentalness', 'NA'),
                        'Speechiness': feature.get('speechiness', 'NA'),
                        'Valence': feature.get('valence', 'NA'),
                        'Key': feature.get('key', 'NA'),
                        'Mode': 'Major' if feature.get('mode', 'NA') == 1 else 'Minor',
                        'Time Signature': feature.get('time_signature', 'NA'),
                        'Duration (ms)': feature.get('duration_ms', 'NA')
                    }
                    track_data.append(track_info)
                else:
                    print(f"Skipping track '{filtered_tracks[idx]['name']}' due to tempo {tempo} BPM.")
            else:
                print(f"Skipping duplicate track '{filtered_tracks[idx]['name']}'.")

    else:
        print(f"Artist {artist} not found.")

df = pd.DataFrame(track_data)

df.to_csv('Top_Tech_House_Songs.csv', index=False)
