from flask import Flask, rendertemplate, sendfrom_directory, request, jsonify
import os

app = Flask(name)
VIDEO_FOLDER = 'static/videos'

@app.route('/')
def index():
    videos = []
    for filename in os.listdir(VIDEO_FOLDER):
        if filename.endswith('.mp4'):
            size = round(os.path.getsize(os.path.join(VIDEO_FOLDER, filename)) / (1024 * 1024), 2)
            videos.append({'name': filename, 'size': f"{size}MB"})
    return render_template('index.html', videos=videos)

@app.route('/play/<video_name>')
def play(video_name):
    return rendertemplate('player.html', videoname=video_name, external=False)

@app.route('/download/<video_name>')
def download(video_name):
    return sendfromdirectory(VIDEOFOLDER, videoname, as_attachment=True)

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = []
    for filename in os.listdir(VIDEO_FOLDER):
        if filename.endswith('.mp4') and query in filename.lower():
            size = round(os.path.getsize(os.path.join(VIDEO_FOLDER, filename)) / (1024 * 1024), 2)
            results.append({'name': filename, 'size': f"{size}MB"})
    return jsonify(results)

@app.route('/play_external')
def play_external():
    video_url = request.args.get('url')
    return rendertemplate('player.html', videourl=video_url, external=True)

if name == 'main':
    app.run(debug=True)