CREATE TABLE if not exists HighCarb (
	Calories int not null,
    Nutrition varchar(255),
    Breakfast varchar(255),
    Lunch varchar(255),
    Dinner varchar(255),
    primary key (Calories)
);

/* Query:
SELECT * FROM eatandfit.HighCarb WHERE Calories = ?;
*/

INSERT INTO HighCarb VALUES (1500, '1500;186;52.7;81', '452:62x2.5;02x1', '470:25x1;63x1', '578:64x3;65x0.5'),
							(1700, '1700;199;38.8;153.7', '492:66x1;43x1', '474:59x1;67x2', '734:23x1;14x5.5'),
                            (1900, '1900;216.4;72;100.4', '636:47x1;51x2', '530:68x2;15x1', '734:56x1;14x3'),
                            (2300, '2300;279.2;68.8;161.1', '740:84x2;13x2', '635:85x1;86x2', '925:87x3;32x1'),
                            (2500, '2500;312.7;70.9;173.8', '807:88x0.5;89x3', '795:90x1;91x4', '898:61x1.5;32x1'),
                            (2700, '2700;326;61.1;240.9', '720:92x2;13x2', '920:93x1;94x3', '1060:75x3;37x3');