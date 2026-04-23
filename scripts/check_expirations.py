import yaml, datetime
from pathlib import Path

config_path = Path(__file__).parent.parent / 'config' / 'user_accounts.yaml'

# Open & Read user_accounts.yaml
with open(config_path, 'r') as f:
    user_accounts = yaml.safe_load(f)

# Compare User's Expiration Date to Current Date
# Print & Write to log whether each user is ACTIVE or EXPIRED/REVOKED
# For Active Users, print & write how many days until expiration
with open(Path(__file__).parent.parent / 'logs' / 'expiration_status.log', 'a') as log_file:
    log_file.write(f"Expiration Check - {datetime.datetime.now().date()}\n")
    for user in user_accounts['users']:
        if user['expiration_date'] < datetime.datetime.now().date():
            print(f"{user['username']} is EXPIRED/REVOKED")
            log_file.write(f"{datetime.datetime.now()}: {user['username']} is EXPIRED/REVOKED\n")
        else:
            days_until_expiration = (user['expiration_date'] - datetime.datetime.now().date()).days
            print(f"{user['username']} is ACTIVE, expires in {days_until_expiration} days")
            log_file.write(f"{datetime.datetime.now()}: {user['username']} is ACTIVE, expires in {days_until_expiration} days\n")
