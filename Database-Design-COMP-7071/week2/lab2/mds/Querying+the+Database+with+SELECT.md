Relational Database Systems



  Querying the Database
      with SELECT




                              1 of 37
Introduction:
The goal of this document is to serve as an introduction to querying a database using the SELECT
statement. The SELECT statement has a number of parts and can perform many different tasks for
retrieving data from the database.

A SELECT statement has the following parts or clauses:
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY;
Each clause in the SELECT statement (aside from SELECT itself) is optional, i.e. FROM is optional,
WHERE is optional, etc. The individual optional clauses can be combined or omitted as needed.

Although the SELECT statement can retrieve data from multiple tables at once, in this lab we will focus
on retrieving data from a single table.

Knowing how to properly use the SELECT statement only comes from practice and with experience in a
wide variety of scenarios. We will attempt to cover many of the common scenarios in this lab.




                                                                                                     2 of 37
Step 1:
Open MySQL Workbench.

Step 2:
Import the SaleCo database.

For this lab we will be using the saleco database which we will import.

From the "File" Menu click on "Open SQL Script…"




Find the saleco_mysql.sql file and Click "Open".




                                                                          3 of 37
The file should look like this:




Click Execute     .

If everything is successful you should see a lot of output in the output section.
Have a quick scroll through to see if there are any errors (Warnings are OK, but errors need to be fixed
before moving on).




                                                                                                   4 of 37
If you refresh the database view you should see the following database and tables:




Step 3:
Reverse engineer the database (create an ERD from the database).

MySQL Workbench has a cool feature. It lets us create an ERD from an existing database. This
feature is called "Reverse Engineer".

Let's create an ERD from the saleco database.

From the "Database" Menu, click "Reverse Engineer…".




This will bring up a wizard for the next steps.




                                                                                               5 of 37
6 of 37
When prompted, fill in the login information for the localhost.

Next, select only the saleco database.




Make sure all table objects are select and Click "Finish".




What you should get is an ERD similar to the diagram below.

IMPORTANT! Take a moment to arrange the entities so that they don't overlap each other or other
relationship lines.

Submit a screenshot that shows the ERD for the database.

Filename: 01_SaleCo_ERD.jpg




                                                                                          7 of 37
Type USE saleco; and execute the command.

This will set your default database to saleco and let MySQL know in which database to look for our
tables. Without this, it may look for our tables from within the wrong database and give us error
messages.

Step 4:
Explore some of the simplest SELECT statements.

Scenario 1: Show all rows and all columns from a single table
Scenario 1 is one of the simplest SELECT statements implementing only 1 of the optional clauses - the
FROM clause. Right after the SELECT keyword we use an asterisk '*' to indicate all of the columns.
Let's give it a try. Our database has the following 7 tables:

    1.   Vendor
    2.   Product
    3.   Customer
    4.   Employee
    5.   Emp
    6.   Invoice
    7.   Line


Let's see all the rows and columns for the customer table.
Write the SQL command to display all the values from the customer table
You should get back all 10 customer rows and all 7 columns (CUS_CODE, CUS_LNAME, CUS_FNAME,
CUS_INITIAL, CUS_AREACODE, CUS_PHONE, CUS_BALANCE).

Remember that, although UPPERCASE and lowercase are both permitted for writing queries, by convention we
use UPPERCASE for SELECT keyword clauses like SELECT and FROM. This helps us with readability.

Write a simple SELECT statement to retrieve all the rows and columns for the other 6 tables:

    1.   Vendor
    2.   Product
    3.   Employee
    4.   Emp
    5.   Invoice
    6.   Line




                                                                                                8 of 37
Step 5:
SELECT only some of the columns.

Scenario 2: Show all rows and some columns from a single table

(Use appropriate tables for the following queries)
Write a SQL query to get back the customer’s name (last, first, and middle initial) and their customer balance.
Write a SQL query to get back the product’s code, description and price.

