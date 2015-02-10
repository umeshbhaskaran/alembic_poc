# alembic_poc
POC on alembic database migration tool

# Installation

Install released versions of Alembic from the Python package index with pip or a similar tool:

pip install alembic

Installation via source distribution is via the setup.py script:

python setup.py install

The install will add the alembic command to the environment. All operations with Alembic then proceed through the usage of this command.

# Dependencies

Alembic’s install process will ensure that SQLAlchemy is installed, in addition to other dependencies. Alembic will work with SQLAlchemy as of version 0.7.3. The latest version of SQLAlchemy within the 0.7, 0.8, or more recent series is strongly recommended.

Alembic supports Python versions 2.6 and above.

#Project Status

Alembic is currently in beta status and is expected to be fairly stable. Users should take care to report bugs and missing features (see Bugs) on an as-needed basis. It should be expected that the development version may be required for proper implementation of recently repaired issues in between releases; the latest master is always available at https://bitbucket.org/zzzeek/alembic/get/master.tar.gz.

#Community Support

Alembic is developed by Mike Bayer, and is loosely associated with the SQLAlchemy and Pylons projects.

User issues, discussion of potential bugs and features should be posted to the Alembic Google Group at sqlalchemy-alembic.

Bugs and feature enhancements to Alembic should be reported on the Bitbucket issue tracker.
