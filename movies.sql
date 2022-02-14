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
    id integer NOT NULL,
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
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO hackbright;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: characters; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.characters (
    id integer NOT NULL,
    char_name character varying,
    movie_id integer,
    actor_id integer
);


ALTER TABLE public.characters OWNER TO hackbright;

--
-- Name: characters_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.characters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.characters_id_seq OWNER TO hackbright;

--
-- Name: characters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.characters_id_seq OWNED BY public.characters.id;


--
-- Name: movies; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    movie_title character varying,
    genre character varying,
    poster character varying,
    watch_link character varying,
    overview text,
    release_date timestamp without time zone,
    tmdb_id character varying
);


ALTER TABLE public.movies OWNER TO hackbright;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO hackbright;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: ratings; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.ratings (
    id integer NOT NULL,
    score integer,
    movie_id integer,
    user_id integer
);


ALTER TABLE public.ratings OWNER TO hackbright;

--
-- Name: ratings_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.ratings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ratings_id_seq OWNER TO hackbright;

--
-- Name: ratings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.ratings_id_seq OWNED BY public.ratings.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying,
    password character varying
);


ALTER TABLE public.users OWNER TO hackbright;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO hackbright;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: characters id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters ALTER COLUMN id SET DEFAULT nextval('public.characters_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Name: ratings id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings ALTER COLUMN id SET DEFAULT nextval('public.ratings_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.actors (id, actor_name, gender, dob, other_name, ethnicity, biography, headshot) FROM stdin;
1	Kelly Marie Tran	{gender}	1989-01-17 00:00:00	{"Kelly Tran","Trần Loan ","켈리 마리 트란","트란 로안","Tran Loan"}	\N	Kelly Marie Tran is a Vietnamese-American film actress known for her performances as Rose Tico in Star Wars: The Last Jedi and Star Wars: The Rise of Skywalker. She has also appeared as a part of CollegeHumor Originals, as Margeurite in About a Boy, and as Sara from Life on Normal Street.	https://image.tmdb.org/t/p/w45/2YuymbQfIlaUx8xtAxL5OOCsw6H.jpg
2	Ann Truong	{gender}	\N	{}	\N		https://image.tmdb.org/t/p/w45/fBFHyU1YIPYgPMYbPDbNgAuzj3y.jpg
\.


--
-- Data for Name: characters; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.characters (id, char_name, movie_id, actor_id) FROM stdin;
1	Raya (voice)	1	1
2	Dawn Betterman (voice)	2	1
3	Jamie	3	1
4	Rose Tico (voice)	4	1
5	Dawn Betterman (voice)	5	1
6	Kelly	6	1
7	Herself	7	1
8	Rose Tico	8	1
9	Rose Tico	9	1
10	Self	10	1
11	Butterfly Girl	11	1
12	Kim Tran	12	2
13	Jodie	13	2
14	Tha	14	2
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.movies (id, movie_title, genre, poster, watch_link, overview, release_date, tmdb_id) FROM stdin;
1	Raya and the Last Dragon	\N	https://image.tmdb.org/t/p/w500/lPsD10PP4rgUGiGR4CCXA6iY0QQ.jpg	\N	Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when an evil force threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, that same evil has returned and it’s up to a lone warrior, Raya, to track down the legendary last dragon to restore the fractured land and its divided people.	\N	527774
2	Dear Diary: World's First Pranks	\N	https://image.tmdb.org/t/p/w500/rSwe3nDvPPjZBjtDTWgzK1t9CP8.jpg	\N	Eep reveals how a comical accident led her and Dawn to discover the joys of tricking their families and set about performing "the world's first pranks."	\N	801876
3	Untouchable	\N	https://image.tmdb.org/t/p/w500/u14JtB4CmXAFwnnwB8PEpj1ESsu.jpg	\N	A masseuse's journey to find the human touch.	\N	468301
4	The Lego Star Wars Holiday Special	\N	https://image.tmdb.org/t/p/w500/zyzJSI7UZZzz5Toj10rYGF5689z.jpg	\N	As her friends prep for a Life Day holiday celebration, Rey journeys with BB-8 on a quest to gain a deeper knowledge of the Force at a mysterious Jedi Temple. There, she embarks on a cross-timeline adventure through beloved moments in Star Wars history, coming into contact with iconic heroes and villains from all eras of the saga. But will she make it back in time for the Life Day feast?	\N	732670
5	The Croods: A New Age	\N	https://image.tmdb.org/t/p/w500/tbVZ3Sq88dZaCANlUcewQuHQOaE.jpg	\N	Searching for a safer habitat, the prehistoric Crood family discovers an idyllic, walled-in paradise that meets all of its needs. Unfortunately, they must also learn to live with the Bettermans -- a family that's a couple of steps above the Croods on the evolutionary ladder. As tensions between the new neighbors start to rise, a new threat soon propels both clans on an epic adventure that forces them to embrace their differences, draw strength from one another, and survive together.	\N	529203
6	Andy's CDs	\N	https://image.tmdb.org/t/p/w500/2jF8YCnHxDLcfpwA4S84hilLRAE.jpg	\N	When Andy is dumped by his girlfriend he must break into his ex's apartment with his ultra nerd best friend, Tyke, in order to reclaim his CD collection.	\N	468898
7	The Director and the Jedi	\N	https://image.tmdb.org/t/p/w500/kc19s3pN3gxEcOSM6H20rFlRODo.jpg	\N	An intimate documentary delving into Rian Johnson's process as he comes in as a director new to the Star Wars universe.	\N	510714
8	Star Wars: The Last Jedi	\N	https://image.tmdb.org/t/p/w500/kOVEVeg59E0wsnXmF9nrh6OmWII.jpg	\N	Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares to do battle with the First Order.	\N	181808
9	Star Wars: The Rise of Skywalker	\N	https://image.tmdb.org/t/p/w500/db32LaOibwEliAmSL2jjDF6oDdj.jpg	\N	The surviving Resistance faces the First Order once again as the journey of Rey, Finn and Poe Dameron continues. With the power and knowledge of generations behind them, the final battle begins.	\N	181812
10	The Skywalker Legacy	\N	https://image.tmdb.org/t/p/w500/lIZzwi4qK3wa5avz3YK0YNDq0ig.jpg	\N	The story lives forever in this feature-length documentary that charts the making of Star Wars: The Rise of Skywalker.	\N	680382
11	XOXO	\N	https://image.tmdb.org/t/p/w500/lSWO4dZTqOEGSHffJl4GH3G8Fvp.jpg	\N	XOXO follows six strangers whose lives collide in one frenetic, dream-chasing, hopelessly romantic night.	\N	352492
12	Never Forget	\N	https://image.tmdb.org/t/p/w500/iigtvhWi9z8HAdVHqaNG6O4IZ7u.jpg	\N	A young Australian nurse Kim is about to start her new life with her boyfriend. In the middle of proposing to her, she gets the biggest news of her life; her father who she hasn't seen since she left Vietnam has died. In order to make things right, she must travel back and say her 'goodbyes'. Her family send an escort to bring her back to the village and she is not happy at all with this arrangement.	\N	472857
13	The Reef: Stalked	\N	https://image.tmdb.org/t/p/w500/kNy3hQKWV3UazFStIAHQuGWHBjM.jpg	\N	In an effort to heal after witnessing her sister’s horrific murder, Nic travels to a tropical resort with her friends for a kayaking and diving adventure. Only hours into their expedition, the women are stalked and then attacked by a great white shark. To survive they will need to band together and Nic will have to overcome her post-traumatic stress, face her fears and slay the monster.	\N	730167
14	Hard Target 2	\N	https://image.tmdb.org/t/p/w500/jO8C2AIIdFyi5ceI6whev0RYt0k.jpg	\N	Forced into a deadly cat-and-mouse game, a disgraced mixed martial arts fighter is hunted through the jungles of Southeast Asia.	\N	402331
\.


--
-- Data for Name: ratings; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.ratings (id, score, movie_id, user_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.users (id, email, password) FROM stdin;
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.actors_id_seq', 2, true);


--
-- Name: characters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.characters_id_seq', 14, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.movies_id_seq', 14, true);


--
-- Name: ratings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.ratings_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: characters characters_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_pkey PRIMARY KEY (id);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: ratings ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: characters characters_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(id);


--
-- Name: characters characters_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- Name: ratings ratings_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- Name: ratings ratings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

