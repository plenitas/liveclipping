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

The web page shows the current playback time when you hover over the video.
Click **Set Start Here** and **Set End Here** to mark the boundaries with
frame‑level precision and optionally provide a title for the clip. The
**Preview Clip** button plays back just the selected range so you can verify the
cut before creating it.
