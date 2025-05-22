import argparse
from datetime import datetime
import boto3


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a clip from a MediaPackage endpoint")
    parser.add_argument('--endpoint-id', required=True,
                        help='MediaPackage OriginEndpoint ID')
    parser.add_argument('--start', required=True,
                        help='Clip start time in ISO 8601 UTC format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('--end', required=True,
                        help='Clip end time in ISO 8601 UTC format (YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('--bucket', required=True,
                        help='S3 bucket for the harvested clip')
    parser.add_argument('--manifest-prefix', required=True,
                        help='Prefix for the clipped manifest key')
    parser.add_argument('--title', help='Optional clip title')
    parser.add_argument('--role-arn', required=True,
                        help='IAM Role ARN that MediaPackage uses to write to S3')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    return parser.parse_args()


def create_clip(args):
    start_time = datetime.fromisoformat(args.start)
    end_time = datetime.fromisoformat(args.end)
    client = boto3.client('mediapackage', region_name=args.region)
    if getattr(args, 'title', None):
        safe_title = args.title.replace(' ', '-')
        clip_id = f"{safe_title}-{int(datetime.utcnow().timestamp())}"
    else:
        clip_id = f"clip-{int(datetime.utcnow().timestamp())}"
    response = client.create_harvest_job(
        Id=clip_id,
        StartTime=start_time.isoformat()+"Z",
        EndTime=end_time.isoformat()+"Z",
        OriginEndpointId=args.endpoint_id,
        S3Destination={
            'BucketName': args.bucket,
            'ManifestKey': args.manifest_prefix,
            'RoleArn': args.role_arn,
        },
    )
    return response['HarvestJob']


def main():
    args = parse_args()
    job = create_clip(args)
    print('Created clip:', job['Id'])


if __name__ == '__main__':
    main()
