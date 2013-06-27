from pyechonest import config, song

API_KEY = "IN508SAUOJG7RW3DN"
URL = "http://developer.echonest.com/api/v4/track/upload"
FILETYPE = "mp3"
CODEGEN_PATH = "codegen"

def id_song(filename):
  metadata = {}
  config.ECHO_NEST_API_KEY = API_KEY
  song_info = song.identify(filename)
  metadata["title"]= song_info[0].title
  metadata["artist"] = song_info[0].artist_name
  
  #results = song.search(metadata["title"], metadata["artist"], 
                         #buckets=["tracks", "id:7digital-US"])[0]
  return metadata
