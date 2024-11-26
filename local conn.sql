CREATE TABLE usr(firstname varchar(50),lastname varchar(50),email varchar(100) UNIQUE,passsword varchar(50),conpassword varchar(50));
select * from usr

INSERT INTO usr VALUES('sai','aswath','sai@gmail.com','pass','pass');
SELECT * FROM usr where (email='chan@gmail.com' and passsword='123456');
select * from  Webvisitor_card

CREATE TABLE Security_Officer(sec_id varchar(10) PRIMARY KEY, SFName varchar(30),SLName varchar(30), SArea varchar(255), SPIN varchar(7),Gate_no varchar(10),email varchar(100),passsword varchar(100));

CREATE TABLE Security_Officer_ph(sec_id varchar(10),sec_phone_no varchar(10),CONSTRAINT security_ph PRIMARY KEY(sec_id,sec_phone_no));
ALTER TABLE Security_Officer ADD passsword varchar(100)

INSERT INTO Security_officer VALUES ('sec01','nandi','reddy','hyd','560025','G01');
SELECT * FROM Security_Officer
INSERT INTO Security_officer_ph VALUES ('sec01','9448825994');


SELECT * FROM Security_Officer where email='kiasec@gmail.com' and passsword='12345'

update staff set passsword='team11' where staff_id='s06'

CREATE TABLE contactus(email VARCHAR(100),name VARCHAR(50),country VARCHAR(50),phno VARCHAR(10));
SELECT * FROM staff

CREATE TABLE Staff(Staff_id varchar(20) PRIMARY KEY, FFIName varchar(30), LFIName varchar(30), Area varchar(255), PIN NUMBER(7));
ALTER TABLE staff ADD passsword varchar(100)
INSERT INTO staff VALUES('s01','rithivika','alapati','hyd',560016);
INSERT INTO staff VALUES('s02','kiara','advani','mum',560017);
INSERT INTO staff VALUES('s03','nandu','reddy','bng',560018);
INSERT INTO staff VALUES('s04','andana','sree','raj',560019);
INSERT INTO staff VALUES('s05','sai','aswath','bng',560020);
INSERT INTO staff VALUES('s06','team','25','bng',560020,'team25@gmail.com','team25');
SELECT * FROM staff_ph

CREATE TABLE Staff_ph(Staff_id  varchar(20) ,phoneno  varchar(10))
INSERT INTO staff_ph VALUES('s06','6361885054')
DELETE FROM staff;
DROP TABLE staff_;
SELECT * FROM staff
DELETE FROM Staff;
DROP TABLE Staff;


DELETE FROM Flight WHERE Flight_no='E7013'
DROP TABLE Flight;

    select * from flight

ALTER SESSION SET NLS_TIMESTAMP_FORMAT  = 'YYYY-MM-DD HH24:MI:SS'

ALTER SESSION SET NLS_TIMESTAMP_FORMAT  = 'YYYY-MM-DD HH24:MI:SS'

ALTER TABLE Flight ADD deleted VARCHAR(1);
UPDATE Flight SET deleted='n'

CREATE TABLE Flight(Flight_no varchar(30) PRIMARY KEY,Flight_name varchar(30),from_ varchar(20),to_ varchar(20),Arrival TIMESTAMP,Departure TIMESTAMP,Available_seats varchar(50),price varchar(100),Staff_id varchar(20) REFERENCES Staff(Staff_id));
INSERT INTO  Flight VALUES('E7037','INDIGO','Bangalore','Delhi','2022-01-10 10:00:00','2022-01-10 12:00:00',20,5000,'s01');
INSERT INTO  Flight VALUES('E7038','INDIGO','Bangalore','Hyderabad','2022-01-11 12:00:00','2022-01-11 3:00:00',15,7000,'s02');
INSERT INTO  Flight VALUES('B0731','AIRWAYS','Bangalore','Delhi','2022-12-11 8:00:00','2022-12-11 9:00:00',10,17000,'s03');
INSERT INTO  Flight VALUES('B0721','JETWAYS','Bangalore','Chennai','2022-12-13 12:00:00','2022-12-13 2:00:00',5,19000,'s04');
INSERT INTO  Flight VALUES('F0621','AIRWAYS','Bangalore','Goa','2022-12-14 4:00:00','2022-12-14 6:15:00',12,12000,'s05');
INSERT INTO  Flight VALUES('F0622','AIRASIA','Bangalore','Vizag','2022-12-15 4:00:00','2022-12-15 5:15:00',22,14000,'s02');
INSERT INTO  Flight VALUES('flall','INDIGO','Bangalore','Hyderabad','2022-12-21T21:40','2022-12-20T21:36',1,5000,'s01');
INSERT INTO  Flight VALUES('flaall','INDIGO','Bangalore','Hyderabad','2022-12-21 21:40','2022-12-20 21:36',1,5000,'s01');
INSERT INTO  Flight VALUES('zflall','INDIGO','Bangalore','Hyderabad','2022-12-23 21:00','2022-12-23 20:59',1,10,'s01');
INSERT INTO  Flight VALUES('E7012','INDIGO','Bangalore','Hyderabad',TO_TIMESTAMP('2022-12-18 22:27'),TO_TIMESTAMP('2022-12-18 22:27'),1,5000,'s01')
SELECT * FROM Flight 
DELETE FROM Flight WHERE Flight_no='zflall' ;


