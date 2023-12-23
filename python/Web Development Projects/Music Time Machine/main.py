import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

desired_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = f"https://www.billboard.com/charts/hot-100/{desired_date}/"

billboard_web = requests.get(URL).text
soup = BeautifulSoup(billboard_web, "html.parser")
all_songs = soup.find_all(id='title-of-a-story', name='h3', class_ ='a-no-trucate')
songs = [song.getText().replace('\n','').replace('\t','') for song in all_songs]

sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id="76c64154e36c4d0f8c4849ce0932ded3",
            client_secret="b9cf2c55d1084843a78633f70e17a67a",
            show_dialog=True,
            cache_path="token.txt",
            username="Siqi Li", 
    )
)

user_id = sp.current_user()['id']

my_playlist = sp.user_playlist_create(user_id, f"{desired_date} Billboard 100", public=False, collaborative=False, description='')

year = desired_date.split('-')[0]

# Get song URIs
uris = []
for song in songs:
    results = sp.search(f"track:{song} year:{year}", type='track')
    try:
        uri = results['tracks']['items'][-1]['uri']
        uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Add song URIs into playlist
sp.playlist_add_items(my_playlist['id'], uris, position=None)



