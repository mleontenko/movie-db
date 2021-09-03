-- Table: public.actors

-- DROP TABLE public.actors;

CREATE TABLE public.actors
(
    id integer NOT NULL DEFAULT nextval('actors_id_seq'::regclass),
    movie_id integer NOT NULL,
    name character varying(1024) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT actors_pkey PRIMARY KEY (id),
    CONSTRAINT fk_movie FOREIGN KEY (movie_id)
        REFERENCES public.movies (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.actors
    OWNER to root;