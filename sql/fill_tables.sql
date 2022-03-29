INSERT INTO public.movies_app_category(title) 
VALUES ('Fantasy'),('Comedy'),('Adventure');


INSERT INTO public.movies_app_movie(title, storyline, created, rating, director, available)
VALUES 
('Spider-Man: No Way Home', 'With Spider-Man s identity now revealed, Peter asks Doctor Strange for help.', '2021-12-31', 8.5, 'Jon Watts', true),
('Doctor Strange', 'While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.', '2016-10-13', 7.5, 'Scott Derrickso', true),
('The Matrix Resurrections', 'Return to a world of two realities: one, everyday life; the other, what lies behind it.', '2021-12-16', 5.7, 'Lana Wachowski', true),
('Star Wars: Episode IX - The Rise of Skywalker', 'In the riveting conclusion of the landmark Skywalker saga, new legends will be born-and the final battle for freedom is yet to come.', '2019-12-16', 6.5, 'J.J. Abrams', true),
('Monty Python and the Holy Grail', 'King Arthur and his Knights of the Round Table embark on a surreal, low-budget search for the Holy Grail, encountering many, very silly obstacles.', '1975-03-14', 8.2, 'Terry Gilliam', true),
('The Big Lebowski', 'This is a very complicated case, Maude. You know, a lot of ins, a lot of outs, a lot of what-have-yous.', '1998-01-18', 8.1, 'Coen Brothers', true),
('MacGruber', 'Former special operative MacGruber is called back into action to take down his arch-enemy, Dieter Von Cunth, who in possession of a nuclear warhead and bent on destroying Washington.', '2010-05-21', 5.6, 'Jorma Taccone', true),
('Thor: Ragnarok', 'Imprisoned on the planet Sakaar, Thor must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.', '2017-10-10', 7.9, 'Taika Waititi', true),
('Indiana Jones and the Raiders of the Lost Ark', 'In 1936, archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before Adolf Hitler s Nazis can obtain its awesome powers.', '1981-06-12', 8.4, 'Steven Spielberg', true),
('The Hobbit: An Unexpected Journey', 'A reluctant Hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home, and the gold within it from the dragon Smaug.', '2012-11-28', 7.8, 'Peter Jackson', true);


INSERT INTO public.movies_app_movie_genre(category_id, movie_id)
VALUES (1 , 1), (1 , 2) , (1 , 3), (1 , 4) , (2 , 5), (2 , 6) , (2 , 7), (3 , 8), (3 , 9) , (3 , 10);