From the vendor table, retrieve all rows, but only the vendor name, areacode, phone, and state:


Submit a screenshot that includes the query and the resultset.


Filename: 02_Scenario_2.jpg

Step 6:
Compute a derived value.

Scenario 3: Show all rows and compute some columns from a single table
Similarly to Scenario 2, we can retrieve all the rows from a table and some of the columns, but those
columns could include a calculation to compute a derived value.

Remember derived values are derived from other columns and/or functions.

For good database design, we split people's names into first name, last name and middle name. But
what if we want to recombine those into a single name? We could add the text for first name together
with the text from last name (also known as concatenating 2 strings together).

CONCAT() Function in MySQL

The CONCAT() function in MySQL is used to combine (concatenate) two or more strings into one.

Basic Syntax

SELECT CONCAT(string1, string2, ..., stringN) AS result;

And this is what that looks like in a SELECT statement -

Type this and execute:
SELECT CONCAT(CUS_FNAME, ' ', CUS_LNAME)
FROM CUSTOMER;




                                                                                                   9 of 37
Notice here that in the resultset, MySQL doesn't know what to call the column and so it names it based
on the function we used. We can easily fix this, by giving the column an alias. An alias is just a nickname
for the column so it looks better in the resultset.
Write a SQL query to give an alias name to the derived column as “Full Name”
By adding the AS "Full Name" after the calculation of the derived value, we'll see our alias instead
of "No column name". You should put double quotes around your alias, if your alias includes spaces.

