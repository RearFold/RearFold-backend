-- CREATE TABLE authority {
--     level varchar(80),
--     description text,
-- }

CREATE TABLE backend.admin (
    admin_id VARCHAR(80) PRIMARY KEY,
    admin_pw VARCHAR(200) NOT NULL, 
    created_at timestamp Default now(),
    description text
    -- authority reference authority.level
);

INSERT INTO admin(admin_id, admin_pw) values ('root', '1234');
INSERT INTO backend.admin(admin_id, admin_pw, description) values ('backend', '1234', 'test용용');