from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (album_name, artist_id, genre) VALUES (%s, %s, %s) RETURNING *" 
    values = [album.album_name, album.artist.id, album.genre]
    results = run_sql(sql,values)
    id = results[0]['id']
    album.id = id 
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)



def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['album_name'], artist, result['genre'], result['id'])

    return album


def delete(id):
    sql ="DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def select_all():
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)


    for row in results:
        artist = artist_repository.select(row['artist_id'])
        print(artist)
        album = Album(row['album_name'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums 

def update(album):
    sql = "UPDATE albums SET (album_name, artist_id, genre)= (%s, %s, %s) WHERE id = %s"
    values = [album.album_name, album.artist.id, album.genre, album.id]
    run_sql(sql, values)

