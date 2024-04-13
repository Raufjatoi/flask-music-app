from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

# Route to serve static files from 'static2' directory
@app.route('/static2/<path:filename>')
def static2_files(filename):
    return send_from_directory('static2', filename)

# Route to serve static files from 'static3' directory
@app.route('/static3/<path:filename>')
def static3_files(filename):
    return send_from_directory('static3', filename)

# Route to serve static files from 'static4' directory
@app.route('/static4/<path:filename>')
def static4_files(filename):
    return send_from_directory('static4', filename)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Discover route
@app.route('/discover')
def discover():
    return render_template('discover.html')

# Albums route
@app.route('/albums')
def albums():
    return render_template('albums.html')

# Artist route
@app.route('/artist')
def artist():
    # You can add logic here to fetch data for artist.html if needed
    return render_template('artist.html')

# Route for creating music
@app.route('/create')
def create():
    return render_template('create.html')

# Route for handling form submission and displaying created music
@app.route('/cmusic', methods=['POST'])
def cmusic():
    title = request.form['title']
    artist = request.form['artist']
    genre = request.form['genre']
    # No need to save the music file, just retrieve the filename
    music_file = request.files['file']
    filename = music_file.filename if music_file else None

    return render_template('cmusic.html', title=title, artist=artist, genre=genre, filename=filename)

# Route for AI Tools page
@app.route('/ai')
def ai():
    return render_template('ai.html')

if __name__ == '__main__':
    app.run(debug=True)
