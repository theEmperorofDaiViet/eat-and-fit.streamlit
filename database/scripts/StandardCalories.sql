CREATE TABLE if not exists StandardCalories (
	Stage int not null,
    Body int not null,
    Sex int not null,
    LowCarb int,
    ModerateCarb int,
    HighCarb int,
    primary key (Stage, Body, Sex)
);

 /*
 Stage: 0, 1
 Body: thiếu cân: 0
       bình thường: 1
       thừa cân: 2
       tiền béo phì: 3
       béo phì: 4
Sex: nam: 0,
     nữ: 1
 */
 
 /* Query:
 SELECT * FROM eatandfit.StandardCalories WHERE Stage = ? and Body = ? and Sex = ?;
 */
 
INSERT INTO StandardCalories VALUES (0, 2, 0, 2200, 2400, 2700),
                                    (0, 3, 0, 2000, 2200, 2500),
                                    (0, 4, 0, 1800, 2000, 2300),
                                    (1, 2, 0, 2000, 2200, 2700),
                                    (1, 3, 0, 1800, 2000, 2500),
                                    (1, 4, 0, 1600, 1800, 2300),
                                    (0, 2, 1, 1400, 1600, 1900),
                                    (0, 3, 1, 1200, 1400, 1700),
                                    (0, 4, 1, 1000, 1200, 1500),
                                    (1, 2, 1, 1200, 1400, 1900),
                                    (1, 3, 1, 1000, 1200, 1700),
                                    (1, 4, 1, 800, 1000, 1500);