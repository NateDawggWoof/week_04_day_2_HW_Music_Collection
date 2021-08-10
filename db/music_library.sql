DROP TABLE albums;
DROP TABLE artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    age INT

);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    album_name VARCHAR (255),
    genre VARCHAR (255),
    artist_id INT REFERENCES artists(id)
);
