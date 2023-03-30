import psycopg2
import json
from logger.logger import logger_init

logger = logger_init("DEBUG")

with open("db.json") as read_json:
    properties = json.load(read_json)["db"]

# Try to connect

try:
    conn = psycopg2.connect(properties)
    logger.info("Successfully connected to DB!")
except Exception as e:
    logger.error(f"I am unable to connect to the database: {e}")

cur = conn.cursor()
try:
    cur.execute("""-- Table: public.food

-- DROP TABLE IF EXISTS public.food;

CREATE TABLE IF NOT EXISTS public.food
(
    id integer NOT NULL,
    food json,
    CONSTRAINT food_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.food
    OWNER to postgres;""")
    logger.info("Food table successfully created!")
except Exception as e:
    logger.error(f"Food creating failed: {e}")

try:
    cur.execute("""-- Table: public.auth

-- DROP TABLE IF EXISTS public.auth;

CREATE TABLE IF NOT EXISTS public.auth
(
    username character(20) COLLATE pg_catalog."default" NOT NULL,
    password character(20) COLLATE pg_catalog."default" NOT NULL,
    key character(30) COLLATE pg_catalog."default" NOT NULL,
    id integer NOT NULL,
    CONSTRAINT auth_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth
    OWNER to postgres;""")
    logger.info("Auth table successfully created!")
except Exception as e:
    logger.error(f"Auth Table creating failed: {e}")

try:
    cur.execute("""-- Table: public.trains

-- DROP TABLE IF EXISTS public.trains;

CREATE TABLE IF NOT EXISTS public.trains
(
    id integer NOT NULL,
    trains json,
    CONSTRAINT trains_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.trains
    OWNER to postgres;""")
    logger.info("Trains table successfully created!")
except Exception as e:
    logger.error(f"Trains Table creating failed: {e}")

try:
    conn.commit()
    logger.info("Changes was successfully committed")
except Exception as e:
    logger.error(f"Changes committing failed: {e}")
