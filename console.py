import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Green Day",30)
artist_repository.save(artist1)

artist2 = Artist("blink182",29)
artist_repository.save(artist1)

album1 = Album("dookie",artist1,"punk")
album_repository.save(album1)
album2 = Album("nimrod",artist1,"punk")
album_repository.save(album2)
album3 = Album("american idiot",artist1,"punk")
album_repository.save(album3)
album4 = Album("enema of the state",artist1,"punk")
album_repository.save(album4)
album5 = Album("california",artist2,"rock")
album_repository.save(album5)

# for album in album_repository.select_all():
#      print(album.__dict__)



pdb.set_trace()
