--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4 (Ubuntu 13.4-4.pgdg20.04+1)
-- Dumped by pg_dump version 13.4 (Ubuntu 13.4-4.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.actors (
    actor_id integer NOT NULL,
    actor_name character varying,
    gender character varying,
    dob timestamp without time zone,
    other_name character varying,
    ethnicity character varying,
    biography text,
    headshot character varying
);


ALTER TABLE public.actors OWNER TO hackbright;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.actors_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_actor_id_seq OWNER TO hackbright;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.actors_actor_id_seq OWNED BY public.actors.actor_id;


--
-- Name: characters; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.characters (
    char_id integer NOT NULL,
    char_name character varying,
    movie_id integer,
    actor_id integer
);


ALTER TABLE public.characters OWNER TO hackbright;

--
-- Name: characters_char_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.characters_char_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.characters_char_id_seq OWNER TO hackbright;

--
-- Name: characters_char_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.characters_char_id_seq OWNED BY public.characters.char_id;


--
-- Name: movies; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.movies (
    movie_id integer NOT NULL,
    movie_title character varying,
    genre character varying,
    poster character varying,
    watch_link character varying,
    overview text,
    release_date timestamp without time zone
);


ALTER TABLE public.movies OWNER TO hackbright;

--
-- Name: movies_movie_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.movies_movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_movie_id_seq OWNER TO hackbright;

--
-- Name: movies_movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.movies_movie_id_seq OWNED BY public.movies.movie_id;


--
-- Name: ratings; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.ratings (
    rating_id integer NOT NULL,
    score integer,
    movie_id integer,
    user_id integer
);


ALTER TABLE public.ratings OWNER TO hackbright;

--
-- Name: ratings_rating_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.ratings_rating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ratings_rating_id_seq OWNER TO hackbright;

--
-- Name: ratings_rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.ratings_rating_id_seq OWNED BY public.ratings.rating_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying,
    password character varying
);


ALTER TABLE public.users OWNER TO hackbright;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO hackbright;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: actors actor_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.actors ALTER COLUMN actor_id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);


--
-- Name: characters char_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters ALTER COLUMN char_id SET DEFAULT nextval('public.characters_char_id_seq'::regclass);


--
-- Name: movies movie_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.movies ALTER COLUMN movie_id SET DEFAULT nextval('public.movies_movie_id_seq'::regclass);