Note: this works for any other columns as well (i.e. column aliases aren't just for derived values).

Age is a derived value that probably shouldn't be stored in the database because we can
calculate it based on birth date.
Type and Execute:
SELECT CONCAT(EMP_TITLE, ' ', EMP_FNAME, ' ', EMP_LNAME) AS "Name",
EMP_DOB AS "Birth Date",
YEAR(NOW())-YEAR(EMP_DOB) AS Age
FROM EMPLOYEE;




                                                                                                       10 of 37
In this query there are a few things new: the calculation for the age and the addition of middle initial
into our name. Let's take a moment to explain what's going on here.

The age calculation is a simplified calculation that takes the current year and subtracts the employee's
birth year. By typing YEAR() we are using a function where you can give it a date (inside the
parentheses) and it gives you back just the year portion of the date.
For example YEAR('2012-12-25') gives back 2012 since '2012-12-25' represents Dec 25, 2012
and 2012 is just the year portion of the date.

NOW() is another function, that provides us the current date. So YEAR(NOW()) is the current year and
YEAR(EMP_DOB) is the employee's birth year. Subtract these two numbers and we have the user's
age*.
                                                             *This is a simplified calculation for demonstration purposes,
                              if you want to know a more accurate calculation and all the gory details, ask your instructor.




                                                                                                                  11 of 37
Let's do another example where we calculate the line item subtotals for the invoices in the database.
Write a SQL query to select the following columns from the Line table: INV_NUMBER, LINE_NUMBER, P_CODE,
LINE_UNITS, LINE_PRICE. The last column should calculate the line item subtotals (LINE_UNITS *
LINE_PRICE)for the invoices in the database. Name the calculated column as “Subtotal”.

This gives us the subtotal for each line in the Line table by calculating the price (LINE_PRICE)
multiplied by the quantity (LINE_UNITS).

For all customers, provide their name in the format "LastName, FirstName" (ex: Ramas, Alfred) and their
full phone number (area code and phone number with a space in between) (ex: 615 844-2573).
Hint: Use the concat function as we did before

Submit a screenshot that includes the query and the resultset.


Filename: 03_Scenario_3.jpg




                                                                                                   12 of 37
Step 7:
Change the order of the rows.

Scenario 4: Show all rows and in a particular order from a single table
If we don't specify a sort order for our SELECT statement, we get what ever sort order our RDBMS
gives us back. This is usually the sort order of our primary key (or other index on the table). If this isn't
the sort order we want to have, we can specify a sort order using the ORDER BY clause.
Here's what that looks like:
SELECT {*|column1, column2}
FROM <table>
ORDER BY <columnA>;
  (replace <table> with your specific table name)
  (replace {*|column1, column2…} with either * for all columns, or a list of columns from the
table)
  (replace <columnA> with a column from the table (columnA doesn't need to match the column1…
list))

You can also specify ascending or descending sort order (i.e. lowest values first or highest values first).

Use ASC for ascending or DESC for descending. ASC is the default.

Write a SQL query to list all employees' names sorted by last name:

Write a SQL query to see all the customers with the highest outstanding balances at the top.
Write a SQL query to show all the products (product code, description and price) ordered with the most
expensive on the top.

Submit a screenshot that includes the query and the resultset.




                                                                                                        13 of 37
Filename: 04_Scenario_4.jpg




                              14 of 37
Step 8:
Change the order of the rows - sort based on multiple columns.

Scenario 5: Show all rows and in a particular order (using multiple columns)
from a single table
When there are duplicates in the first sorted column, we may want to sort those similar rows by another
column as well. When we sort the employees by last name, we have 3 people with the last name
'Smith'. If we don't sort on another column, those 3 Smiths will come back in any order that the RDBMS
wants to provide. Let's fix this and sort by first name as well.

Here's what that looks like:
SELECT {*|column1, column2}
FROM <table>
ORDER BY {columnA, columnB…}
 (replace <table> with your specific table name)
 (replace {*|column1, column2…} with either * for all columns, or a list of columns from the
table)
 (replace {columnA,columnB…} with a list of columns from the table (the column1… list doesn't
need to match the columnA… list))


To sort the customers by last name and first name –

Write a SQL query to sort the customer records by the last name and then by first name.

The result set should look like this.




                                                                                                15 of 37
Write a SQL query that sorts employees by first, middle and last names (in that order). Submit a screenshot that
includes the query and the resultset.

Filename: 05_Scenario_5.jpg




                                                                                                 16 of 37
Step 9:
Get only the top rows in a particular order.

Scenario 6: Show only the top rows and in a particular order from a single table
For tables that have lots of rows and we only want to see the first few results, we can limit the number
of rows that get returned. This is often combined with particular order to get back the 'top' values.

Here's what that looks like:
SELECT {*|column1, column2}
FROM <table>
ORDER BY {columnA, columnB…}
LIMIT <x>;

 (replace <x> with the number of rows to limit the resultset to. i.e.)
 (replace <table> with your specific table name)
 (replace {*|column1, column2…} with either * for all columns, or a list of columns from the
table)
 (replace {columnA,columnB…} with a list of columns from the table (the column1… list doesn't
need to match the columnA… list))


Example (shows only the 5 oldest people):
SELECT firstName, lastName
FROM Person
ORDER BY birthDate ASC
LIMIT 5;
To get the 5 oldest employees -

Type and execute:
SELECT
CONCAT(EMP_TITLE, ' ', EMP_FNAME, ' ', EMP_LNAME) AS "Name", EMP_DOB,
YEAR(NOW())-YEAR(EMP_DOB) AS "Age"
FROM EMPLOYEE
ORDER BY EMP_DOB
LIMIT 5;




                                                                                                  17 of 37
To get the 5 newest employees -

Type and execute:
SELECT CONCAT(EMP_TITLE, ' ', EMP_FNAME, ' ', EMP_LNAME) AS "Name",
EMP_HIRE_DATE, YEAR(GETDATE())-YEAR(EMP_HIRE_DATE) AS "Age"
FROM EMPLOYEE
ORDER BY EMP_HIRE_DATE DESC
LIMIT 5;




                                                                 18 of 37
Create a query to list the 3 most expensive products:

Submit a screenshot that includes the query and the resultset.


Filename: 06_Scenario_6.jpg




Step 10:
Get only the rows that match what you want.

Scenario 7: Show only the rows that match a condition from a single table
We sometimes want to search for rows that match a condition and show only these rows. For this we
have the WHERE clause. The WHERE clause can test each row for certain conditions so that we only
show rows that for example:

    •   Must have a birthdate of April 11, 1995.
    •   Must have a first name of 'Ryota' AND last name of 'Berkovich'
    •   Must have a price between $20 and $45.
    •   Must have an office in 'BC', 'AB' or 'ON'
    •   … and many more




                                                                                             19 of 37
It's very common to only show a single row based on it's primary key. That's one of the benefits of the
primary key!
Create a query to get the customer with the CUS_CODE equal to 10016.

Create a query to combine 2 criteria together using the AND operator to give us the customer or
customers with the first name of 'James' and last name of 'Brown'.

The result should look like this




We can also the OR operator to look for rows that might match one or the other criteria.
Create a query that shows customers with the first name of 'Anne' or last name of 'Brown'.




Our product table allows for NULLs in the vendor code column (V_CODE). This means that if a product
currently doesn't have a vendor (because the vendor went out of business or temporarily don't sell that
product at the moment) the V_CODE will be NULL. Unfortunately using the equals operator won't work
when finding a match on NULLs. Instead we need to use IS NULL.




                                                                                                  20 of 37
