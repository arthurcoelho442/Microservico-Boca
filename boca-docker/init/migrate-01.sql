\connect bocadb;

CREATE TABLE public.tagtable
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    name text NOT NULL,
    value text NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.tagtable
    OWNER to postgres;