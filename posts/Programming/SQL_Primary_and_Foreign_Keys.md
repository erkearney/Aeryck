### [Basic Data Manipulation](https://aeryck.com/post:SQL: Basic Data Manipulation)
### [JOINs and Relationships](https://aeryck.com/post:SQL Intermediate Querying and JOINs)
### [PRIMARY and FOREIGN KEYs (this post)](https://aeryck.com/post:SQL PRIMARY and FOREIGN Keys)

Take a moment to imagine how this database might evolve over time. Clearly we'd
add the remaining states and presidents, but we might also want a
political_parties table. Perhaps also a vice_presidents table, and/or a senators
and representatives table? As the size of this database grows we're going to
need to introduce some constraints and rules in order to manage the complexity
and also help catch errors. We can add some by designating columns as PRIMARY or
FOREIGN KEYs.

The purpose of the PRIMARY KEY column is to uniquely identify each row, thus a
column designated as a PRIMARY KEY automatically has the following constraints
added to it:

- Each value in the column must be unique
- No value in the column can be NULL

Columns of any data type are allowed to become primary KEYs, however in practice
an **id** column of type INT that automatically increments is often chosen, as
it's easy to ensure the above constraints are followed. Other columns, such as a
*name* column should only be used as a PRIMARY KEY if you are absolutely certain
that no other row will *ever* be added to that table with the same name. For
example, designating *first_name*, *middle_name*, or *last_name* as the PRIMARY
KEY in our us_presidents table would be a horrible idea (as we've already seen
with John Adams), so we will use the *number* column instead. However using
*name* in the us_states table as the PRIMARY KEY is probably safe to do, as we
can be reasonably certain there will never be two different states with the same
name.

```sql
ALTER TABLE us_presidents
  ADD PRIMARY KEY (number);

ALTER TABLE us_states
  ADD PRIMARY KEY (name);
```

We can finally put the **relational** in relational databases by introducing the
FOREIGN KEY. A foreign key is a table column that references the PRIMARY key of
a different table. This references establishes an important relationship between
the tables. To demonstrate, let's establish a relationship between the
us_presidents and us_states tables. 

<details>
<summary>Current table columns</summary>

```sql
SELECT table_name, column_name
  FROM information_schema.columns
 WHERE table_schema = 'public'
 ORDER BY table_name;
```

<table border="1">
  <tr>
    <th align="center">table_name</th>
    <th align="center">column_name</th>
  </tr>
  <tr valign="top">
    <td align="left">us_presidents</td>
    <td align="left">number</td>
  </tr>
  <tr valign="top">
    <td align="left">us_presidents</td>
    <td align="left">political_party</td>
  </tr>
  <tr valign="top">
    <td align="left">us_presidents</td>
    <td align="left">middle_name</td>
  </tr>
  <tr valign="top">
    <td align="left">us_presidents</td>
    <td align="left">home_state</td>
  </tr>
  <tr valign="top">
    <td align="left">us_presidents</td>
    <td align="left">first_name</td>
  </tr>
  <tr valign="top">
    <td align="left">us_presidents</td>
    <td align="left">last_name</td>
  </tr>
  <tr valign="top">
    <td align="left">us_states</td>
    <td align="left">number</td>
  </tr>
  <tr valign="top">
    <td align="left">us_states</td>
    <td align="left">region</td>
  </tr>
  <tr valign="top">
    <td align="left">us_states</td>
    <td align="left">name</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

</details>

Looks at the columns of our tables, we can create a relationship between these
two tables using the **home_state** column of us_presidents and the **name**
column of us_states:

```sql
     ALTER TABLE us_presidents
       ADD CONSTRAINT fk_us_presidents_us_states
   FOREIGN KEY (home_state)
REFERENCES us_states(name);
```

> ERROR:  insert or update on table "us_presidents" violates foreign KEY constraint "state_name"
> 
> DETAIL:  KEY (home_state)=(Tennessee) is not present in table "us_states".