This will not work to show all products that don't have a vendor:
SELECT P_CODE, P_DESCRIPT, P_PRICE, P_DISCOUNT, V_CODE
FROM PRODUCT
WHERE V_CODE = NULL;




Instead, we use to show all products that don't have a vendor:
SELECT P_CODE, P_DESCRIPT, P_PRICE, P_DISCOUNT, V_CODE
FROM PRODUCT
WHERE V_CODE IS NULL;




Type and execute the above examples and see the difference.




                                                                    21 of 37
To show all products that have a vendor, we use IS NOT NULL.

Type and execute:
SELECT P_CODE, P_DESCRIPT, P_PRICE, P_DISCOUNT, V_CODE
FROM PRODUCT
WHERE V_CODE IS NOT NULL;




                                                               22 of 37
Using the LIKE operator we can do pattern matching to find words and phrases that match the text we
want.

For example, to look for a product with a product description that contains the word saw we could use –

Create a query which displays all the p_code, p_decsript, p_price, p_discount and v_code where the

description contains the word “saw”;

Hint: Use the % symbol, as a special character, to indicate any other character. This way 'saw' could be at
the beginning of the description, at the end, or anywhere in the middle.




Create a query to all the 'hammer' products:

Submit a screenshot that includes the query and the resultset.


Filename: 07_Scenario_7A.jpg




                                                                                                   23 of 37
Create a query for all the 'hammer' products and make sure we have a vendor this time:

Submit a screenshot that includes the query and the resultset.


Filename: 08_Scenario_7B.jpg




                                                                                         24 of 37
In our WHERE clause we can also specify a list using the IN operator. This will check to see which rows
match any of the items in the list. This is equivalent to using the OR operator for each item on our list.


Create a query find all the vendors in Georgia (GA) and Kentucky (KY) and in order (order by v_state). Use IN
operator.




Create a query to show all employees with a title in 'Ms.', 'Mrs.':

Submit a screenshot that includes the query and the resultset.


Filename: 09_Scenario_7C.jpg




                                                                                                     25 of 37
Using the BETWEEN operator we can see if rows fit into a range of values.

Let's find all the baby boomers (born in 1946 to 1964) in the employee table.

Create a query to select the EMP_NUM, EMP_LNAME, EMP_FNAME, EMP_DOB, EMP_HIRE_DATE where the
employee date of birth is between '1946-01-01' AND '1964-12-31';




Can you find all products which have a price between $20 and $50?

Submit a screenshot that includes the query and the resultset.


Filename: 10_Scenario_7D.jpg




                                                                                  26 of 37
