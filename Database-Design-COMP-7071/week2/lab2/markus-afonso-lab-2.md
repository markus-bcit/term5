# Lab 2: Querying the Database with SELECT
**Name:** Markus Afonso

---

## 01. ERD Screenshot
**Requirement:** Submit a screenshot that shows the ERD for the database.
*(Insert `01_SaleCo_ERD.jpg` here)*

---

## 02. Scenario 2: Select Specific Columns
**Requirement:** From the vendor table, retrieve all rows, but only the vendor name, areacode, phone, and state.

```sql
SELECT V_NAME, V_AREACODE, V_PHONE, V_STATE 
FROM VENDOR;
```
*(Insert `02_Scenario_2.jpg` here)*

---

## 03. Scenario 3: Derived Values (Concat)
**Requirement:** For all customers, provide their name in the format "LastName, FirstName" and their full phone number (area code and phone number with a space in between).

```sql
SELECT 
    CONCAT(CUS_LNAME, ', ', CUS_FNAME) AS "Name", 
    CONCAT(CUS_AREACODE, ' ', CUS_PHONE) AS "Phone" 
FROM CUSTOMER;
```
*(Insert `03_Scenario_3.jpg` here)*

---

## 04. Scenario 4: Ordering Rows
**Requirement:** Write a SQL query to show all the products (product code, description and price) ordered with the most expensive on the top.

```sql
SELECT P_CODE, P_DESCRIPT, P_PRICE 
FROM PRODUCT 
ORDER BY P_PRICE DESC;
```
*(Insert `04_Scenario_4.jpg` here)*

---

## 05. Scenario 5: Multi-Column Sorting
**Requirement:** Write a SQL query that sorts employees by first, middle and last names (in that order).

```sql
SELECT * 
FROM EMPLOYEE 
ORDER BY EMP_FNAME, EMP_INITIAL, EMP_LNAME;
```
*(Insert `05_Scenario_5.jpg` here)*

---

## 06. Scenario 6: Top Rows (Limit)
**Requirement:** Create a query to list the 3 most expensive products.

```sql
SELECT * 
FROM PRODUCT 
ORDER BY P_PRICE DESC 
LIMIT 3;
```
*(Insert `06_Scenario_6.jpg` here)*

---

## 07. Scenario 7A: Pattern Matching (LIKE)
**Requirement:** Create a query which displays all the p_code, p_decsript, p_price, p_discount and v_code where the description contains the word “saw”.

```sql
SELECT P_CODE, P_DESCRIPT, P_PRICE, P_DISCOUNT, V_CODE 
FROM PRODUCT 
WHERE P_DESCRIPT LIKE '%saw%';
```
*(Insert `07_Scenario_7A.jpg` here)*

---

## 08. Scenario 7B: Pattern Matching + NULL Check
**Requirement:** Create a query for all the 'hammer' products and make sure we have a vendor this time.

```sql
SELECT P_CODE, P_DESCRIPT, P_PRICE, P_DISCOUNT, V_CODE 
FROM PRODUCT 
WHERE P_DESCRIPT LIKE '%hammer%' 
AND V_CODE IS NOT NULL;
```
*(Insert `08_Scenario_7B.jpg` here)*

---

## 09. Scenario 7C: IN Operator
**Requirement:** Create a query to show all employees with a title in 'Ms.', 'Mrs.'.

```sql
SELECT * 
FROM EMPLOYEE 
WHERE EMP_TITLE IN ('Ms.', 'Mrs.');
```
*(Insert `09_Scenario_7C.jpg` here)*

---

## 10. Scenario 7D: Range Check (BETWEEN)
**Requirement:** Can you find all products which have a price between $20 and $50?

```sql
SELECT * 
FROM PRODUCT 
WHERE P_PRICE BETWEEN 20 AND 50;
```
*(Insert `10_Scenario_7D.jpg` here)*

---

## 11. Scenario 8A: Aggregates (MIN/MAX)
**Requirement:** Show the first and last customer code from the customer table.

```sql
SELECT 
    MIN(CUS_CODE) AS "First Customer Code", 
    MAX(CUS_CODE) AS "Last Customer Code" 
FROM CUSTOMER;
```
*(Insert `11_Scenario_8A.jpg` here)*

---

## 12. Scenario 8B: Aggregates (COUNT)
**Requirement:** Show the number of products that have vendors.

```sql
SELECT COUNT(V_CODE) AS "Products with Vendors" 
FROM PRODUCT;
```
*(Insert `12_Scenario_8B.jpg` here)*

---

## 13. Scenario 9A: Group By
**Requirement:** Can you count the number of customers in each areacode?

```sql
SELECT CUS_AREACODE, COUNT(*) AS "Customer Count" 
FROM CUSTOMER 
GROUP BY CUS_AREACODE;
```
*(Insert `13_Scenario_9A.jpg` here)*

---

## 14. Scenario 9B: Group By (Titles)
**Requirement:** Provide me a count of each Mr., Ms. and Mrs from the employee table.

```sql
SELECT EMP_TITLE, COUNT(*) AS "Count" 
FROM EMPLOYEE 
WHERE EMP_TITLE IN ('Mr.', 'Ms.', 'Mrs.') 
GROUP BY EMP_TITLE;
```
*(Insert `14_Scenario_9B.jpg` here)*

---

## 15. Scenario 10: Having Clause
**Requirement:** Find the most expensive invoices (invoices over $100).

```sql
SELECT INV_NUMBER, SUM(LINE_UNITS * LINE_PRICE) AS "Invoice Total" 
FROM LINE 
GROUP BY INV_NUMBER 
HAVING SUM(LINE_UNITS * LINE_PRICE) > 100;
```
*(Insert `15_Scenario_10.jpg` here)*
