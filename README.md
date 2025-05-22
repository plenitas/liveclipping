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
  --duration 60 \
  --bucket my-bucket \
  --manifest-prefix clips/myclip \
  --role-arn arn:aws:iam::111122223333:role/MediaPackageHarvest
```

This command creates a 60 second clip starting at the specified time. The resulting manifest and segments will be stored in the provided S3 bucket and prefix.
