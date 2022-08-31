-- portfolio project -- Chris Bowen
-- SQL Script QUERY TESTER

"""

THIS WILL EDIT THE ACTUAL CTUNES DATABASE 

BACK UP THE DB BEFORE USING THIS TOOL

    BACKUP
        command 
            docker exec pg_container pg_dump --verbose --file c_tunes_dump.sql c_tunes

        Find the latest back up
            docker exec pg_container ls
        
        Inspect the data dump 
            docker cp pg_container:moma_dump.sql data

        restore to original database
            docker exec pg_container psql c_tunes -f c_tunes_dump.sql

"""

-- use the following in the termainal to run this script
-- cat x.sql | docker exec -i pg_container psql

-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'c_tunes' AND pid <> pg_backend_pid();

-- connect via psql
\c c_tunes

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


-- Test queries below here ---

-- reset tables (erase data)
--TRUNCATE TABLE users_songs CASCADE;
--TRUNCATE TABLE songs CASCADE;
--TRUNCATE TABLE albums CASCADE;
--TRUNCATE TABLE artists CASCADE;
--TRUNCATE TABLE users CASCADE;