Step 11:
Get summary information (using aggregate functions) from a table.

Scenario 8: Show summary information from a single table
There are 5 aggregate functions that can provide summary information:

    •   COUNT()       Provides a count of the number of rows.
    •   SUM()         Provides a mathematical sum (addition) of all values in a column.
    •   AVG()         Provides the mathematical average (mean) of all values in a column.
    •   MIN()         Provides the smallest value for a column.
    •   MAX()         Provides the largest value for a column.



Here's what that looks like:
SELECT <AGGREGATE(column1)>
FROM <table>;
 (replace <table> with your specific table name)
 (replace <AGGREGRATE> with one of the 5 aggregate functions and replace column1 with column
from the table.)

Example (get the number of rows in the Person table):
SELECT count(*)
FROM Person;



Let's count the number of rows in the employee table -

Type and execute:
SELECT COUNT(*) AS "Number of Employees"
FROM EMPLOYEE;




                                                                                            27 of 37
Let's find out how much all of our employees owe us (all outstanding balances) -

Type and execute:
SELECT SUM(CUS_BALANCE)
FROM CUSTOMER;




To show the first and last employee number -

Type and execute:
SELECT MIN(EMP_NUM) AS 'First Employee Number',
MAX(EMP_NUM) AS 'Last Employee Number'
FROM EMPLOYEE;




                                                                                   28 of 37
To show the number of products and average price for a specific vendor with vendor code 24288.

Type and execute:
SELECT COUNT(*) AS "Number of Products",
AVG(P_PRICE) AS "Average Price"
FROM PRODUCT
WHERE V_CODE = 24288;




Your turn:

Show the first and last customer code from the customer table.

Submit a screenshot that includes the query and the resultset.


Filename: 11_Scenario_8A.jpg




                                                                                                 29 of 37
Show the number of products that have vendors.

Submit a screenshot that includes the query and the resultset.


Filename: 12_Scenario_8B.jpg




Step 12:
Get summary information (using aggregate functions) from groups of rows in a table.

Scenario 9: Show summary information from groups of rows from a single table
With our 5 aggregate functions we can provide summary information on the whole table,
and groups of rows as well. In order to produce groups of rows, we use the GROUP BY clause.

Here's what that looks like:
SELECT <AGGREGATE(column1)> {columnA, columnB…}
FROM <table>
GROUP BY {columnA, columnB…};
 (replace <table> with your specific table name)
 (replace <AGGREGATE> with one of the 5 aggregate functions and replace column1 with column
from the table.)
 (replace {columnA, columnB…} with a list of columns from the table)
 (note: you can't put a column in the select section that isn't in the group by section)

Example (get the number of people with different eye colors from the person table):
SELECT count(*)
FROM Person
GROUP BY eyeColor;




                                                                                              30 of 37
I want a count of all the vendors, but not just for the entire vendor table, I want it broken down by state-

Type and execute:
SELECT V_STATE, COUNT(*) AS 'Count by State'
FROM VENDOR
GROUP BY V_STATE;




Can you count the number of customers in each areacode?

Submit a screenshot that includes the query and the resultset.


Filename: 13_Scenario_9A.jpg




                                                                                                    31 of 37
Let's calculate the total cost of each of the invoices (represented in the line table).

Type and execute:
SELECT INV_NUMBER, SUM(LINE_UNITS*LINE_PRICE) AS 'Invoice Total'
FROM LINE
GROUP BY INV_NUMBER;




To show the number of products and average price for a each of the vendors -

Type and execute:
SELECT V_CODE, COUNT(*), AVG(P_PRICE)
FROM PRODUCT
GROUP BY V_CODE;




                                                                                          32 of 37
Provide me a count of each Mr., Ms. and Mrs from the employee table.

Submit a screenshot that includes the query and the resultset.


Filename: 14_Scenario_9B.jpg




Step 13:
Get summary information (using aggregate functions) from a table with certain restrictions.

