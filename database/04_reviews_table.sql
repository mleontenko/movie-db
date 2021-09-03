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