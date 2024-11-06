import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

with open('spotify_api_key.txt', 'r') as file:
    api_key = file.read().strip()
client_id = '68006493ebb54060b490b4654b84b6b5'
client_secret = api_key

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_ids = [
    '37i9dQZF1DWVY4eLfA3XFQ', 
    '7nppx7uLgcmkZHg70HNfOk', 
    '0TOtvml0WfdY0OK6hcB0uV', 
    '6yyFZPfg3pU3d3IHNpaNKI'
]  

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
            
            track_info = {
                'Track Name': track['name'],
                'Artist Name': track['artists'][0]['name'],
                'Popularity': track['popularity'],
                'Tempo': audio_features.get('tempo', 'NA'),
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

for playlist_id in playlist_ids:
    get_tracks_from_playlist(playlist_id)
df = pd.DataFrame(track_data)
df.to_csv('Top_Tech_House_Songs_From_Playlists.csv', index=False)
