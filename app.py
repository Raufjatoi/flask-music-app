from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/static2/<path:filename>')
def static2_files(filename):
    return send_from_directory('static2', filename)

@app.route('/static3/<path:filename>')
def static3_files(filename):
    return send_from_directory('static3', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/albums')
def albums():
    return render_template('albums.html')

@app.route('/artist')
def artist():
    # You can add logic here to fetch data for artist.html if needed
    return render_template('artist.html')

if __name__ == '__main__':
    app.run(debug=True)
