CREATE TABLE "User" (
    username VARCHAR(15) PRIMARY KEY,
    first_name VARCHAR(10),
    last_name VARCHAR(10),
    email VARCHAR(30)
);

CREATE TABLE Playlist (
    playlist_id INT PRIMARY KEY,
    playlist_name VARCHAR(15),
    category VARCHAR(10), 
    creator_username VARCHAR(15),
    FOREIGN KEY (creator_username) REFERENCES "User"(username)
);

CREATE TABLE Album (
    album_id INT PRIMARY KEY,
    year_of_release INT, 
    title VARCHAR(15),
    genre VARCHAR(10),
    podcast_or_music VARCHAR(10)
);

CREATE TABLE Artist (
    artist_id INT PRIMARY KEY,
    artist_name VARCHAR(15),
    country VARCHAR(10),
    UNIQUE(artist_name )
);

CREATE TABLE Track (
    track_id INT PRIMARY KEY,
    track_name VARCHAR(15),
    artist_name VARCHAR(15), 
    foreign key (artist_name) REFERENCES Artist(artist_name),
    duration INT,
    album_id INT,
    FOREIGN KEY (album_id) REFERENCES Album(album_id)
);

CREATE TABLE Releases (
    artist_id INT,
    album_id INT,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (album_id) REFERENCES Album(album_id),
    PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE PlaylistTrack (
    playlist_id INT,
    track_id INT,
    FOREIGN KEY (playlist_id) REFERENCES Playlist(playlist_id),
    FOREIGN KEY (track_id) REFERENCES Track(track_id),
    PRIMARY KEY (playlist_id, track_id)
);

INSERT INTO "User" (username, first_name, last_name, email)
VALUES
    ('ansab10', 'Ansab', 'Aalim', 'aalim.ansab@email.com'),
    ('adnanmd17', 'Adnan', 'Mohammed', 'adnanmohammed310@gmail.com'),
    ('ansh6', 'Ansh', 'Aggarwal', 'aggarwal.ansh@email.com'),
    ('safal12', 'Safal', 'Mehrotra', 'mehrotra.safal@email.com'),
    ('ishaan15', 'Ishaan', 'Manhaas', 'manhaas.ishaan@email.com');

INSERT INTO Album (album_id, year_of_release, title, genre, podcast_or_music)
VALUES
    (1, 2020, 'Summer Vibes', 'Pop', 'Music'),
    (2, 2019, 'Greatest Hits', 'Rock', 'Music'),
    (3, 2021, 'Piano Beats', 'Classical', 'Music'),
    (4, 2018, 'Hip Hop Jazz', 'Hip Hop', 'Music'),
    (5, 2023, 'Motivation', 'Talks', 'Podcast'),
    (6, 2022, 'Jazz Nights', 'Jazz', 'Music'),
    (7, 2022, 'Paranormal', 'Talks', 'Podcast'),
    (8, 2016, 'Electronic Dope', 'Electronic', 'Music'),
    (9, 2015, 'R&B Soul', 'R&B', 'Music'),
    (10, 2024, 'Indie Vibes', 'Indie', 'Music');

INSERT INTO Artist (artist_id, country, artist_name)
VALUES
    (1, 'USA', 'Alicia Keys'),
    (2, 'UK', 'Coldplay'),
    (3, 'Germany', 'Tangerine Dream'),
    (4, 'Canada', 'Drake'),
    (5, 'Australia', 'Keith Urban'),
    (6, 'Brazil', 'Antonio Carlos'),
    (7, 'Sweden', 'Avicii'),
    (8, 'Ireland', 'Hozier'),
    (9, 'France', 'Stromae'),
    (10, 'India', 'KK Singh');
     
INSERT INTO Track (track_id, track_name, artist_name, duration, album_id)
VALUES
    (1, 'Sunset Shines', 'Alicia Keys', 240, 1),
    (2, 'Highway Nowhere','Coldplay', 210, 2),
    (3, 'Moonlight Rays', 'Tangerine Dream',360, 3),
    (4, 'Rap God','Drake', 300, 4),
    (5, 'Monday Travel','Keith Urban', 270, 5),
    (6, 'Smooth Jazz','Antonio Carlos', 320, 6),
    (7, 'Bhangarh Talks', 'Avicii',280, 7),
    (8, 'Folklore','Hozier', 330, 8),
    (9, 'Soulful Seren','Stromae', 290, 9),
    (10, 'Indie Anthem','KK Singh', 250, 10);
    

INSERT INTO Playlist (playlist_id, playlist_name, category, creator_username) 
VALUES
    (101, 'Chill Mix', 'Party', 'ansab10'),
    (102, 'Workout Beats', 'Gym', 'ansab10'),
    (103, 'Party Jams', 'Party', 'adnanmd17'),
    (104, 'Study Session', 'Study', 'ansh6'),
    (105, 'Road Trip', 'Personal', 'safal12'),
    (106, 'Throwback Hits', 'Personal', 'ishaan15'),
    (107, 'Relaxing Piano', 'Relax', 'ansab10'),
    (108, 'Country Vibes', 'Personal', 'ansh6'),
    (109, 'Rock Anthems', 'Party', 'safal12'),
    (110, 'Pop Sensations', 'Party', 'adnanmd17');

INSERT INTO PlaylistTrack (playlist_id, track_id)
VALUES
    (101, 1),
    (101, 3),
    (102, 4),
    (102, 5),
    (103, 6),
    (103, 7),
    (104, 8),
    (104, 9),
    (105, 10),
    (105, 2),
    (106, 3),
    (106, 6),
    (107, 7),
    (107, 9),
    (108, 1),
    (108, 4),
    (109, 2),
    (109, 5),
    (110, 8),
    (110, 10);
    
INSERT INTO Releases (artist_id, album_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);