CREATE USER app WITH PASSWORD 'uiGh2lah';
CREATE DATABASE app_db;

\c app_db

CREATE TABLE IF NOT EXISTS results (
    id serial PRIMARY KEY,
    address VARCHAR(300) UNIQUE,
    words_count INT NOT NULL,
    http_status_code INT
);

CREATE TYPE task_status AS ENUM ('NOT_STARTED', 'PENDING', 'FINISHED');

CREATE TABLE IF NOT EXISTS tasks (
    id serial PRIMARY KEY,
    address VARCHAR(300) UNIQUE,
    timestamp TIMESTAMP,
    task_status task_status,
    http_status_code INT
);

GRANT ALL PRIVILEGES ON DATABASE app_db TO app;
GRANT ALL PRIVILEGES ON TABLE results TO app;
GRANT ALL PRIVILEGES ON TABLE tasks TO app;
GRANT ALL ON sequence tasks_id_seq to app;
GRANT ALL ON sequence results_id_seq to app;
