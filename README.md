# alembic_poc
POC of alembic database migration tool

# Steps for handling migration
1. Make changes to your model --> alembic_poc/models/skills.py
2. Navigate to the folder where alembic is initialized or where alembic.ini is available --> alembic_poc/migration/ in this case.
3. Run the command -- > alembic revision --autogenerate -m <your_comment>.
    1. This will generate the migration file <version_your_comment.py> under the folder alembic_poc/migration/alembic/versions.
4. Offline migration.
    1. When we need to run migration in offline mode i.e without affecting actual database we can create migration files (sql files) which can be used later.
    2. Run the command and redirect the output to any sql file
       alembic upgrade +1 --sql > <your_sql_file>
5. Online migration
    1. When we need to run migration online. Run command alembic upgrade head --> this will upgrade database to the latest version or
    2. Run command alembic upgrade <version_no> to upgrade to a specific higher version.
6. Downgrading
    Run command alembic downgrade base to revert all updates.
    Run command alembic downgrade -1 to downgrade one version lower.
    Run command alembic downgrade <version_no> to downgrade to a specific version.

# Notes
1. alembic_poc/migration/alembic/eny.py script needs to be modified to accept your own datbase connection and metadata of your models.