Scenario 10: Show summary information with restrictions from a single table
Let's say you want to know everyone who has the same last name as someone else (non unique last
name).

We know how to get a list of last names and a count of each them with:
SELECT EMP_LNAME, COUNT(*)
FROM employee
GROUP BY EMP_LNAME

But this will show records for all the last names. Some are going to be unique (a count of 1) and others
may have more (non unique). How do we show only those that are non unique? Answer: the HAVING
clause. The HAVING clause can check the result of an aggregate function and restrict the resultset to
only those rows.

Here's what that looks like:
SELECT <AGGREGATE(column1)> {columnA, columnB…}
FROM <table>




                                                                                                   33 of 37
GROUP BY {columnA, columnB…}
HAVING <restriction>;
 (replace <table> with your specific table name)
 (replace <AGGREGATE> with one of the 5 aggregate functions and replace column1 with column
from the table.)
 (replace {columnA, columnB…} with a list of columns from the table)
 (replace <restriction> with an aggregate function and a condition)
 (note: you can't put a column in the select section that isn't in the group by section)


Example (get the number of people with different eye colors from the person table but only if that count
is larger than 100):
SELECT count(*)
FROM Person
GROUP BY eyeColor
HAVING count(*) > 100;



Find from the employees table all non unique last names -

Type and execute:
SELECT EMP_LNAME, COUNT(*)
FROM employee
GROUP BY EMP_LNAME
HAVING COUNT(*) >= 2;




                                                                                                 34 of 37
Find the most expensive invoices (invoices over $100).

Submit a screenshot that includes the query and the resultset.


Filename: 15_Scenario_10.jpg




                                                                 35 of 37
Step 14:
Get data from similar tables.

Scenario 11: Show rows from one table and similar rows from another
In the case where we have similar tables, for example employees and customers (they all have first
name, last name and middle initial), we may want to get rows from both tables. This is where we can
use the UNION ALL clause. The UNION ALL clause takes 2 SELECT statements and gives back the
rows of the 1st SELECT and the rows of the 2nd SELECT.

In the case of employees and customers, we know how to get rows from the employees table:

SELECT EMP_FNAME, EMP_INITIAL, EMP_LNAME
FROM employee;

And we know how to get rows from the customers table:
SELECT CUS_FNAME, CUS_INITIAL, CUS_LNAME
FROM customer;

As long as the number of columns (both have first name, last name and middle initial) and the data
types of those columns match (the first name of employee is varchar() and the first name of customer is
varchar()), we can do a UNION ALL to get a list of all people (employees and customers). Maybe we
want to invite everyone to a really big party?!
Here's what that looks like:
<SELECT#1>
UNION ALL
<SELECT#2>;
 (replace <SELECT#1> with any valid SELECT statement)
 (replace <SELECT#2> with any valid SELECT statement)
 (just make sure that the number and data types of the columns match - or MS SQL will get mad at you
and give you an error message!)


Example (get all the employees and customers in one resultset):
SELECT EMP_FNAME, EMP_INITIAL, EMP_LNAME
FROM employee;
UNION ALL
SELECT CUS_FNAME, CUS_INITIAL, CUS_LNAME
FROM customer;




                                                                                                36 of 37
Get all the employees and customers (with their phone numbers) -

Type and execute:
SELECT EMP_FNAME, EMP_LNAME,
EMP_AREACODE, EMP_PHONE,
'Employee' AS 'Type'
FROM EMPLOYEE
UNION ALL
SELECT CUS_FNAME, CUS_LNAME,
CUS_AREACODE, CUS_PHONE,
'Customer' AS 'Type'
FROM CUSTOMER;




Phew! … And we are done!

Please include all the screenshots in a document and submit them as one word file or a pdf file.
Please DO NOT submit Zip files or individual screenshots. The submission is strictly restricted to one file that contains
all the screenshots (query and the result grid clearly visible to the lab instructor).


                                                                                                         37 of 37
