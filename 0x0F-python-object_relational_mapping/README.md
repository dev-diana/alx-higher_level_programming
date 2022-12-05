# Object Relational Mapping in Python
- Linking two amazing worlds: Databases and Python!
- For the first part, I use the module MySQLdb to connect to a MySQL database and execute my SQL queries.
- In the second part, I use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

# Install MySQLdb module version 2.0.x
## For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

- $ sudo apt-get install python3-dev
- $ sudo apt-get install libmysqlclient-dev
- $ sudo apt-get install zlib1g-dev
- $ sudo pip3 install mysqlclient
- ...
- $ python3
- >>> import MySQLdb
- >>> MySQLdb.version_info 
- (2, 0, 3, 'final', 0)

# Install SQLAlchemy module version 1.4.x
- $ sudo pip3 install SQLAlchemy
- ...
- $ python3
- >>> import sqlalchemy
- >>> sqlalchemy.__version__ 
- '1.4.22'
