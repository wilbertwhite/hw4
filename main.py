import flask
import os

app = flask.Flask(__name__)

@app.route("/")
def index():
    shows = ["Bojack", "Kaiji", "Arcane", "Naruto", "One Piece"]
    photos = [
        "https://m.media-amazon.com/images/M/MV5BYWQwMDNkM2MtODU4OS00OTY3LTgwOTItNjE2Yzc0MzRkMDllXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg", 
        "https://image.myanimelist.net/ui/O8As4Owaeopr38cOJiaKo3HkVyuhYeZtekNwngfwLTvPsCIxIXVTZOz6xSg3u5wqof8V_mkpocXIU5V89qjnYtABVYaWPub-d3u6NhmedUVHpE1E3pAlWsj1nSm5axSI", 
        "https://m.media-amazon.com/images/M/MV5BYmU5OWM5ZTAtNjUzOC00NmUyLTgyOWMtMjlkNjdlMDAzMzU1XkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg",
        "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",
        "https://m.media-amazon.com/images/M/MV5BODcwNWE3OTMtMDc3MS00NDFjLWE1OTAtNDU3NjgxODMxY2UyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg"
    ]
    return flask.render_template(
        "index.html",
        len = len(shows), 
        shows = shows,
        pLen = len(photos),
        photos = photos
    )

app.run(debug=True)