We got an error! Up until this point I've deliberately INSERTed any data into
us_states beyond the original 13. This allowed me to demonstrate how [LEFT,
INNER, RIGHT, and OUTER JOINs work in the previous
post](https://aeryck.com/post:Databases:%20SQL%20Intermediate%20Querying%20and%20Joins),
and now it serves as an example to a KEY feature of SQL relationships: a value
cannot exist in a FOREIGN KEY column if it does not exist in the column it is
referencing. Let's finally INSERT Tennessee (and a couple bonus states) INTO
us_states.

```sql
    INSERT INTO us_states (name, region)
    VALUES ('Vermont', 'Northeast'),
           ('Kentucky', 'South'),
           ('Tennessee', 'South'),
           ('Ohio', 'Midwest');

     ALTER TABLE us_presidents
       ADD CONSTRAINT fk_us_presidents_us_states
   FOREIGN KEY (home_state)
REFERENCES us_states(name);
```

Now that Tennessee (and all values found in the **home_state** column) exists in
us_states, we can create our FOREIGN KEY without error\*. We do this by simply
ALTERing us_presidents, then specifying we'd like **home_state** to be a FOREIGN
KEY, and finally that we want this FOREIGN KEY to REFERENCE the **name** column
in us_states.

Introducing constraints brings with them some advantages that can make managing
the database significantly easier, especially once it grows in size and access is
given to more users. For example, we can now catch *some* spelling mistakes when
INSERTing new data. Let's add poor William Henry Harrison back in:

```sql
INSERT INTO us_presidents (first_name, middle_name, last_name, political_party, home_state)
VALUES ('William', 'Henry', 'Harrison', 'Whig', 'Ohiio');
```

> ERROR:  insert or update on table "us_presidents" violates foreign key constraint "state_name"
>
> DETAIL:  Key (home_state)=(Ohiio) is not present in table "us_states".

Of course I say *some* mistakes, because a spelling mistake could still sneak
into a column that is not a FOREIGN KEY:

```sql
INSERT INTO us_presidents (first_name, middle_name, last_name, political_party, home_state)
VALUES ('William', 'Jenry', 'Harrison', 'Whig', 'Ohio');

SELECT first_name, middle_name, last_name
  FROM us_presidents
 WHERE last_name = 'Harrison';
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">Jenry</td>
    <td align="left">Harrison</td>
  </tr>
</table>
<p>(1 row)<br />
</p>

By default, this new FOREIGN KEY constraint might be a little *too*
constraining. For example, what if a state were to change its name?

```sql
UPDATE us_states
   SET name = 'New Amsterdam'
 WHERE name = 'New York';
```

> ERROR:  update or delete on table "us_states" violates foreign key constraint "fk_us_presidents_us_states" on table "us_presidents"
> 
> DETAIL:  Key (name)=(New York) is still referenced from table "us_presidents".

Herein lies the beauty in relational databases. When creating FOREIGN KEYs we
can specify CASCADEing effects (i.e., effects that will automatically propagate
changes made from one column to *all* columns that are a FOREIGN KEY referencing
it. Let's demonstrate by recreating the FOREIGN KEY CONSTRAINT and specifying
some CASCADEing affects:

```sql
     ALTER TABLE us_presidents
      DROP constraint fk_us_presidents_us_states;

     ALTER TABLE us_presidents
       ADD constraint fk_us_presidents_us_states
   FOREIGN KEY (home_state)
REFERENCES us_states(name)
        ON DELETE SET NULL
        ON UPDATE CASCADE;

    UPDATE us_states
       SET name = 'New Amsterdam'
     WHERE name = 'New York';

    SELECT name
      FROM us_states
     ORDER BY number;
```

<table border="1">
  <tr>
    <th align="center">name</th>
  </tr>
  <tr valign="top">
    <td align="left">Delaware</td>
  </tr>
  <tr valign="top">
    <td align="left">Pennsylvania</td>
  </tr>
  <tr valign="top">
    <td align="left">New Jersey</td>
  </tr>
  <tr valign="top">
    <td align="left">Georgia</td>
  </tr>
  <tr valign="top">
    <td align="left">Connecticut</td>
  </tr>
  <tr valign="top">
    <td align="left">Massachusetts</td>
  </tr>
  <tr valign="top">
    <td align="left">Maryland</td>
  </tr>
  <tr valign="top">
    <td align="left">South Carolina</td>
  </tr>
  <tr valign="top">
    <td align="left">New Hampshire</td>
  </tr>
  <tr valign="top">
    <td align="left">Virginia</td>
  </tr>
  <tr valign="top">
    <td align="left">New Amsterdam</td>
  </tr>
  <tr valign="top">
    <td align="left">North Carolina</td>
  </tr>
  <tr valign="top">
    <td align="left">Rhode Island</td>
  </tr>
  <tr valign="top">
    <td align="left">Vermont</td>
  </tr>
  <tr valign="top">
    <td align="left">Kentucky</td>
  </tr>
  <tr valign="top">
    <td align="left">Tennessee</td>
  </tr>
  <tr valign="top">
    <td align="left">Ohio</td>
  </tr>
</table>
<p>(17 rows)<br />
</p>

We can see that now we were able to successfully change the name of 'New York'
to 'New Amsterdam' in us_states, but now let's look at us_presidents!

```sql
SELECT first_name, middle_name, last_name, home_state
  FROM us_presidents
 ORDER BY number;
```

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
    <td align="left">Tennessee</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New Amsterdam</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">Henreigh</td>
    <td align="left">Harrison</td>
    <td align="left">Ohio</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

Notice how Martin Van Buren's home state was also changed to New Amsterdam! This
is because we specified that when we UPDATE SQL should CASCADE the changes.
We've also specified that when we DELETE we want the impacted rows to be SET to
NULL:

```sql
DELETE FROM us_states
 WHERE name = 'Ohio';

SELECT first_name, middle_name, last_name, home_state
  FROM us_presidents
 ORDER BY number;
```

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
    <td align="left">Tennessee</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New Amsterdam</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">Henreigh</td>
    <td align="left">Harrison</td>
    <td align="left">&nbsp; </td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

Here you can see that because we've DELETEd William "Henreigh" Harrison's state
of Ohio from us_states, his home_state was set to NULL. In addition to CASCADE
and SET NULL, there is also NO ACTION, which simply prevents altering or
removing referenced values (this is the default setting when creating FOREIGN
KEYs, which is why we got the original error) and SET DEFAULT, which will set
impacted values to a value specified when CREATEing the table instead of NULL.

We've now learned how to create and use PRIMARY and FOREIGN KEYs. As I mentioned
before, many tutorials will introduce these topics straight away, but it's my
view that doing this obscures much of their value and importance. My hope is
that by waiting this long to broach this topic, it's more clear now why PRIMARY
and FOREIGN KEYs are not only useful, but necessary in large relational
databases.

In the [next post]() we're going to delve into ACID properties, and how to
backup and protect our database.
