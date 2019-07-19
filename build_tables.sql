
CREATE TABLE IF NOT EXISTS top_tracks (
    id INT AUTO_INCREMENT,
    track VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    playcount INT NOT NULL,
    date DATE,
    PRIMARY KEY (id)
)
CREATE TABLE IF NOT EXISTS top_artists (
    id INT AUTO_INCREMENT,
    artist VARCHAR(255) NOT NULL,
    playcount INT NOT NULL,
    date DATE,
    PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS listen_history(
    id INT AUTO_INCREMENT,
    track VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    date DATETIME,
    PRIMARY KEY (id)
)
