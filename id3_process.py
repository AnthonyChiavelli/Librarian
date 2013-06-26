from mutagen.id3 import ID3, TIT2
import os

def process_files(directory):
  #Recursively iterator over files
  for _, _,files in os.walk(directory):
    for f in files:
      #Construct complete path
      f = directory + "/" + f
      #Update metadata
      metadata = ID3(f)
      metadata.add(TIT2(encoding=3, text=u"Rick Astley"))
      metadata.save()

      
