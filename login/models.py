from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)




class Staff(models.Model):
    staff_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=30, db_column="FFIName")
    last_name = models.CharField(max_length=30, db_column="LFIName")
    area = models.CharField(max_length=255, db_column="Area")
    pin = models.IntegerField(db_column="PIN")
    
 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Flight(models.Model):
    flight_no = models.CharField(max_length=30, primary_key=True)
    flight_name = models.CharField(max_length=30)
    from_city = models.CharField(max_length=20, db_column="from_")
    to_city = models.CharField(max_length=20, db_column="to_")
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    available_seats = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    staff = models.ForeignKey(
        Staff,
        db_column="Staff_id",
        on_delete=models.CASCADE,
        default="s01",
    )
    deleted = models.BooleanField(default=False)


class StaffPhone(models.Model):
    staff = models.ForeignKey(Staff, db_column="Staff_id", on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, db_column="phone_no")

    class Meta:
        unique_together = ["staff", "phone"]

class StaffLogin(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(
        max_length=50, db_column="passsword"
    )  # Note: 3 s's as per SQL
    staff = models.ForeignKey(Staff, db_column="Staff_id", on_delete=models.CASCADE)

class SecurityOfficer(models.Model):
    sec_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30, db_column="SFName")
    last_name = models.CharField(max_length=30, db_column="SLName")
    area = models.CharField(max_length=255, db_column="SArea")
    pin = models.CharField(max_length=7, db_column="SPIN")
    gate_no = models.CharField(max_length=10, db_column="Gate_no")
    email = models.EmailField(max_length=100, unique=True,null=True)
    password = models.CharField(max_length=100, db_column="passsword",null=True)


# In models.py, update Passenger class:

class Passenger(models.Model):
    pnr = models.CharField(max_length=20, primary_key=True)
    firstname = models.CharField(max_length=30, db_column="Fname")
    lastname = models.CharField(max_length=30, db_column="Lname")
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=10)
    security_status = models.BooleanField(default=False, db_column="Security_Status")
    checkin_status = models.BooleanField(default=False)
    flight = models.ForeignKey(Flight, db_column="Flight_no", on_delete=models.CASCADE)
    staff = models.ForeignKey(
        Staff,
        db_column="staff_id",
        on_delete=models.CASCADE,
        default='s01'  # Add default staff
    )
    security_officer = models.ForeignKey(
        SecurityOfficer, 
        db_column="sec_id", 
        on_delete=models.CASCADE,
        default='sec1'
    )
    seat_no = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Passenger {self.pnr} ({self.firstname} {self.lastname})"

class ContactUs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)



class SecurityOfficerPhone(models.Model):
    officer = models.ForeignKey(
        SecurityOfficer, db_column="sec_id", on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=10, db_column="sec_phone_no")

    class Meta:
        unique_together = ["officer", "phone"]



class WebVisitorFlight(models.Model):
    flight = models.OneToOneField(Flight, primary_key=True, on_delete=models.CASCADE)
    cookie_id = models.CharField(max_length=20)
    ticket_no = models.CharField(max_length=20, db_column="tckt_no")


class WebvisitorCard(models.Model):
    cookie_no = models.CharField(max_length=10)
    card_number = models.CharField(max_length=20, db_column="card_no")
    card_name = models.CharField(max_length=30)
    cvv = models.CharField(max_length=5)
    expiry = models.DateField(db_column="exp_date")


class WebVisitor(models.Model):
    cookie_no = models.CharField(max_length=10)
    ip_addr = models.CharField(max_length=40)
    location = models.CharField(max_length=255, db_column="Loc")
    email = models.EmailField(max_length=50, db_column="email_id")
    mobile = models.CharField(max_length=10, db_column="mobile_no")
    staff = models.ForeignKey(Staff, db_column="Staff_id", on_delete=models.CASCADE)



class PassengerPhone(models.Model):
    passenger = models.ForeignKey(Passenger, db_column="PNR", on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, db_column="phone_no")

    class Meta:
        unique_together = ["passenger", "phone"]

