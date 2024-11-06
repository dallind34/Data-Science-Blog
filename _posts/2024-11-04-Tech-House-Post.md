---
layout: post
title:  "Tech House Playlist Analysis and Spotify API"
author: Dallin Draper
description: In this post, I teach you how to use the Spotify API to collect data from popular tech house songs and analyze which features contribute to their success on playlists. I break down the process step-by-step and explore key elements like Danceability, Energy, and Speechiness to understand what makes a track stand out. 
image: "/assets/images/dj.jpg"
---


# What is Tech House?

Tech house is a genre that blends the danceable beats of classic house music with the darker, more minimalistic genre techno. The main features of the genre are deep basslines, classic house rhythms, and catchy vocal samples. It’s also somewhat formulaic, with most tracks moving through buildups to create tension and bass drops to keep energy high. As someone who makes tech house music, the formulaic nature of the genre is exactly why I wanted to analyze it to see which elements really make a track stand out.


# Motivating Question

The main question I am hoping to answer with this analysis is: What features of a tech house song contribute most to its success on Spotify playlists? By analyzing a dataset of songs from 3 of the most popular tech house Spotify playlists, I hope to find out which musical elements are most associated with a song's popularity. This knowledge could help producers and offer insights into how specific musical features might enhance a tech house song's chances of climbing the ranks of tech house Spotify playlists. 


# Data Collection & Tutorial

## Ethics

I used the official Spotify API, which is an approved way to access Spotify’s music data without any sketchy workarounds. By sticking to Spotify’s usage policies, I was able to pull detailed info on audio features for tech house tracks while staying within their terms of service. This approach let me gather the data I needed responsibly, without any unauthorized scraping or misuse.

Here’s a step-by-step guide on using the Spotify API to create a custom dataset. I gathered my dataset using this process:

## Packages

In Python, I used requests to interact with the Spotify API, pandas to structure and analyze the data, and json to handle Spotify’s JSON data format. Using these packages made it easy to request, process, and store data for analysis.

### Step 1:Set Up a Spotify Developer Account

- Go to the Spotify Developer Dashboard and log in or create a Spotify account.

- In the dashboard, create a new application to access your API credentials, which include your Client ID and Client Secret. Keep these secure, as they allow access to the API.

### Step 2: Authenticate and Get an Access Token

Use the requests library in Python to exchange your credentials for an access token. This token will be used to authorize your data requests.

Here’s some example code:

    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    import pandas as pd

    # Replace these with your own Spotify API credentials
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

### Step 3: Choose a Playlist and Get Data

- Use the playlist’s unique ID in your URL to access track data. 

- Use the /playlists/{playlist_id}/tracks endpoint to retrieve track information and /audio-features for detailed audio metrics.

Here's some example code:

    playlist_id = 'YOUR_PLAYLIST_ID'
    base_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    response = requests.get(base_url, headers=headers)
    tracks = response.json()

### Step 4: Get Features From Each Track

- For each track, use its unique track ID to request additional details from the /audio-features endpoint.

- This allowed me to access audio features for each song such as Tempo, Danceability, Energy, Loudness, Valence, and Speechiness.

        track_id = 'YOUR_TRACK_ID'
        features_url = f'https://api.spotify.com/v1/audio-features/{track_id}'
    
### Step 5: Organize the Data

- Store the data in a structured format using a pandas DataFrame, then save it as a CSV for further analysis.

        import pandas as pd

        data = {'Track Name': track_name, 'Tempo': tempo, 'Danceability': danceability, ...}
        df = pd.DataFrame(data)
        df.to_csv('tech_house_tracks.csv', index=False)


# Variable Information

Danceability: Measures how suitable a track is for dancing, based on elements like tempo, rhythm stability, and beat strength.

Energy: Captures the intensity and activity of the track, with higher values indicating more energetic songs.

Loudness: Average loudness in decibels (dB).

Tempo: The track’s speed measured in beats per minute (BPM) (typically around 120-130 BPM for tech house).

Valence: Measures the mood of the track. Higher values indicate happier or more upbeat tones, while lower values suggest darker tones.

Speechiness: Assesses the presence of spoken words or vocal samples in the track. Tracks with more spoken elements can have a higher speechiness score.


# Analysis
 
To get a sense of the musical characteristics shared by the most popular tech house songs on Spotify’s top playlists, I looked at some basic statistics:

Most Popular Key: The most common key among these top tracks was C♯ / D♭. This is a very low key for house music and is consistent with the idea that tech house focuses on deep basslines.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/key.jpg" alt="">
</figure>

Average Tempo: The average tempo for these tracks is around 128 BPM. My inital assumption that the average house song would be around 124 BPM so tech house might be slightly faster.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/tempo.jpg" alt="">
</figure>

Most Popular Mode: Major mode was the most common among these songs. This really surprised me and I amost wonder if the Spotify data is correct because most tech house songs I know are in minor or phrygian. 


## Exploratory Data Analysis (EDA)

### Linear Regression Model
  
I first tried a linear regression model to predict popularity using features like Danceability, Energy, and Speechiness. However, the model didn’t perform well, with an R-squared of just 0.03, meaning it could only explain 3% of the variation in popularity. This suggests that the relationship between these features and popularity is more complex and likely non-linear.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/linear_regression.jpg" alt="">
</figure>


### Random Forest Model

The Random Forest model performed better and showed a higher R-squared. This improvement supports the idea that non-linear relationships exist between the features and popularity within these curated playlists.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/Forest2.jpg" alt="">
</figure>


### Feature Importances

The feature importance plot from the Random Forest model highlighted Danceability, Energy, and Speechiness as the most influential features in determining a song’s popularity:

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/forest.jpg" alt="">
</figure>


# Conclusion

Using the Spotify API was a simple way to get detailed data on tech house tracks. My analysis showed that Danceability, Speechiness, and Energy play big roles in a song’s popularity. Tracks with strong beats and catchy vocal hooks tend to perform better on playlists. For tech house fans or producers, it’s cool to see which elements can make a track stand out!

## Links
[Spotify API](https://developer.spotify.com/documentation/web-api)

[History of Tech House](https://www.beatportal.com/articles/60692-beatports-definitive-history-of-tech-house)

[Tech House Groovy Bangers Spotify Playlist](https://open.spotify.com/playlist/0TOtvml0WfdY0OK6hcB0uV?si=3670ea226919484f)

## Note
All code for this project can be found in my github repository under my Data Science Blog in a folder called Code.

My dataset can also be found here.

[Link To Code Repository](https://github.com/dallind34/Data-Science-Blog/tree/main/code/API%20Project%20-%20Tech%20House)