# liveclipping

This repository contains a simple command line tool to create clips from an AWS MediaLive stream using MediaPackage harvest jobs.

## Requirements
- Python 3.8+
- boto3 (``pip install boto3``)
- AWS credentials with permissions to create MediaPackage harvest jobs

## Usage

```bash
python live_clipping.py \
  --endpoint-id <origin_endpoint_id> \
  --start 2023-01-01T12:00:00 \
  --end 2023-01-01T12:01:00 \
  --bucket my-bucket \
  --manifest-prefix clips/myclip \
  --role-arn arn:aws:iam::111122223333:role/MediaPackageHarvest
```

This command creates a clip between the given start and end times. The resulting manifest and segments will be stored in the provided S3 bucket and prefix.

## Web Interface

A simple Flask application is included to create clips from a browser. Install
Flask and run the server:

```bash
pip install flask
python web_app.py
```

Then open `http://localhost:5000` in your browser. The page shows a video player
and a form to submit the start and end times along with other parameters. After
filling out the fields press "Create Clip" and the server will request a harvest
job from MediaPackage.

### Playing a local HLS stream

To test the interface with a locally hosted HLS manifest, start an HTTP server
in the directory containing your `.m3u8` and segment files:

```bash
cd /path/to/hls/files
python -m http.server 8000
```

Then launch the Flask app while specifying the local manifest URL via the
`VIDEO_URL` environment variable:

```bash
VIDEO_URL=http://localhost:8000/stream.m3u8 python web_app.py
```

Open `http://localhost:5000` and the player will load the stream from your
local server.
