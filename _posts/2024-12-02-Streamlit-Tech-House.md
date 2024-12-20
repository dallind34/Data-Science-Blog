---
layout: post
title:  "Data Meets Dance: Exploring Tech House Data Using Streamlit"
author: Dallin Draper
description: This post explores the characteristics that make tech house tracks successful, focusing on insights like the importance of danceability, energy, and tempo. It introduces an interactive Streamlit app where users can filter, visualize, and rank tracks to uncover trends and gain a deeper understanding of what defines popular tech house music. 
image: "/assets/images/header4.jpg"
---

# Recap

In my previous blog post, I set out to answer the question: What features of a tech house song contribute most to its success on Spotify playlists? Using the Spotify API, I collected data on audio features from tracks featured on popular tech house playlists. My initial analysis highlighted trends like average tempo and key distributions, and I built a random forest model to predict track popularity based on these features. This post builds on those findings, focusing on key insights and introducing an interactive Streamlit app that lets users explore the data in depth.

# Importance of Danceability, Energy, and Speechiness

A Random Forest model revealed that Danceability, Energy, and Speechiness are the top three features influencing a track's popularity on Spotify. These features consistently emerged as the most important predictors and significantly outweighed others like Valence or Tempo.

## Visualizations

Below is a feature importance plot from the Random Forest model:

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/forest.jpg" alt="">
</figure>

The plot illustrates that Danceability has the highest importance score, followed by Energy and Speechiness. Together, these three features explain much of the variance in popularity scores compared to other audio features.

## Interpretation

Danceability: Tracks that are easier to dance to, with stable rhythms and strong beats, naturally appeal to tech house fans who prioritize groove and flow in music.

Energy: High-energy tracks are more engaging and dynamic, often leading to better reception in clubs and playlists.

Speechiness: Vocal samples or spoken-word elements add a unique character to tracks, making them stand out and more memorable to listeners.

These findings suggest that tech house producers aiming for playlist success should prioritize making tracks with high danceability, energetic beats, and catchy vocal elements.

# Common Musical Characteristics

## Key and Tempo

A closer look at the dataset revealed that the most popular key among tech house tracks is C♯ / D♭, and the average tempo is approximately 128 BPM. 

## Visualizations

Below are histograms showcasing the distribution of keys and tempos for the analyzed tracks:

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/key.jpg" alt="">
</figure>

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/tempo.jpg" alt="">
</figure>


The key histogram shows a clear preference for the C♯ / D♭ key, while the tempo histogram illustrates that most tracks cluster around 128 BPM, with few outliers.

## Interpretation

Key: The preference for C♯ / D♭ aligns with tech house's deep and resonant basslines, which often define the genre's aesthetic.
Tempo: The average tempo of 128 BPM falls within the expected range for tech house, striking a balance between energy and groove.

For music producers, this insight is valuable when deciding on the key and tempo of a track to ensure it aligns with the expectations of tech house listeners and playlist curators.


# Introducing the Tech House Song Analysis Streamlit App

## Purpose of the App

[The Tech House Analysis Dashboard](https://appapp-rheflqbfwscekp7ju7itzz.streamlit.app/) is an interactive tool designed to explore the audio and popularity features of tech house tracks collected from Spotify playlists. This app allows users to uncover trends and patterns in key musical elements like tempo, energy, and danceability that contribute to a song's success in this genre. 

Access the app here: (https://appapp-rheflqbfwscekp7ju7itzz.streamlit.app/)

# What Can This App Do?

The app is divided into four sections, each can be accessed in the dropdown menu.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/dropdown.jpg" alt="">
</figure>

## Dataset Overview:

Automatically displays the filtered dataset based on user-selected keys and tempo ranges.
Users can view all relevant track details, such as artist name, tempo, energy, danceability, speechiness, and popularity.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/dataset.jpg" alt="">
</figure>

## Key and Tempo Insights:

Visualize the distribution of musical keys in the dataset using a bar chart.
Explore the tempo distribution of tracks with an interactive histogram.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/dist.jpg" alt="">
</figure>

## Feature Exploration:

Select a specific audio feature (e.g., energy, danceability, valence, or speechiness) to analyze its distribution across the dataset.
The dynamic histogram provides a deeper understanding of how these features vary among tracks.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/feature.jpg" alt="">
</figure>

## Dynamic Song Ranking:

Rank songs based on any selected feature (e.g., popularity, energy, or danceability).
Adjust the number of songs displayed using a slider and view the ranked results in a table.
Explore the top-ranked tracks and their respective artists to gain insights into standout performers.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/ranking.jpg" alt="">
</figure>

# Exploring the Sidebar Features

The sidebar in the Tech House Song Analysis Dashboard provides users with filtering tools to customize their exploration of the dataset. By adjusting the filters in the sidebar, users can narrow down the data to focus on specific keys or bpms of interest. The sidebar filters apply globally across all sections of the app.

<figure>
    <img src= "https://dallind34.github.io/Data-Science-Blog/assets/images/sidebar.jpg" alt="">
</figure>

## What the Sidebar Can Do

### Filter by Key:

Use the menu to choose one or more musical keys to filter the dataset.
For example, selecting "C♯ / D♭" and "A" will restrict the dataset to only tracks in these keys.

### Filter by Tempo Range:

Adjust the slider to specify a tempo range (in beats per minute or BPM).
For exaple, setting the range to 120–128 BPM will show only tracks within this tempo range.

# Conclusion

The Tech House Song Analysis Dashboard demonstrates the power of combining data and interactivity to uncover meaningful insights about what makes tech house tracks successful. With features like dynamic filtering, visualizations, and song rankings, the app empowers users to explore key musical elements like danceability, tempo, and energy at their own pace. Whether you're a producer fine-tuning your next track or a fan curious about the genre's defining traits, the dashboard provides a hands-on way to dive into the data.

Ready to explore the beats and patterns that drive tech house? Try the app now and uncover your own insights! Click [here](https://appapp-rheflqbfwscekp7ju7itzz.streamlit.app/) to start your journey into data-driven music exploration.

## Note

All code for this project can be found in my github repository under my Data Science Blog in a folder called Code.

My dataset can also be found here.

[Link To Code Repository and Data](https://github.com/dallind34/Data-Science-Blog/tree/main/code/API%20Project%20-%20Tech%20House)

[Link To Streamlit App Repository](https://github.com/dallind34/Tech_House_Streamlit)

[Link To The Streamlit App](https://appapp-rheflqbfwscekp7ju7itzz.streamlit.app/)

## Playlists That Were Used For Data

[Tech House 2024](https://open.spotify.com/playlist/7nppx7uLgcmkZHg70HNfOk?si=ea865142872049e8)

[Tech House Groovy Bangers](https://open.spotify.com/playlist/0TOtvml0WfdY0OK6hcB0uV?si=4b0995f26c254200)

[Tech House 2024 2](https://open.spotify.com/playlist/6jCgabXrYUjqdaF0ozKkTj?si=44aef1bd236e432c)