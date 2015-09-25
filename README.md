# Nebrios External Database

This app is intended for use with a Nebri instance. Visit https://nebrios.com to sign up for free!

<h2>Setup</h2>
This app requires very little in terms of setup. Please ensure that all files are placed in the correct places over SFTP. `libraries/nebri_external_db.py` should be copied to /libraries.

<h2>Requirements</h2>
This app requires the use of sqlalchemy. SSH into your Nebri instance and install via pip:
```
pip install sqlalchemy
```

<h2>Examples</h2>
```
from nebri_external_db import connect
Session = connect('db_type', 'db_name', 'db_ip', 'port', 'username', 'password')
session = Session()
# do stuff with the db
```
- db_type: the database you want to use, i.e. for MySQL, db_type would be 'mysql'
- db_name: the name of the database you want to connect to
- db_ip: the ip address of the server that the database is being served from
- port: the port to connect to
- username (optional): the user you would like to connect to the database as
- password (optional): the password for the given user

<strong>HINT</strong>: if your database requires an ssh tunnel, pair this app with https://github.com/nebrie/nebri-ssh.
