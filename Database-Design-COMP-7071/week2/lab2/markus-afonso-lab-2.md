# Lab 2: Querying the Database with SELECT
**Name:** Markus Afonso

---

## 01. ERD Screenshot
**Requirement:** Submit a screenshot that shows the ERD for the database.

01_SaleCo_ERD.jpg
![[Pasted image 20260122083701.png]]

---

## 02. Scenario 2: Select Specific Columns
**Requirement:** From the vendor table, retrieve all rows, but only the vendor name, areacode, phone, and state.

`02_Scenario_2.jpg` 
![[Pasted image 20260122105915.png]]

---

## 03. Scenario 3: Derived Values (Concat)
**Requirement:** For all customers, provide their name in the format "LastName, FirstName" and their full phone number (area code and phone number with a space in between).

`03_Scenario_3.jpg` 
![[Pasted image 20260122104232.png]]

---

## 04. Scenario 4: Ordering Rows
**Requirement:** Write a SQL query to show all the products (product code, description and price) ordered with the most expensive on the top.

`04_Scenario_4.jpg` 
![[Pasted image 20260122105100.png]]

---

## 05. Scenario 5: Multi-Column Sorting
**Requirement:** Write a SQL query that sorts employees by first, middle and last names (in that order).

`05_Scenario_5.jpg` 
![[Pasted image 20260122110725.png]]

---

## 06. Scenario 6: Top Rows (Limit)
**Requirement:** Create a query to list the 3 most expensive products.

`06_Scenario_6.jpg` 
![[Pasted image 20260122111017.png]]

---

## 07. Scenario 7A: Pattern Matching (LIKE)
**Requirement:** Create a query which displays all the p_code, p_decsript, p_price, p_discount and v_code where the description contains the word “saw”.

`07_Scenario_7A.jpg` 
![[Pasted image 20260122134650.png]]

 ---

## 08. Scenario 7B: Pattern Matching + NULL Check
**Requirement:** Create a query for all the 'hammer' products and make sure we have a vendor this time.

`08_Scenario_7B.jpg` 
![[Pasted image 20260122134856.png]]

---

## 09. Scenario 7C: IN Operator
**Requirement:** Create a query to show all employees with a title in 'Ms.', 'Mrs.'.

`09_Scenario_7C.jpg` 
![[Pasted image 20260122135245.png]]
---

## 10. Scenario 7D: Range Check (BETWEEN)
**Requirement:** Can you find all products which have a price between $20 and $50?

`10_Scenario_7D.jpg` 
![[Pasted image 20260122140301.png]]

---

## 11. Scenario 8A: Aggregates (MIN/MAX)
**Requirement:** Show the first and last customer code from the customer table.

`11_Scenario_8A.jpg` 
![[Pasted image 20260122140538.png]]

---

## 12. Scenario 8B: Aggregates (COUNT)
**Requirement:** Show the number of products that have vendors.

`12_Scenario_8B.jpg` 
![[Pasted image 20260122140707.png]]

---

## 13. Scenario 9A: Group By
**Requirement:** Can you count the number of customers in each areacode?

`13_Scenario_9A.jpg` 
![[Pasted image 20260122141120.png]]

---

## 14. Scenario 9B: Group By (Titles)
**Requirement:** Provide me a count of each Mr., Ms. and Mrs from the employee table.

`14_Scenario_9B.jpg` 
![[Pasted image 20260122141837.png]]


---

## 15. Scenario 10: Having Clause
**Requirement:** Find the most expensive invoices (invoices over $100).

`15_Scenario_10.jpg` 
![[Pasted image 20260122142746.png]]