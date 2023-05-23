### [Basic Data Manipulation](https://aeryck.com/post:SQL: Basic Data Manipulation)
### [Joins and Relationships (this post)](https://aeryck.com/post:SQL Intermediate Querying and Joins)
### [Primary and Foreign Keys](https://aeryck.com/post:SQL Primary and Foreign Keys)
### [Transactions and ACID properties](https://aeryck.com/post:SQL%20Transactions%20and%20ACID%20properties)
### [Views Procedures and Functions](https://aeryck.com/post:SQL Views Procedures and Functions)

In the [last post](https://aeryck.com/post:SQL Basic Data Manipulation) we created a table for some early
U.S. Presidents and states, and learned we can view our tables with:

```sql
SELECT first_name, middle_name, last_name, home_state
  FROM us_presidents;

SELECT name, region
  FROM us_states;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">home_state</th>
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
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
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
    <td align="left">Tennessee</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
  </tr>
</table>
<p>(8 rows)<br />
</p>

<table border="1">
  <tr>
    <th align="center">name</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">Delaware</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">Pennsylvania</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">New Jersey</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Georgia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">Connecticut</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Maryland</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">South Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">New Hampshire</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">North Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">Rhode Island</td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(13 rows)<br />
</p>

As you've likely gathered from this posts' title, we're going to be JOINing
these tables together. We're going to be making the use of aliases by using the
AS keyword to keep the statement length under control. We'll also add the ORDER
BY clause so that we can sort the presidents by the order of which they were
elected. Notice how just like with the WHERE clause, we can ORDER BY a column
even if we aren't SELECTing that column.

```sql
SELECT p.first_name, p.middle_name, p.last_name, p.home_state, s.region
  FROM us_presidents AS p
       JOIN us_states AS s ON p.home_state = s.name
 ORDER BY p.number;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">home_state</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van </td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(8 rows)<br />
</p>

Now we have a single table comprised of columns from both the us_presidents and
the us_states tables. 

When calling JOIN, you must specify a column from each table to be JOINed ONto.
In the above example, we JOINed the home_state column from us_presidents ONto
the name column of us_states. This caused SQL to stitch together rows where
those columns match. Take a look at George Washington's row in us_presidents,
and Virginia's row in us_states. Since the value of **home_state** matches the
value of **name**, the data in these rows across these tables were combined into
one. 

When we use the JOIN keyword by itself, we're technically performing an *inner*
join, meaning all rows that do not have a 'match' are automatically filtered
out.

You've probably noticed that not every state from us_states made it into this
new table, in fact, only three states, Virginia, Massachusetts, and New York are
present. You may have also noticed that not every president made it to this list
as well... Andrew Jackson, who hails from Tennessee is missing, the reason being
is Tennessee is not yet in the us_states table. 

We can keep the unmatched rows, and populate the missing columns with NULL by
specifying we'd like a FULL JOIN:

```sql
SELECT p.first_name, p.middle_name, p.last_name, p.home_state, s.region
  FROM us_presidents AS p
  FULL JOIN us_states AS s ON p.home_state = s.name;
 ORDER BY p.number;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">home_state</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">Tennessee</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(18 rows)<br />
</p>

Using FULL joins are pretty rare (after all, it's not clear what the above table
even means\*), more commonly you will see the LEFT JOIN and the RIGHT JOIN, which
I think of as 'partial FULL JOINs'. A LEFT JOIN will keep the rows from the
first specified (i.e., 'left') table, even if it does not match the second
('right') table on the JOIN column. Vice versa for RIGHT JOIN:

```sql
SELECT p.first_name, p.middle_name, p.last_name, p.home_state, s.region
  FROM us_presidents as p
       LEFT JOIN us_states as s ON p.home_state = s.name
 ORDER BY p.number;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">home_state</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">Tennessee</td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(8 rows)<br />
</p>

Notice here in the LEFT JOIN that Andrew Jackson is present, with the region
column simply being left blank for him. Because this was a LEFT JOIN, rows from
the RIGHT table that do not match any rows on the LEFT table on the join column
are absent.

Take a second to consider what the output of a RIGHT JOIN will be:

```sql
SELECT p.first_name, p.middle_name, p.last_name, p.home_state, s.region
  FROM us_presidents as p
       RIGHT JOIN us_states as s ON p.home_state = s.name
 ORDER BY p.number;
```

<details>
<summary>Results of RIGHT JOIN</summary>
<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">home_state</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(17 rows)<br />
</p>

The results are the same as the FULL JOIN above, except Andrew Jackson is
missing, as that was the only row from the LEFT table that did not have a match
ON the JOIN column.
</details>

Wrapping your head around the different types of JOINs can be a bit tricky, this
visualization ([credit: w3schools](https://www.w3schools.com/sql/sql_join.asp))
can help make sense of it.
![Figure 1: Different types of JOINs
visualized](/static/images/databases/sql/joins_and_relationships/1.png "Figure
1: Different types of JOINs visualized")

### Aggregate Functions and GROUP BY
We'll wrap up this post by fleshing out our querying knowledge, starting with
the aggregate function COUNT(), which simply returns the number of matching
rows:

```sql
SELECT COUNT(home_state)
  FROM us_presidents
 WHERE home_state = 'Virginia';
```

<table border="1">
  <tr>
    <th align="center">count</th>
  </tr>
  <tr valign="top">
    <td align="right">4</td>
  </tr>
</table>
<p>(1 row)<br />
</p>

This query simply COUNTed the number of rows where home_state is 'Virginia'.
Using aggregate functions introduces some limitations into how we write our
queries. For example, this query fails:

```sql
SELECT last_name, COUNT(home_state)
  FROM us_presidents
 WHERE home_state = 'Virginia';
```

> ERROR:  column "us_presidents.last_name" must appear in the GROUP BY clause or be used in an aggregate function 

> LINE 1: SELECT last_name, COUNT(home_state)

We can intuitively understand this error by looking at the output of the
previous query. By adding the COUNT() aggregate function, we've 'smashed' all
rows WHERE home_state = 'Virginia' into one. We can't SELECT a last_name from
this one row because there's no way for SQL to determine which last_name
('Washington', 'Jefferson', 'Madison', or 'Monroe') we could be referring to!

The other aggregate functions are SUM() and AVG(). They're not particularly
applicable to this database, but are incredibly useful in others.

So if we want more columns we'll need to either use more aggregate functions or
the GROUP BY clause. Here is a query that will output the number of presidents
from each state:

```sql
SELECT home_state, COUNT(home_state)
  FROM us_presidents
 GROUP BY home_state
 ORDER BY count DESC;
```

<table border="1">
  <tr>
    <th align="center">home_state</th>
    <th align="center">count</th>
  </tr>
  <tr valign="top">
    <td align="left">Virginia</td>
    <td align="right">4</td>
  </tr>
  <tr valign="top">
    <td align="left">Massachusetts</td>
    <td align="right">2</td>
  </tr>
  <tr valign="top">
    <td align="left">New York</td>
    <td align="right">1</td>
  </tr>
  <tr valign="top">
    <td align="left">Tennessee</td>
    <td align="right">1</td>
  </tr>
</table>
<p>(4 rows)<br />
</p>

And finally, we of course can combine JOINs, aggregate functions, and the GROUP
BY clause. Let's come up with a query that will tell use home many presidents
came from each *region* of the United States:

```sql
SELECT s.region, COUNT(s.region)
  FROM us_presidents AS p
       JOIN us_states As s ON p.home_state = s.name
 GROUP BY s.region;
```

<table border="1">
  <tr>
    <th align="center">region</th>
    <th align="center">count</th>
  </tr>
  <tr valign="top">
    <td align="left">South</td>
    <td align="right">4</td>
  </tr>
  <tr valign="top">
    <td align="left">Northeast</td>
    <td align="right">3</td>
  </tr>
</table>
<p>(2 rows)<br />
</p>

You would be forgiven if you think this is a strange query. After all, why are
we JOINing us_presidents ONto us_states, if we're only SELECTing columns from
us_states? What must be realized is that when executing this query, the JOIN
executes first, meaning we're recreating something like the table created by our
very first JOIN, all the way back at the start of this post. Afterwards, we're
using the COUNT() aggregate function and GROUP BY clause to smash the rows whose
regions are equal to each other together, leaving us with just two rows
containing 'South' and 'Northeast', along with the respective COUNTs.

In the [next post]() I'm going to introduce Primary and Foreign keys, a topic
I've been carefully avoiding up until now, despite many tutorials leading with
it.


\* We can actually make this table a little less confusing by re-thinking our
query. The home_state column is blank for states that haven't yet sent someone
to the White House, but we could instead SELECT the name column from the states
table:

<details>
<summary>Using name from states instead of home_state from
us_presidents</summary>

```sql
SELECT p.first_name, p.middle_name, p.last_name, s.name, s.region
  FROM us_presidents as p
  FULL JOIN us_states as s ON p.home_state = s.name
 ORDER BY p.number;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">name</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">New Hampshire</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Maryland</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Connecticut</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Georgia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">New Jersey</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">North Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Rhode Island</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Delaware</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Pennsylvania</td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(18 rows)<br />
</p>

</details>

That's somewhat better, at least we can now see the names of the states with no
matching president. However, it isn't great that we now have columns called
*first_name*, *middle_name*, *last_name*, and... *name*..., the last of which
referring to a completely different entity than the first three. We can again
simply use an ALIAS to resolve this:

<details>
<summary>Using an ALIAS to resolve confusion</summary>

```sql
SELECT p.first_name, p.middle_name, p.last_name, s.name AS state, s.region
  FROM us_presidents as p
       FULL JOIN us_states as s ON p.home_state = s.name
 ORDER BY p.number;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">state</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
    <td align="left">&nbsp; </td>
    <td align="left">Washington</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jefferson</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Virginia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">New Hampshire</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Maryland</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Connecticut</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Georgia</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">New Jersey</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">North Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Rhode Island</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Delaware</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">South Carolina</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">&nbsp; </td>
    <td align="left">Pennsylvania</td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(18 rows)<br />
</p>

</details>
