from mutagen.id3 import ID3, TIT2, TPE1
import os
import identify

def process_files(directory):
  #Recursively iterator over files
  for _, _,files in os.walk(directory):
    for f in files:
      if (not "mp3" in f): continue
      #Get correct metadata
      f = directory + "/" + f
      correct_metadata = identify.id_song(f)
      #Update metadata
      old_metadata = ID3()
      old_metadata.add(TIT2(encoding=3, text=correct_metadata["title"]))
      old_metadata.add(TPE1(encoding=3, text=correct_metadata["artist"]))
      old_metadata.save(f)
      



      
