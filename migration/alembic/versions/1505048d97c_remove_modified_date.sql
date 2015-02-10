CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL
);

-- Running upgrade  -> 5b665583002

CREATE TABLE skills (
    skill_id INTEGER NOT NULL AUTO_INCREMENT, 
    skill_name VARCHAR(200) NOT NULL, 
    skill_description TEXT NOT NULL, 
    is_deleted BOOL NOT NULL, 
    created_by VARCHAR(200) NOT NULL, 
    created_date DATETIME NOT NULL, 
    modified_by VARCHAR(200), 
    modified_date DATETIME, 
    PRIMARY KEY (skill_id), 
    CHECK (is_deleted IN (0, 1))
);

INSERT INTO alembic_version (version_num) VALUES ('5b665583002');