SELECT *  FROM Flight WHERE TO_DATE(Arrival) AS  Arrival;

select TO_DATE() from Flight;


select * FROM Flight WHERE CONVERT(VARCHAR(10),Arrival) = '10-JAN-2022'                     WHERE from_=bangalore and to_=Delhi
select to_char(cast(Arrival as date),'DD-MM-YYYY'), from_,to_ from Flight WHERE from_='Bangalore' and to_='Delhi' ;

Select TRUNC(Arrival) FROM Flight;

select * FROM Flight WHERE TRUNC(Arrival)='2022-01-10' and from_='Bangalore' and to_='Delhi' ;

select * FROM Flight WHERE to_char(cast(Arrival as date),'YYYY-MM-DD')='2022-01-10' and from_='Bangalore' and to_='Delhi' ;

select dbms_random.string('X', 6) str from dual;

DROP TABLE Security_Officer;
CREATE TABLE Security_Officer(sec_id varchar(10) PRIMARY KEY, SFName varchar(30),SLName varchar(30), SArea varchar(255), SPIN varchar(7),Gate_no varchar(10));
INSERT INTO Security_officer VALUES ('sec01','nandi','reddy','hyd','560025','G01');

INSERT INTO Passenger(PNR,Fname,Lname,Gender,Nationality,Security_Status,checkin_status,checkin_status,Flight_no,staff_id,sec_id) 
SELECT PNR,Fname,Lname,Gender,Nationality,Security_Status,checkin_status,checkin_status,Flight_no,staff_id,sec_id  from  Passenger 
where (PNR=select dbms_random.string('X', 6) str from dual,Fname='sai',Lname='aswath',Gender='Male',Nationality='Indian',Security_Status='yes',checkin_status='yes',Flight_no='B0731',staff_id='s01',sec_id='sec01')

DROP TABLE Passenger;
CREATE TABLE Passenger(PNR varchar(20) PRIMARY KEY,Fname varchar(30),Lname varchar(30),Gender varchar(10),Nationality varchar(10),Security_Status varchar(10),checkin_status varchar(10),Flight_no varchar(30),staff_id varchar(20),sec_id varchar(10), FOREIGN KEY(Flight_no) REFERENCES Flight(Flight_no), FOREIGN KEY(staff_id) REFERENCES Staff(Staff_id),FOREIGN KEY(sec_id) REFERENCES Security_Officer(sec_id));
INSERT INTO Passenger VALUES('6387W0','sai','aswath','Male','Indian','yes','yes','E7037','s01','sec01','2C');
SELECT * FROM Passenger
SELECT * FROM Passenger WHERE PNR='XZ2S2J' and Fname='sai' and Lname='aswath'

SELECT * FROM Passenger WHERE Flight_no='E7037'

select seat_no from Passenger where Flight_no='E7037'


INSERT INTO Passenger VALUES('XZ2S2J','sai','aswath','Male','Indian','yes','yes','E7037','s01','sec01')

ALTER SESSION SET NLS_DATE_FORMAT='YYYY-MM';
ALTER TABLE Passenger ADD seat_no VARCHAR(10)

DROP TABLE Webvisitor_card;
CREATE TABLE Webvisitor_card(Cookie_no varchar(10)PRIMARY KEY,card_no varchar(20),card_name varchar(30),cvv varchar(5),exp_date DATE);
INSERT INTO Webvisitor_card VALUES('ck7526','0000-1236-1236-1235','sai','235','2022-04')
INSERT INTO Webvisitor_card VALUES('ck5022','9632-9632-3654-6324','sdrtfyguhijokjiuhgyftdr','636','2022-11')
INSERT INTO Webvisitor_card VALUES('ck9426','0000-1236-1236-1235','sai','235','2022-04')
INSERT INTO Webvisitor_card VALUES('ck9496','0000-1236-1236-1235','sai','235','2022-04')
INSERT INTO Webvisitor_card VALUES('ck49426','0000-1236-1236-1235','sai','235','2022-10')
INSERT INTO Webvisitor_card VALUES('ck46426','0000-1236-1236-1235','sai','235',TO_DATE('1989-12','YYYY-MM'))


SELECT * FROM Webvisitor_card

SELECT * FROM Flight NATURAL JOIN Passenger;
Select PNR,concat(Fname, concat(' ', Lname)),Flight.Flight_no,from_,to_,Arrival from Passenger, Flight where Passenger.Flight_no = Flight.Flight_no 
XZ2S2J
SELECT * FROM Passenger WHERE Flight_no='E7037'
UPDATE Passenger set Security_Status='no'



CREATE TABLE Passenger_ph(PNR varchar(20),phone_no varchar(10),CONSTRAINT passenger_ph_no PRIMARY KEY(PNR,phone_no));
INSERT INTO  Passenger_ph VALUES('','')
SELECT * FROM Passenger_ph


CREATE TABLE staff_ph(Staff_id varchar(10), phone_no varchar(10),CONSTRAINT staff_ph_no PRIMARY KEY(Staff_id,phone_no));
INSERT INTO staff_ph('s01','9448825994',)

SELECT seat_no FROM Passenger WHERE PNR=''

UPDATE Passenger set seat_no='4D',checkin_status='yes' WHERE PNR='AI1QW8'