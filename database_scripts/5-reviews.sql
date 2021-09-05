-- SEQUENCE: public.reviews_id_seq

-- DROP SEQUENCE public.reviews_id_seq;

CREATE SEQUENCE public.reviews_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.reviews_id_seq
    OWNER TO root;


-- Table: public.reviews

-- DROP TABLE public.reviews;

CREATE TABLE public.reviews
(
    id integer NOT NULL DEFAULT nextval('reviews_id_seq'::regclass),
    movie_id integer NOT NULL,
    review character varying(16384) COLLATE pg_catalog."default" NOT NULL,
    compound real NOT NULL,
    CONSTRAINT reviews_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.reviews
    OWNER to root;