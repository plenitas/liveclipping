from types import SimpleNamespace
from flask import Flask, render_template, request, jsonify
from live_clipping import create_clip

app = Flask(__name__)


@app.route('/')
def index():
    # Replace with your HLS manifest URL
    video_url = 'https://example.com/stream.m3u8'
    return render_template('index.html', video_url=video_url)


@app.route('/clip', methods=['POST'])
def clip():
    data = request.get_json(force=True)
    try:
        args = SimpleNamespace(
            endpoint_id=data['endpoint_id'],
            start=data['start'],
            end=data['end'],
            bucket=data['bucket'],
            manifest_prefix=data['manifest_prefix'],
            title=data.get('title'),
            role_arn=data['role_arn'],
            region=data.get('region', 'us-east-1')
        )
        job = create_clip(args)
        return jsonify({'status': 'ok', 'job_id': job['Id']})
    except Exception as exc:
        return jsonify({'status': 'error', 'message': str(exc)}), 400


if __name__ == '__main__':
    app.run(debug=True)
