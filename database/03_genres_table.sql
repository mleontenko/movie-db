-- SEQUENCE: public.genres_id_seq

-- DROP SEQUENCE public.genres_id_seq;

CREATE SEQUENCE public.genres_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.genres_id_seq
    OWNER TO root;


-- Table: public.genres

-- DROP TABLE public.genres;

CREATE TABLE public.genres
(
    id integer NOT NULL DEFAULT nextval('genres_id_seq'::regclass),
    movie_id integer NOT NULL,
    name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT fk_genre_movie FOREIGN KEY (movie_id)
        REFERENCES public.movies (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.genres
    OWNER to root;