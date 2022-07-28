create database train_db
use train_db

create table trainDetails(
	train_id INT Primary Key,
	train_name VARCHAR(20)
	);

CREATE TABLE stationDetails(
	station_id INT PRIMARY KEY,
	station_name VARCHAR(20)
	);

CREATE TABLE passengerDetails(
	pass_id INT IDENTITY PRIMARY KEY,
	pass_name VARCHAR(20),
	trainID INT,
	startStation INT,
	endStation INT,
	waiting_list INT,
	CONSTRAINT fk_trainID
		FOREIGN KEY(trainID)
		REFERENCES trainDetails(train_id),
	CONSTRAINT fk_startstation
		FOREIGN KEY(startStation)
		REFERENCES stationDetails(station_id),
	CONSTRAINT fk_endstation
		FOREIGN KEY(endStation)
		REFERENCES stationDetails(station_id)
	);

insert into trainDetails values
(1,'TVM_ALP'),
(2,'TVM_EKM'),
(3,'TVM_KZK');

insert into stationDetails values
(1,'TVM'),
(2,'ALP'),
(3,'EKM'),
(4,'KZK');

insert into passengerDetails(pass_name,trainID,startStation,endStation,waiting_list) values
('John',1,1,2,0),
('Ram',1,1,2,0),
('Bond',2,1,3,0),
('Gates',3,1,4,0);

select count(pass_id) from passengerDetails
where trainID = 1;

select sum(waiting_list) from passengerDetails
where trainID = 1;