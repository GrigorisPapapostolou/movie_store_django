CREATE SEQUENCE IF NOT EXISTS public.movies_app_category_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.movies_app_category_id_seq OWNER TO postgres;

CREATE SEQUENCE IF NOT EXISTS public.movies_app_movie_genre_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.movies_app_movie_genre_id_seq OWNER TO postgres;

CREATE SEQUENCE IF NOT EXISTS public.movies_app_movie_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.movies_app_movie_id_seq OWNER TO postgres;

CREATE SEQUENCE IF NOT EXISTS public.movies_app_rental_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.movies_app_rental_id_seq OWNER TO postgres;

CREATE SEQUENCE IF NOT EXISTS public.auth_user_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;
ALTER SEQUENCE public.auth_user_id_seq OWNER TO postgres;


CREATE TABLE IF NOT EXISTS public.movies_app_category
(
    id bigint NOT NULL DEFAULT nextval('movies_app_category_id_seq'::regclass),
    title character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT movies_app_category_pkey PRIMARY KEY (id),
    CONSTRAINT movies_app_category_title_key UNIQUE (title)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.movies_app_category OWNER to postgres;

CREATE INDEX IF NOT EXISTS movies_app_category_title
    ON public.movies_app_category 
    USING btree (title COLLATE pg_catalog."default" varchar_pattern_ops ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public.movies_app_movie
(
    id bigint NOT NULL DEFAULT nextval('movies_app_movie_id_seq'::regclass),
    title character varying(50) COLLATE pg_catalog."default" NOT NULL,
    storyline character varying(200) COLLATE pg_catalog."default" NOT NULL,
    created date NOT NULL,
    rating double precision NOT NULL,
    director character varying(50) COLLATE pg_catalog."default",
    available boolean NOT NULL,
    CONSTRAINT movies_app_movie_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.movies_app_movie OWNER to postgres;


CREATE TABLE IF NOT EXISTS public.movies_app_movie_genre
(
    id bigint NOT NULL DEFAULT nextval('movies_app_movie_genre_id_seq'::regclass),
    movie_id bigint NOT NULL,
    category_id bigint NOT NULL,
    CONSTRAINT movies_app_movie_genre_pkey PRIMARY KEY (id),
    CONSTRAINT movies_app_movie_genre_movie_id_category_id_uniq UNIQUE (movie_id, category_id),
    CONSTRAINT movies_app_movie_gen_category_id_fk_movies_ap FOREIGN KEY (category_id)
        REFERENCES public.movies_app_category (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT movies_app_movie_genre_movie_id_9a6476ad_fk_movies_app_movie_id FOREIGN KEY (movie_id)
        REFERENCES public.movies_app_movie (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.movies_app_movie_genre
    OWNER to postgres;

CREATE INDEX IF NOT EXISTS movies_app_movie_genre_category_id
    ON public.movies_app_movie_genre USING btree
    (category_id ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX IF NOT EXISTS movies_app_movie_genre_movie_id
    ON public.movies_app_movie_genre USING btree
    (movie_id ASC NULLS LAST)
    TABLESPACE pg_default;

