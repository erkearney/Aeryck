There is an overwhelming amount of data in the world. We need a way to
**manage** that data. The most popular method for serious data storage and
manipulation is to use a *relational database*, along with **S**tructured
**Q**uery **L**anguage (SQL). In these next posts, we're going to learn how to
effectively use SQL to store, retrieve, and manipulate data. The mini-tutorial
will be split into four key sections:

### [Basic Data Manipulation (this post)](https://aeryck.com/post:SQL Basic Data Manipulation)
### [Joins and Relationships](https://aeryck.com/post:SQL Intermediate Querying and Joins)
### [Primary and Foreign Keys](https://aeryck.com/post:SQL Primary and Foreign Keys)
### [Transactions and ACID properties](https://aeryck.com/post:SQL Transactions and ACID Properties)
### [Views Procedures and Functions](https://aeryck.com/post:SQL Views Procedures and Functions)


[Other tutorials](https://www.postgresqltutorial.com/) will typically start by
having you download a 'toy database' to get started. This is because in
real-world applications it is overwhelmingly likely that you will be querying
and modifying an existing database, and rarely creating a new one from scratch.
That being said, this tutorial will start with us creating a tiny database from
scratch, so that we can be intimately familiar with the data and learn SQL with
a 'bottom-up' approach.

## Setup
The process for setting up an SQL will vary depending on which system you
choose, as well as your operating system. Instead of exhaustively covering
every possibility, I will simply refer you to the official installation
instructions for the two most popular systems:
[PostgreSQL](https://www.postgresqltutorial.com/postgresql-getting-started/)
and
[MySQL](https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing).
While I will be using PostgreSQL personally, all statements within this tutorial
will also work in a MySQL database, so feel free to setup whichever one you
prefer.


## Creating tables and inserting data
The *table* is the fundamental building block of relational databases. A
relational database must have at least one table (though there will almost
always be many more). A table can be created as:

```sql
CREATE TABLE us_presidents (
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    political_party VARCHAR(30)
);
```

Here we've created a table and given it the name "us_presidents". We've given
the table three columns: first_name, last_name, and political_party. In SQL, we
must specify the [datatype](https://www.w3schools.com/sql/sql_datatypes.asp)
of columns, be it INT, DATE, etc. In this case, we've set the datatype of each
column to VARCHAR(30), meaning a string of variable length, up to 30 characters.


So we have a table, but it's currently devoid of any data. We can insert data
into the table like so:

```sql
INSERT INTO us_presidents (first_name, last_name, political_party)
VALUES ('John', 'Adams', 'Federalist');
```

###### Despite being on two lines, the above is treated as a single statement, delimited by the semicolon. See the note below for more info.\*


###### It's worth noting that despite being three separate keywords, for all intents and purposes, INSERT, INTO, and VALUES are all just part of one command. You will never use one without the other two.

We've INSERTed a row INTO the *us_presidents* table here. When calling the
INSERT INTO statement, we must specify the table name as well as the columns of
that table that correspond with the data we are inserting. 

Notice how when calling INSERT INTO, we specify the columns first, then the data
using the VALUES keyword. We are not required to specify the columns in the same
order they appear in the table. For example:

```sql
INSERT INTO us_presidents (last_name, political_party, first_name)
VALUES ('Thomas', 'Jefferson', 'Democratic-Republican');
```

We just need to make sure the order of the data in the VALUES statement aligns
with the order of the columns we specify.

We can also leave a column completely blank should we wish:

```sql
INSERT INTO us_presidents (first_name, last_name)
VALUES ('George', 'Washington');
```

We didn't specify a political party for George Washington (because he never had
one, technically), so the political_party cell for him will simply be blank.

## Querying data
We've been INSERTing data into a table, but up until now we haven't been able to
see what we've been doing! Let's address that with the SELECT statement:

```sql
SELECT first_name, last_name, political_party
  FROM us_presidents;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">last_name</th>
    <th align="center">political_party</th>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Adams</td>
    <td align="left">Federalist</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">Jefferson</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">Washington</td>
    <td align="left">&nbsp; </td>
  </tr>
</table>
<p>(3 rows)<br />
</p>

###### In cases such as this, where we are SELECTing every column from a table, you can use the wildcard (\*) operator like so: SELECT * FROM us_presidents;. I'm going to avoid doing so in this tutorial to be as explicit as possible, but using it isn't "wrong" by any means.

When INSERTing, we could specify the columns in whichever order we want (or even
choose to omit columns altogether), the same is true with the SELECT statement:

```sql
SELECT political_party, last_name
  FROM us_presidents;
```

<table border="1">
  <tr>
    <th align="center">political_party</th>
    <th align="center">last_name</th>
  </tr>
  <tr valign="top">
    <td align="left">Federalist</td>
    <td align="left">Adams</td>
  </tr>
  <tr valign="top">
    <td align="left">Democratic-Republican</td>
    <td align="left">Jefferson</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
  </tr>
</table>
<p>(3 rows)<br />
</p>

There is **a lot** more we can do with the SELECT statement. To show more of its
capabilities, let's add more data to our us_presidents table. We can INSERT
multiple rows at once like so:

```sql
INSERT INTO us_presidents (first_name, last_name, political_party)
VALUES ('James', 'Madison', 'Democratic-Republican'),
       ('James', 'Monroe', 'Democratic-Republican'),
       ('John', 'Adams', 'Democratic-Republican'),
       ('Andrew', 'Jackson', 'Democratic'),
       ('Martin', 'Buren', 'Democratic'),
       ('William', 'Harrison', 'Whig');

SELECT first_name, last_name, political_party
  FROM us_presidents;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">last_name</th>
    <th align="center">political_party</th>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Adams</td>
    <td align="left">Federalist</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">Jefferson</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">Washington</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">Madison</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">Monroe</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Adams</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">Jackson</td>
    <td align="left">Democratic</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Buren</td>
    <td align="left">Democratic</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">Harrison</td>
    <td align="left">Whig</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

We can filter our query using **clauses**, the first of which we'll examine is
WHERE:

```sql
SELECT first_name, last_name, political_party
  FROM us_presidents
 WHERE first_name = 'James';
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">last_name</th>
    <th align="center">political_party</th>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">Madison</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">Monroe</td>
    <td align="left">Democratic-Republican</td>
  </tr>
</table>
<p>(2 rows)<br />
</p>

###### Notice the single equals sign here is checking for equality, not assigning as it would in languages such as Python and Java.

We can even use the WHERE clause to filter based on a column we don't want to
actually see in our output table:

```sql
SELECT first_name, last_name
  FROM us_presidents
 WHERE political_party = 'Democratic-Republican';
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">last_name</th>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">Jefferson</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">Madison</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">Monroe</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Adams</td>
  </tr>
</table>
<p>(4 rows)<br />
</p>

Have you noticed anything strange? 

```sql
SELECT first_name, last_name, political_party
  FROM us_presidents
 WHERE last_name = 'Adams';
```


<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">last_name</th>
    <th align="center">political_party</th>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Adams</td>
    <td align="left">Federalist</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Adams</td>
    <td align="left">Democratic-Republican</td>
  </tr>
</table>
<p>(2 rows)<br />
</p>

What's going on here? Well the first row is referring to [John
Adams](https://en.wikipedia.org/wiki/John_Adams), second President of the United
States, while the other row is for [John *Quincy*
Adams](https://en.wikipedia.org/wiki/John_Quincy_Adams), sixth President of the
United States. As a temporary fix to this issue, we can add a middle name column
to the table (we will discuss better methods for handling situations such as
these in the [next post](https://aeryck.com/post:10)).

```sql
ALTER TABLE us_presidents
  ADD middle_name VARCHAR(30);

SELECT first_name, middle_name, last_name
  FROM us_presidents;
```
<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">&nbsp; </td>
    <td align="left">Buren</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">&nbsp; </td>
    <td align="left">Harrison</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

Now we have a blank middle_name column, we can UPDATE John Adams to give him his
Quincy middle name:

```sql
UPDATE us_presidents
   SET middle_name = 'Quincy'
 WHERE last_name = 'Adams';

SELECT first_name, middle_name, last_name
  FROM us_presidents;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">political_party</th>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">Democratic</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">&nbsp; </td>
    <td align="left">Buren</td>
    <td align="left">Democratic</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">&nbsp; </td>
    <td align="left">Harrison</td>
    <td align="left">Whig</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Federalist</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Democratic-Republican</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

Oh no! That statement updated *both* John Adams'! But it we look back at our
query this makes perfect sense. We simply asked to make the middle_name of each
row WHERE last_name = 'Adams' equal to 'Quincy', We can write a statement that
specifically targets just on John Adams by using the AND clause. Let's go ahead
an update another president commonly known by his first, middle, and last names
as well.

```sql
UPDATE us_presidents
   SET middle_name = NULL
 WHERE last_name = 'Adams' AND political_party = 'Federalist';

UPDATE us_presidents
   SET middle_name = 'Van'
 WHERE first_name = 'Martin' AND last_name = 'Buren';

UPDATE us_presidents
   SET middle_name = 'Henry'
 WHERE first_name = 'William' AND last_name = 'Harrison';

SELECT first_name, middle_name, last_name, political_party
  FROM us_presidents;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">political_party</th>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">Democratic</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van </td>
    <td align="left">Buren</td>
    <td align="left">Democratic</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">Henry </td>
    <td align="left">Harrison</td>
    <td align="left">Whig</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Democratic-Republican</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Federalist</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

We've updated both John Adams (the first one) to get rid of the Quincy middle
name, and we've given the "Harrison" middle name to [William Henry
Harrison](https://en.wikipedia.org/wiki/William_Henry_Harrison) (We've also
updated Martin *van* Buren while we were at it). If that name sounds strangely
familiar, it's probably because William Henry Harrison is the man who died 31
days after becoming president. A tenure so short that one might argue he
shouldn't even be included in a list of presidents. We can entertain such an
argument with:

```sql
DELETE FROM us_presidents
 WHERE first_name = 'William' AND middle_name = 'Henry' AND last_name = 'Harrison';

SELECT first_name, middle_name, last_name
  FROM us_presidents;
```

###### Notice we can chain multiple AND clauses together.

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van </td>
    <td align="left">Buren</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
  </tr>
</table>
<p>(8 rows)<br />
</p>

In addition to the AND clause, there's also the OR and NOT clauses, and more.

As mentioned before, a relational database will almost always have more than one
table, so let's create a second one now:

```sql
CREATE TABLE us_states (
number SERIAL,
name VARCHAR(30),
region VARCHAR(30)
);
```

PostgreSQL uses the SERIAL keyword whereas other databases, such as MySQL use
the AUTO_INCREMENT keyword. Here is how you would create the same table in
MySQL:

```sql
CREATE TABLE us_states (
number INT AUTO_INCREMENT,
name VARCHAR(30),
region VARCHAR(30)
);
```

Here, we've created a table called us_states and given it three columns: number,
name, and region. Let's fill our new table with some data by INSERTing states
based on the order they joined the union:

```sql
INSERT INTO us_states (name, region)
VALUES ('Delaware', 'South'),
       ('Pennsylvania', 'Northeast'),
       ('New Jersey', 'Northeast'),
       ('Georgia', 'South'),
       ('Connecticut', 'Northeast'),
       ('Massachusetts', 'Northeast'),
       ('Maryland', 'South'),
       ('South Carolina', 'South'),
       ('New Hampshire', 'Northeast'),
       ('Virginia', 'South'),
       ('New York', 'Northeast'),
       ('North Carolina', 'South'),
       ('Rhode Island', 'Northeast');

SELECT number, name, region
  FROM us_states;
```

<table border="1">
  <tr>
    <th align="center">number</th>
    <th align="center">name</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="right">1</td>
    <td align="left">Delaware</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="right">2</td>
    <td align="left">Pennsylvania</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="right">3</td>
    <td align="left">New Jersey</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="right">4</td>
    <td align="left">Georgia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="right">5</td>
    <td align="left">Connecticut</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="right">6</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="right">7</td>
    <td align="left">Maryland</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="right">8</td>
    <td align="left">South Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="right">9</td>
    <td align="left">New Hampshire</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="right">10</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="right">11</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="right">12</td>
    <td align="left">North Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="right">13</td>
    <td align="left">Rhode Island</td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(13 rows)<br />
</p>

Notice we did *not* specify any values for the **number** column, yet the column
is populated anyway. This is because we've created this column to start at 1 and
automatically increment as each new row is added.

Now let's add a new column to us_presidents to house the home state of each
president. While we're at it, let's also give each president a number, to
indicate the order of presidential succession. You'll notice that accomplishing
this task requires a very verbose statement. This is because while adding new
columns to tables in a relational database is *possible* (we'll make it slightly
less painful using the CASE keyword, which allows us to implement a switch-like
statement), it is very *impractical*. Should you ever find yourself designing a
database, you'll need to put careful thought and consideration into the layout
of your tables. Adding new columns to a database that has already been deployed,
and populating them with data is no easy task:

```sql
UPDATE us_presidents
   SET number =
  CASE
  WHEN last_name = 'Washington' THEN 1
  WHEN last_name = 'Adams' AND middle_name IS NULL THEN 2
  WHEN last_name = 'Jefferson' THEN 3
  WHEN last_name = 'Madison' THEN 4
  WHEN last_name = 'Monroe' THEN 5
  WHEN last_name = 'Adams' AND middle_name = 'Quincy' THEN 6
  WHEN last_name = 'Jackson' THEN 7
  WHEN last_name = 'Buren' THEN 8
END;

UPDATE us_presidents
   SET home_state =
  CASE
  WHEN last_name = 'Washington' THEN 'Virginia'
  WHEN last_name = 'Adams' AND middle_name IS NULL THEN 'Massachusetts'
  WHEN last_name = 'Jefferson' THEN 'Virginia'
  WHEN last_name = 'Madison' THEN 'Virginia'
  WHEN last_name = 'Monroe' THEN 'Virginia'
  WHEN last_name = 'Adams' AND middle_name = 'Quincy' THEN 'Massachusetts'
  WHEN last_name = 'Jackson' THEN 'South Carolina'
  WHEN last_name = 'Buren' THEN 'New York'
END;

SELECT first_name, middle_name, last_name, home_state
  FROM us_presidents
 ORDER BY number;
```

###### Notice we had to be careful of John (Quincy)? Adams again

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">home_state</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">Virginia</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Virginia</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Virginia</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Virginia</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">South Carolina</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">&nbsp; </td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
  </tr>
</table>
<p>(8 rows)<br />
</p>

Here, we SELECTed and included the ORDER BY clause to sort our results, so we'd
have the first president in the first row (like when we used WHERE in the last
post, we can ORDER BY a column even if we didn't SELECT that column!)


### \*A brief word on SQL syntax and style
SQL is case-**in**sensitive, meaning that

```sql
SELECT id FROM People;
select id from people;
SeLeCt iD fRoM pEoPlE;
```

are all valid and equivalent statements. SQL statements are delimited with a
semicolon (;), regardless of white-space, meaning that

```sql
SELECT
id
FROM
People
;
```

Is also valid and equivalent to the statements above. All that being said, don't
allow yourself to become so preoccupied with whether or not you can, that you
forget to stop and think if you should. In fact, when writing anything at all,
I'd generally recommend finding a [style guide](https://www.sqlstyle.guide/) and
sticking to it. Virtually all SQL style guides agree that you should capitalize
every letter in reserved keywords (e.g., SELECT and FROM). I will be following
[Simon Holywell's style guide](https://www.sqlstyle.guide/) for all statements
in this tutorial, so statements will follow the form:

```sql
SELECT id FROM people;
```

In the [next tutorial](), we will learn about joins and relationships.