--
-- Name: ratings rating_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings ALTER COLUMN rating_id SET DEFAULT nextval('public.ratings_rating_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.actors (actor_id, actor_name, gender, dob, other_name, ethnicity, biography, headshot) FROM stdin;
1	Kelly Marie Tran	{gender}	1989-01-17 00:00:00	{"Kelly Tran","Trần Loan ","켈리 마리 트란","트란 로안","Tran Loan"}	\N	Kelly Marie Tran is a Vietnamese-American film actress known for her performances as Rose Tico in Star Wars: The Last Jedi and Star Wars: The Rise of Skywalker. She has also appeared as a part of CollegeHumor Originals, as Margeurite in About a Boy, and as Sara from Life on Normal Street.	https://image.tmdb.org/t/p/w45/2YuymbQfIlaUx8xtAxL5OOCsw6H.jpg
2	Thalia Tran	{gender}	2007-01-01 00:00:00	{}	\N	Thalia Tran is an actress, known for Little (2019) and Raya and the Last Dragon (2021).	https://image.tmdb.org/t/p/w45/9JTbJ7wVKkVks4XRfyNCem1jFSO.jpg
3	Kelly Marie Tran	{gender}	1989-01-17 00:00:00	{"Kelly Tran","Trần Loan ","켈리 마리 트란","트란 로안","Tran Loan"}	\N	Kelly Marie Tran is a Vietnamese-American film actress known for her performances as Rose Tico in Star Wars: The Last Jedi and Star Wars: The Rise of Skywalker. She has also appeared as a part of CollegeHumor Originals, as Margeurite in About a Boy, and as Sara from Life on Normal Street.	https://image.tmdb.org/t/p/w45/2YuymbQfIlaUx8xtAxL5OOCsw6H.jpg
4	Thalia Tran	{gender}	2007-01-01 00:00:00	{}	\N	Thalia Tran is an actress, known for Little (2019) and Raya and the Last Dragon (2021).	https://image.tmdb.org/t/p/w45/9JTbJ7wVKkVks4XRfyNCem1jFSO.jpg
\.


--
-- Data for Name: characters; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.characters (char_id, char_name, movie_id, actor_id) FROM stdin;
1	Raya (voice)	\N	\N
2	Dawn Betterman (voice)	\N	\N
3	Jamie	\N	\N
4	Rose Tico (voice)	\N	\N
5	Dawn Betterman (voice)	\N	\N
6	Kelly	\N	\N
7	Herself	\N	\N
8	Rose Tico	\N	\N
9	Rose Tico	\N	\N
10	Self	\N	\N
11	Butterfly Girl	\N	\N
12	Raina	\N	\N
13	Little Noi (voice)	\N	\N
14	Raya (voice)	\N	\N
15	Dawn Betterman (voice)	\N	\N
16	Jamie	\N	\N
17	Rose Tico (voice)	\N	\N
18	Dawn Betterman (voice)	\N	\N
19	Kelly	\N	\N
20	Herself	\N	\N
21	Rose Tico	\N	\N
22	Rose Tico	\N	\N
23	Self	\N	\N
24	Butterfly Girl	\N	\N
25	Raina	\N	\N
26	Little Noi (voice)	\N	\N
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.movies (movie_id, movie_title, genre, poster, watch_link, overview, release_date) FROM stdin;
1	Raya and the Last Dragon	\N	/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg	\N	Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when an evil force threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, that same evil has returned and it’s up to a lone warrior, Raya, to track down the legendary last dragon to restore the fractured land and its divided people.	\N
2	Dear Diary: World's First Pranks	\N	/rSwe3nDvPPjZBjtDTWgzK1t9CP8.jpg	\N	Eep reveals how a comical accident led her and Dawn to discover the joys of tricking their families and set about performing "the world's first pranks."	\N
3	Untouchable	\N	/u14JtB4CmXAFwnnwB8PEpj1ESsu.jpg	\N	A masseuse's journey to find the human touch.	\N
4	The Lego Star Wars Holiday Special	\N	/zyzJSI7UZZzz5Toj10rYGF5689z.jpg	\N	As her friends prep for a Life Day holiday celebration, Rey journeys with BB-8 on a quest to gain a deeper knowledge of the Force at a mysterious Jedi Temple. There, she embarks on a cross-timeline adventure through beloved moments in Star Wars history, coming into contact with iconic heroes and villains from all eras of the saga. But will she make it back in time for the Life Day feast?	\N
5	The Croods: A New Age	\N	/tbVZ3Sq88dZaCANlUcewQuHQOaE.jpg	\N	Searching for a safer habitat, the prehistoric Crood family discovers an idyllic, walled-in paradise that meets all of its needs. Unfortunately, they must also learn to live with the Bettermans -- a family that's a couple of steps above the Croods on the evolutionary ladder. As tensions between the new neighbors start to rise, a new threat soon propels both clans on an epic adventure that forces them to embrace their differences, draw strength from one another, and survive together.	\N
6	Andy's CDs	\N	/2jF8YCnHxDLcfpwA4S84hilLRAE.jpg	\N	When Andy is dumped by his girlfriend he must break into his ex's apartment with his ultra nerd best friend, Tyke, in order to reclaim his CD collection.	\N
7	The Director and the Jedi	\N	/kc19s3pN3gxEcOSM6H20rFlRODo.jpg	\N	An intimate documentary delving into Rian Johnson's process as he comes in as a director new to the Star Wars universe.	\N
8	Star Wars: The Last Jedi	\N	/kOVEVeg59E0wsnXmF9nrh6OmWII.jpg	\N	Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares to do battle with the First Order.	\N
9	Star Wars: The Rise of Skywalker	\N	/db32LaOibwEliAmSL2jjDF6oDdj.jpg	\N	The surviving Resistance faces the First Order once again as the journey of Rey, Finn and Poe Dameron continues. With the power and knowledge of generations behind them, the final battle begins.	\N
10	The Skywalker Legacy	\N	/lIZzwi4qK3wa5avz3YK0YNDq0ig.jpg	\N	The story lives forever in this feature-length documentary that charts the making of Star Wars: The Rise of Skywalker.	\N
11	XOXO	\N	/lSWO4dZTqOEGSHffJl4GH3G8Fvp.jpg	\N	XOXO follows six strangers whose lives collide in one frenetic, dream-chasing, hopelessly romantic night.	\N
12	Little	\N	/4MDB6jJl3U7xK1Gw64zIqt9pQA4.jpg	\N	Jordan Sanders, a take-no-prisoners tech mogul, wakes up one morning in the body of her 13-year-old self right before a do-or-die presentation. Her beleaguered assistant April is the only one in on the secret that her daily tormentor is now trapped in an awkward tween body, just as everything is on the line.	\N
13	Raya and the Last Dragon	\N	/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg	\N	Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when an evil force threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, that same evil has returned and it’s up to a lone warrior, Raya, to track down the legendary last dragon to restore the fractured land and its divided people.	\N
14	Raya and the Last Dragon	\N	/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg	\N	Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when an evil force threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, that same evil has returned and it’s up to a lone warrior, Raya, to track down the legendary last dragon to restore the fractured land and its divided people.	\N
15	Dear Diary: World's First Pranks	\N	/rSwe3nDvPPjZBjtDTWgzK1t9CP8.jpg	\N	Eep reveals how a comical accident led her and Dawn to discover the joys of tricking their families and set about performing "the world's first pranks."	\N
16	Untouchable	\N	/u14JtB4CmXAFwnnwB8PEpj1ESsu.jpg	\N	A masseuse's journey to find the human touch.	\N
17	The Lego Star Wars Holiday Special	\N	/zyzJSI7UZZzz5Toj10rYGF5689z.jpg	\N	As her friends prep for a Life Day holiday celebration, Rey journeys with BB-8 on a quest to gain a deeper knowledge of the Force at a mysterious Jedi Temple. There, she embarks on a cross-timeline adventure through beloved moments in Star Wars history, coming into contact with iconic heroes and villains from all eras of the saga. But will she make it back in time for the Life Day feast?	\N
18	The Croods: A New Age	\N	/tbVZ3Sq88dZaCANlUcewQuHQOaE.jpg	\N	Searching for a safer habitat, the prehistoric Crood family discovers an idyllic, walled-in paradise that meets all of its needs. Unfortunately, they must also learn to live with the Bettermans -- a family that's a couple of steps above the Croods on the evolutionary ladder. As tensions between the new neighbors start to rise, a new threat soon propels both clans on an epic adventure that forces them to embrace their differences, draw strength from one another, and survive together.	\N
19	Andy's CDs	\N	/2jF8YCnHxDLcfpwA4S84hilLRAE.jpg	\N	When Andy is dumped by his girlfriend he must break into his ex's apartment with his ultra nerd best friend, Tyke, in order to reclaim his CD collection.	\N
20	The Director and the Jedi	\N	/kc19s3pN3gxEcOSM6H20rFlRODo.jpg	\N	An intimate documentary delving into Rian Johnson's process as he comes in as a director new to the Star Wars universe.	\N
21	Star Wars: The Last Jedi	\N	/kOVEVeg59E0wsnXmF9nrh6OmWII.jpg	\N	Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares to do battle with the First Order.	\N
22	Star Wars: The Rise of Skywalker	\N	/db32LaOibwEliAmSL2jjDF6oDdj.jpg	\N	The surviving Resistance faces the First Order once again as the journey of Rey, Finn and Poe Dameron continues. With the power and knowledge of generations behind them, the final battle begins.	\N
23	The Skywalker Legacy	\N	/lIZzwi4qK3wa5avz3YK0YNDq0ig.jpg	\N	The story lives forever in this feature-length documentary that charts the making of Star Wars: The Rise of Skywalker.	\N
24	XOXO	\N	/lSWO4dZTqOEGSHffJl4GH3G8Fvp.jpg	\N	XOXO follows six strangers whose lives collide in one frenetic, dream-chasing, hopelessly romantic night.	\N
25	Little	\N	/4MDB6jJl3U7xK1Gw64zIqt9pQA4.jpg	\N	Jordan Sanders, a take-no-prisoners tech mogul, wakes up one morning in the body of her 13-year-old self right before a do-or-die presentation. Her beleaguered assistant April is the only one in on the secret that her daily tormentor is now trapped in an awkward tween body, just as everything is on the line.	\N
26	Raya and the Last Dragon	\N	/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg	\N	Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when an evil force threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, that same evil has returned and it’s up to a lone warrior, Raya, to track down the legendary last dragon to restore the fractured land and its divided people.	\N
\.


--
-- Data for Name: ratings; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.ratings (rating_id, score, movie_id, user_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.users (user_id, email, password) FROM stdin;
\.


--
-- Name: actors_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.actors_actor_id_seq', 4, true);


--
-- Name: characters_char_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.characters_char_id_seq', 26, true);


--
-- Name: movies_movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.movies_movie_id_seq', 26, true);


--
-- Name: ratings_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.ratings_rating_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, false);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (actor_id);


--
-- Name: characters characters_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_pkey PRIMARY KEY (char_id);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (movie_id);


--
-- Name: ratings ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_pkey PRIMARY KEY (rating_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: characters characters_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(actor_id);


--
-- Name: characters characters_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(movie_id);


--
-- Name: ratings ratings_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(movie_id);


--
-- Name: ratings ratings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

