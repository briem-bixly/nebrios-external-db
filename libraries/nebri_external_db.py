from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


def connect(db, db_name, db_ip, port, username=None, password=None):
    if username is not None and password is not None:
        url = '%s://%s:%s@%s:%s/%s' % (db, username, password, db_ip, port, db_name)
    else:
        url = '%s://%s:%s/%s' % (db, db_ip, port, db_name)
    engine = create_engine(url, echo=True)
    Session = sessionmaker(bind=engine)
    return Session
