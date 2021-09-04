-- SEQUENCE: public.movies_id_seq

-- DROP SEQUENCE public.movies_id_seq;

CREATE SEQUENCE public.movies_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.movies_id_seq
    OWNER TO root;


-- Table: public.movies

-- DROP TABLE public.movies;

CREATE TABLE public.movies
(
    id integer NOT NULL DEFAULT nextval('movies_id_seq'::regclass),
    moviedb_id integer NOT NULL,
    original_title character varying(1024) COLLATE pg_catalog."default",
    release_date date,
    director character varying(1024) COLLATE pg_catalog."default",
    CONSTRAINT movies_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.movies
    OWNER to root;