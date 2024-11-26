CREATE TABLE Staff(Staff_id varchar(20) PRIMARY KEY, FFIName varchar(30), LFIName varchar(30), Area varchar(255), PIN NUMBER(7));
INSERT INTO staff VALUES('s01','rithivika','alapati','hyd',560016);

CREATE TABLE staff_ph(Staff_id varchar(10), phone_no varchar(10),CONSTRAINT staff_ph_no PRIMARY KEY(Staff_id,phone_no));

CREATE TABLE Security_Officer(sec_id varchar(10) PRIMARY KEY, SFName varchar(30),SLName varchar(30), SArea varchar(255), SPIN varchar(7),Gate_no varchar(10));

CREATE TABLE Security_Officer_ph(sec_id varchar(10),sec_phone_no varchar(10),CONSTRAINT security_ph PRIMARY KEY(sec_id,sec_phone_no));

CREATE TABLE webVisitorFlight(Flight_no varchar(20) PRIMARY KEY,cookie_id varchar(20), tckt_no  varchar(20));

CREATE TABLE Flight(Flight_no varchar(30) PRIMARY KEY,Flight_name varchar(30),from_ varchar(20),to_ varchar(20),Arrival TIMESTAMP,Departure TIMESTAMP,Available_seats varchar(50),price varchar(100),Staff_id varchar(20) REFERENCES Staff(Staff_id));
INSERT INTO  Flight VALUES('E7037','INDIGO','Bangalore','Delhi','10-JAN-2022','10-JAN-2022 12:00:00',20,5000,'s01');

CREATE TABLE Webvisitor_card(Cookie_no varchar(10),card_no varchar(20),card_name varchar(30),cvv varchar(5),exp_date DATE);
    
CREATE TABLE WebVisitor(Cookie_no varchar(10),ip_addr varchar(40), Loc varchar(255),email_id varchar(50),mobile_no varchar(10),Staff_id varchar(20),FOREIGN KEY(Staff_id) REFERENCES Staff(Staff_id));

CREATE TABLE Passenger_ph(PNR varchar(20),phone_no varchar(10),CONSTRAINT passenger_ph_no PRIMARY KEY(PNR,phone_no));

CREATE TABLE Passenger(PNR varchar(20) PRIMARY KEY,Fname varchar(30),Lname varchar(30),Gender varchar(10),Nationality varchar(10),Security_Status varchar(1),checkin_status varchar(1),Flight_no varchar(30),staff_id varchar(20),sec_id varchar(10), FOREIGN KEY(Flight_no) REFERENCES Flight(Flight_no), FOREIGN KEY(staff_id) REFERENCES Staff(Staff_id),FOREIGN KEY(sec_id) REFERENCES Security_Officer(sec_id));
INSERT INTO Passenger VALUES(select dbms_random.string('X', 6) str from dual,'sai','aswath');

CREATE TABLE FligSht(Flight_no varchar(30) PRIMARY KEY,Flight_name varchar(30),from_ varchar(20),to_ varchar(20),Arrival TIMESTAMP,Departure TIMESTAMP,Available_seats NUMBER(20),price NUMBER(20),Staff_id varchar(20) REFERENCES Staff(Staff_id));
INSERT INTO  Flight VALUES('E7036','INDIGO','Bangalore','Delhi','10-JAN-2022 09:00:00','10-JAN-2022 12:00:00',20,5000,'s01');

ALTER SESSION SET NLS_DATE_FORMAT='DD-MON-YYYY HH24:MI:SS';

select dbms_random.string('X', 6) str from dual;

















CREATE TABLE stafflogin(email varchar(50) UNIQUE,passsword varchar(50));
INSERT INTO stafflogin VALUES('team25@gmail.com','team25','TEAM25');
ALTER TABLE stafflogin ADD Staff_id varchar(20)
UPDATE  stafflogin SET name='Team25'
SELECT * FROM stafflogin;
DROP TABLE stafflogin;
