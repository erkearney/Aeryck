There is an overwhelming amount of data in the world. We need a way to
**manage** that data. The most popular method for serious data storage and
manipulation is to use a *relational database*, along with **S**tructured
**Q**uery **L**anguage (SQL). In these next posts, we're going to learn how to
effectively use SQL to store, retrieve, and manipulate data. The mini-tutorial
will be split into four key sections:

### [Basic Data Manipulation (this post)](https://aeryck.com/post:9)
### [Joins and Relationships](https://aeryck.com/post:10)
### [Intermediate Querying](https://aeryck.com/post:11)
### [Functions and Aggregation](https://aeryck.com/post:12)
### [Transactions and Error Handling](https://aeryck.com/post:13)
### [Exercises](https://aeryck.com/post:14)

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
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    political_party VARCHAR(50)
);
```

Here we've created a table and given it the name "us_presidents". We've given
the table three columns: first_name, last_name, and political_party. In SQL, we
must specify the [datatype](https://www.w3schools.com/sql/sql_datatypes.asp)
of columns, be it INT, DATE, etc. In this case, we've set the datatype of each
column to VARCHAR(50), meaning a string of variable length, up to 50 characters.


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
  ADD middle_name VARCHAR(50);

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
We'll go over these clauses in [Intermediate Querying](https://aeryck.com/post:11)


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

In the [next tutorial](), we will learn about functions and aggregation.
