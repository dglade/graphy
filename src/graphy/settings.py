import os
import yaml

with open(os.environ.get('GRAPHY_CONFIG_FILE')) as f:
    config = yaml.safe_load(f.read())

metra_auth = (config.get('accessKey'), config.get('secretKey'))
metra_base_url = 'https://gtfsapi.metrarail.com'

