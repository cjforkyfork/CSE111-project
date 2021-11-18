-- .mode "csv"
-- .separator ","

-- .import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/animal.csv"' animal
-- .import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/animals_assistant.csv"' animals_assistant
-- .import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/shelter_assistant.csv"' shelter_assistant
-- .import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/shelter.csv"' shelter
-- .import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/status.csv"' status

INSERT INTO visits VALUES(1,1,2,3,'has started being aggresive');
INSERT INTO visits VALUES(2,2,2,9,'has started isolating');
INSERT INTO visits VALUES(3,5,4,20,'sudden violent spasms');
INSERT INTO visits VALUES(4,10,2,6,'visit for adoption');
INSERT INTO visits VALUES(5,8,1,19,'improving behavior');

-- city_key INT PRIMARY KEY NOT NULL,
-- city_name char(25) not null
INSERT INTO city VALUES(1,'Merced');
INSERT INTO city VALUES(2,'Modesto');
INSERT INTO city VALUES(3,'Stanislaus');
INSERT INTO city VALUES(4,'Turlock');
INSERT INTO city VALUES(5,'Atwater');
INSERT INTO city VALUES(6,'Tracy');
INSERT INTO city VALUES(7,'Stockton');
INSERT INTO city VALUES(8,'Sacramento');
INSERT INTO city VALUES(9,'Ceres');
INSERT INTO city VALUES(10,'Salida');

-- customer_id  INT PRIMARY KEY NOT NULL,
--     city_key INT NOT NULL,
--     FOREIGN KEY(city_key) REFERENCES city(city_key)
INSERT INTO customer VALUES(1,'Kirby Mckenna',1);
INSERT INTO customer VALUES(2,'Sarah-Jayne Larsen',2);
INSERT INTO customer VALUES(3,'Izzy Head',3);
INSERT INTO customer VALUES(4,'Robert Davis',4);
INSERT INTO customer VALUES(5,'Ricky Dunigan',5);
INSERT INTO customer VALUES(6,'Robert Cooper',6);
INSERT INTO customer VALUES(7,'Darnell Carlton',7);
INSERT INTO customer VALUES(8,'Emma Heart',8);
INSERT INTO customer VALUES(9,'Alexa Ryan',9);
INSERT INTO customer VALUES(10,'Mitchell Sewis',10);
INSERT INTO customer VALUES(11,'Aniy Krup',10);
INSERT INTO customer VALUES(12,'Mozol Rej',9);
INSERT INTO customer VALUES(13,'James Lin',8);
INSERT INTO customer VALUES(14,'Alexander Pham',7);
INSERT INTO customer VALUES(15,'Ronald Sr',6);
INSERT INTO customer VALUES(16,'Shana Young',5);
INSERT INTO customer VALUES(17,'Michael Miranda',4);
INSERT INTO customer VALUES(18,'Lawman Reed',3);
INSERT INTO customer VALUES(19,'Cuthbert Mon',2);
INSERT INTO customer VALUES(20,'Ryan Beagle',1);


--     customer_id  INT PRIMARY KEY NOT NULL,
--     city_key INT NOT NULL,
--     FOREIGN KEY(city_key) REFERENCES city(city_key)

INSERT INTO customer_community VALUES(1,6);
INSERT INTO customer_community VALUES(2,1);
INSERT INTO customer_community VALUES(3,7);
INSERT INTO customer_community VALUES(4,3);
INSERT INTO customer_community VALUES(5,2);
INSERT INTO customer_community VALUES(6,8);
INSERT INTO customer_community VALUES(7,9);
INSERT INTO customer_community VALUES(8,10);
INSERT INTO customer_community VALUES(9,11);
INSERT INTO customer_community VALUES(10,4);
INSERT INTO customer_community VALUES(10,16);
INSERT INTO customer_community VALUES(9,20);
INSERT INTO customer_community VALUES(8,19);
INSERT INTO customer_community VALUES(7,18);
INSERT INTO customer_community VALUES(6,17);
INSERT INTO customer_community VALUES(5,5);
INSERT INTO customer_community VALUES(4,15);
INSERT INTO customer_community VALUES(3,14);
INSERT INTO customer_community VALUES(2,13);
INSERT INTO customer_community VALUES(1,12);

--     donation_key INT PRIMARY KEY NOT NULL,
--     customer_id  INT  NOT NULL,
--     shelter_key  INT NOT NULL,
--     money     decimal(9,2) NOT NULL,

INSERT INTO donations VALUES(1,1,6,3000);
INSERT INTO donations VALUES(2,2,1,500);
INSERT INTO donations VALUES(3,3,7,100);
INSERT INTO donations VALUES(4,4,3,3000);
INSERT INTO donations VALUES(5,5,2,3000);
INSERT INTO donations VALUES(6,1,12,3000);
INSERT INTO donations VALUES(7,2,13,3000);
INSERT INTO donations VALUES(8,3,14,3000);
INSERT INTO donations VALUES(9,4,15,3000);
INSERT INTO donations VALUES(10,5,5,3000);
INSERT INTO donations VALUES(11,3,14,7000);
INSERT INTO donations VALUES(12,5,5,7100);
INSERT INTO donations VALUES(13,6,12,200);
INSERT INTO donations VALUES(14,8,7,500);


INSERT INTO requests_visits VALUES(1,5,2);
INSERT INTO requests_visits VALUES(2,4,10);
INSERT INTO requests_visits VALUES(3,5,7);
INSERT INTO requests_visits VALUES(4,7,9);
INSERT INTO requests_visits VALUES(5,6,4);
INSERT INTO requests_visits VALUES(6,2,3);
INSERT INTO requests_visits VALUES(7,1,2);
INSERT INTO requests_visits VALUES(8,3,8);
INSERT INTO requests_visits VALUES(9,5,9);
INSERT INTO requests_visits VALUES(10,1,2);
INSERT INTO requests_visits VALUES(11,5,2);
INSERT INTO requests_visits VALUES(12,5,8);

-- TWO NEW INSERT STATEMENTS WHICH ARENT RUN YET

INSERT INTO donations VALUES(13,10,16,500);
INSERT INTO requests_visits VALUES(8,5);




