import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get list of snapshot IDs used in existing volumes
    volume_snapshots = [
        vol['SnapshotId'] for vol in ec2.describe_volumes()['Volumes']
        if 'SnapshotId' in vol
    ]
    
    # Get all snapshots owned by the account
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        
        if snapshot_id not in volume_snapshots:
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted: {snapshot_id}")
            except Exception as e:
                print(f"Failed to delete {snapshot_id}: {e}")
