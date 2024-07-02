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

![5 - Reports](https://github.com/kdkrle/employee_data/assets/59825527/8384f9ce-a815-4df8-b4ef-8d4e2c70c5d8)

_Picture 6: Reports_

Below is a frame for choosing one of several options, which are also a short 
description of the results that we will get by opening a new form.

'Hijerarhija firme' (Company Hierarchy) is a graphic representation of the 
level of hierarchy in the company. Below the title and subtitle is a short 
legend and information to interpret this display. The display itself is 
below that in a separate frame 'Hijerarhija pozicija u firmi' (Hierarchy of 
positions in the company).

![5 1a - Company Hierarchy (upper part)](https://github.com/kdkrle/employee_data/assets/59825527/e2b1ed2a-a16f-4b46-8fe4-62b3a0f9ee27)

_Picture 7: Company Hierarchy (upper part)_

![5 1b - Company Hierarchy (bottom part)](https://github.com/kdkrle/employee_data/assets/59825527/52ecdab0-3034-4489-a2f3-2b508d7e8abc)

_Picture 8: Company Hierarchy (bottom part)_

The option 'Spisak pozicija s odgovornostima' (List of positions with 
responsibilities) gives us an insight into the responsibilities that an 
employee has in the corresponding position.

![5 2 - Positions and Responsibilities](https://github.com/kdkrle/employee_data/assets/59825527/e380d6aa-4d38-4946-ba4a-71d196ae29c8)

_Picture 9: Positions and Responsibilities_

The option 'Informacije o radnim mestima' (Workplace information) opens a 
new window with information in three columns. The first is a short 
designation for the workplace, the second is the full name of the workplace, 
and the third is the location, i.e. the address where the workplace is 
located.

![5 3 - Workplace Information](https://github.com/kdkrle/employee_data/assets/59825527/65d265fc-dd53-4a24-9bde-7bab620aa8dc)

_Picture 10: Workplace Information_

The last option 'Delokrug sektora' (Sector Scope) takes us to a form that 
shows which sectors exist in the company and which job positions belong to 
which sectors.

![5 4 - Sectors Scope](https://github.com/kdkrle/employee_data/assets/59825527/ebb777b1-42e8-4f97-9509-f3f293dad4af)

_Picture 11: Sectors Scope_

## 5.6 Graphics

Pressing the last button on the main form opens a window for selecting one 
of the graphics or charts. There is a choice of ten different types of 
graphical representation of the relationship between the data we have.

![6 - Graphics](https://github.com/kdkrle/employee_data/assets/59825527/a9d833da-e5f5-4cce-8c2f-e020708804d6)

_Picture 12: Graphics_

Examples:
![6 1 - Number of Positions per Sector](https://github.com/kdkrle/employee_data/assets/59825527/ad77bb7e-d968-417f-ac52-3ab1dae35ec6)

_Picture 13: Number of Positions per Sector_

![6 2 - Number of Employees per Employment Year](https://github.com/kdkrle/employee_data/assets/59825527/8da39aa2-ad45-46d3-b376-45033c911628)

_Picture 14: Number of Employees per Employment Year_

![6 3 - Number of Employees per Position](https://github.com/kdkrle/employee_data/assets/59825527/900f672b-b7a3-4af6-80c7-903ef1cd0d2e)

_Picture 15: Number of Employees per Position_

![6 4 - Number of Employees per Workplace](https://github.com/kdkrle/employee_data/assets/59825527/15128c4a-d087-4f67-aad3-75b5ee5571d4)

_Picture 16: Number of Employees per Workplace_

![6 5 - Percentage of Employees per Sector](https://github.com/kdkrle/employee_data/assets/59825527/e0f82a3c-a97a-46aa-9036-00ba789878d7)

_Picture 17: Percentage of Employees per Sector_

![6 6 - Ratio of Current and Former Employees](https://github.com/kdkrle/employee_data/assets/59825527/e14814f8-d86a-48d0-9f52-7918ed378fb0)

_Picture 18: Ratio of Current and Former Employees_

![6 7 - Ratio of Employees With Mobile and Landline Phones](https://github.com/kdkrle/employee_data/assets/59825527/54853c0f-69e3-4857-9230-fc3ed1c9d5e4)

_Picture 19: Ratio of Employees With Mobile and Landline Phones_

![6 8 - Ratio of Employees With and Without Email](https://github.com/kdkrle/employee_data/assets/59825527/d3b2bb99-e229-4053-8197-f60001438454)

_Picture 20: Ratio of Employees With and Without Email_

![6 9 - Ratio of Former and Current Employees per Workplace](https://github.com/kdkrle/employee_data/assets/59825527/babe94e8-1f21-430b-9b26-1e2668cfdb99)

_Picture 21: Ratio of Former and Current Employees per Workplace_

![6 10 - Ratio of Former and Current Employees per Position](https://github.com/kdkrle/employee_data/assets/59825527/b0b35423-27ab-4fc3-8c0c-57772f4d380c)

_Picture 22: Ratio of Former and Current Employees per Position_
