CREATE SEQUENCE auth_id_seq;

-- Table: public.food

-- DROP TABLE IF EXISTS public.food;

CREATE TABLE IF NOT EXISTS public.food
(
    id integer NOT NULL,
    food json DEFAULT '{}'::json,
    CONSTRAINT food_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.food
    OWNER to postgres;

-- Table: public.auth

-- DROP TABLE IF EXISTS public.auth;

CREATE TABLE IF NOT EXISTS public.auth
(
    username character(20) COLLATE pg_catalog."default" NOT NULL,
    password character(20) COLLATE pg_catalog."default" NOT NULL,
    id integer NOT NULL DEFAULT nextval('auth_id_seq'::regclass),
    CONSTRAINT auth_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auth
    OWNER to postgres;


-- Table: public.trains

-- DROP TABLE IF EXISTS public.trains;

CREATE TABLE IF NOT EXISTS public.trains
(
    id integer NOT NULL,
    trains json DEFAULT '{}'::json,
    CONSTRAINT trains_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.trains
    OWNER to postgres;