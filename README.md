# 1. Project title
    SYSTEM FOR ENTERING DATA ON EMPLOYEES

# 2. Brief description of the project
The project was done as an integral part of the practice course "Python 
Developer - Advanced" in the company **ITOiP** (IT Training and Practice - 
https://itoip.rs).

System for management and entry of basic data on former and employed workers.

The application was made in Python, with the help of the PostgreSQL 
database management system. The 'Custom Tkinter' library was used to create 
the user interface.

Tables made as an example are in the archive 'tables.zip'.

# 3. The README.md file contents
#### 1. Project title
#### 2. Brief description of the project
#### 3. The README.md file contents
#### 4. Database and table structure
#### 5. Application description and usage

# 4. Database and table structure
Database name: "zaposleni"

Tables:

    radnici
        id_radnika          (varchar (10), primary key, not null)
                                                        # employee ID
        ime                 (varchar (20), not null),   # employee first name
        prezime             (varchar (20), not null),   # employee last name
        adresa              (varchar (40), not null),   # residential address
        telefon             (varchar (10), not null),   # employee phone
        email               (varchar (40)),             # employee email
        pozicija            (varchar (30), not null),   # employee position
        lokacija            (varchar (4), not null),    # employee's workplace
        istorija            (text, not null),           # employment history
        zaposlen            (boolean, not null),        # employed (yes/no)
        datum_zaposljavanja (date not, null),           # employment date
        prestanak_radnog_odnosa     
                            (date)      # date of termination of employment

    pozicije
        naziv               (varchar (30), primary key, not null)
                                                        # position name
        opis                (text, not null)            # responsibilities
        sektor              (varchar (15), not null)    # position sector

    lokacije
        sifra               (varchar (4), primary key, not null)
                                                        # location code
        pun_naziv           (varchar (25), not null)    # location full name
        adresa              (varchar (40), not null)    # workplace address

# 5. Application description and usage

## 5.1. Main Screen

The main screen contains the logo and name of the company, the title of the 
application and buttons for selecting actions in the application. Each 
button has a short explanation next to it, except for the 'Izađi' (Exit) 
button at the bottom of the screen, which is used to close the application.

![1 - Main Screen](https://github.com/kdkrle/employee_data/assets/59825527/2ecf1449-1fe3-4ff6-8a39-9636f42e5c32)

_Picture 1: Main Screen_

## 5.2 New employees

By pressing the 'New employees' button on the main screen, a new window 
opens in which there is a form for entering data about a new employee.

![2 - New Employees](https://github.com/kdkrle/employee_data/assets/59825527/1edaff12-a9da-4fe1-acb9-f92b80e15e9b)

_Picture 2: New Employees_

At the top of the window there is a small logo and the name of the company, 
next to it is the title of this window.

Below that is a frame called 'Employee ID' in which a new ten-digit ID is 
generated that does not exist in the database.

After that, there is a section called 'Lični podaci' (Personal data) in which 
there are fields for entering the name, surname, address, phone and email, 
if the latter exists. The first four input fields are required. If they are 
not filled in, a notification about unfilled fields pops up.

Then follows the frame with the name 'Podaci o zaposlenju' (Employment data),
in which the position of the new employee in the company, the name of the 
location of his workplace and the date of employment are entered.

Below is a notice about the tag that comes after the names of required fields.

At the bottom of this screen there is an 'Unesi' (Enter) button, which inserts 
the entered values into the database, and a 'Odustani' (Cancel) button, 
which closes the screen.

## 5.3 Data review

By pressing the 'Pregled podataka' (Data review) button on the main screen, 
we open a new window in which we can review the data of all employees who 
are current employed or used to be.

![3 - Data Review](https://github.com/kdkrle/employee_data/assets/59825527/804d248b-5d8d-4f64-9d0e-ee260f10cba0)

_Picture 3: Data Review_

A specific employee is selected from the 'Izbor radnika' (Employee 
Selection) drop-down menu. The employees are sorted by last name, and after 
the last name and first name there is also their ID number, because it is 
possible that there are workers with the same first and last name.

By selecting a worker, data is automatically written in the appropriate fields.

At the bottom is a 'Zatvori' (Close) button that closes this window.

## 5.4. Update

The 'Ažuriranje' (Update) button on the main screen takes us to the form 
which updates existing data. At the top, there is again a logo with the 
name of the company, as well as the title of this form.

![4a - Update (upper part)](https://github.com/kdkrle/employee_data/assets/59825527/edcf1fd3-c149-4623-a6cc-4e230e32b021)

_Picture 4: Update (upper part)_

![4b - Update (bottom part)](https://github.com/kdkrle/employee_data/assets/59825527/de23fb85-6dfd-4c3a-843f-14b2820859be)

_Picture 5: Update (bottom part)_

Next is the frame called 'Kriterijumi' (Criteria) in which we can use criteria 
(filters) to reduce the list for selecting workers. At the top of the frame 
is the basic information for using these filters, followed by drop-down 
menus with the selection of workers in a specific position, in a specific 
location, or by whether the worker is still employed or not.

Selecting one of the filters also changes the list for selecting workers. 
If no filter is selected, the 'Izbor radnika' (Employee Selection) drop-down 
list contains all employees from the database.

Below the filters is the 'Izbor radnika' (Employee Selection) frame where 
we select the employee whose data needs to be updated. By selecting a 
worker from the drop-down menu, the data in this and the next frame is 
automatically displayed. In this frame there is also the employee ID, which 
cannot be changed, and information about whether the worker is still 
employed or not.

The next box 'Podaci za menjanje' (Data to change) has three columns. The 
first column contains the data names, the second the current data from the 
database, and the third the input fields, drop-down menus and date 
selection fields. The data can be updated due to its change or bad entry in 
the database. All, several data or only one of them can be changed.

The 'Ažuriraj' (Update) button inserts new data into the associated tables. 
The 'Resetuj' (Reset) button removes filters, worker selection and all data, 
so we can select and enter everything from the beginning. The 'Zatvori' 
(Close) button, of course, closes this window.

## 5.5. Reports

Pressing the 'Izveštaji' (Reports) button on the main screen opens a new 
window. In that window, at the top, we have the logo and the name of the 
company, next to which is the title of the window.

Below is a frame for choosing one of several options, which are also a short 
description of the results that we will get by opening a new form.

'Hijerarhija firme' (Company Hierarchy) is a graphic representation of the 
level of hierarchy in the company. Below the title and subtitle is a short 
legend and information to interpret this display. The display itself is 
below that in a separate frame 'Hijerarhija pozicija u firmi' (Hierarchy of 
positions in the company).

The option 'Spisak pozicija s odgovornostima' (List of positions with 
responsibilities) gives us an insight into the responsibilities that an 
employee has in the corresponding position.

The option 'Informacije o radnim mestima' (Workplace information) opens a 
new window with information in three columns. The first is a short 
designation for the workplace, the second is the full name of the workplace, 
and the third is the location, i.e. the address where the workplace is 
located.

The last option 'Delokrug sektora' (Sector Scope) takes us to a form that 
shows which sectors exist in the company and which job positions belong to 
which sectors.

## 5.6 Graphics

Pressing the last button on the main form opens a window for selecting one 
of the graphics or charts. There is a choice of ten different types of 
graphical representation of the relationship between the data we have.
