import tekore as tk
from time import sleep
import subprocess


output = subprocess.check_output('spotify')
client_id = 'c3206afd91c84c94a181946a015b554e'
client_secret = '620696b543224716a7193d25d1f19555'

app_token = tk.request_client_token(client_id, client_secret)
redirect_uri = 'https://example.com/callback'
spotify = tk.Spotify(app_token)
user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)
spotify.token = user_token


# token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
#
# spotify = tk.Spotify(token)
tracks = spotify.current_user_top_tracks()
print(tracks.items[0].id)
spotify.playback_resume()
spotify.playback_start_tracks([t.id for t in tracks.items])
# sleep(10
# spotify.playback_pause()
# finlandia = '3hHWhvw2hjwfngWcFjIzqr'
# spotify.playback_start_tracks([finlandia])