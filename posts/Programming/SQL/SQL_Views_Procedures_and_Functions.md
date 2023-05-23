In this post, we're going to learn how to simplify our queries and save time
writing them.

### [Basic Data Manipulation](https://aeryck.com/post:SQL Basic Data Manipulation)
### [Joins and Relationships](https://aeryck.com/post:SQL Intermediate Querying and Joins)
### [Primary and Foreign Keys](https://aeryck.com/post:SQL Primary and Foreign Keys)
### [Transactions and ACID properties](https://aeryck.com/post:SQL%20Transactions%20and%20ACID%20properties)
### [Views Procedures and Functions (this post)](https://aeryck.com/post:SQL Views Procedures and Functions)

## Views
Throughout this tutorial, we've written the following query many, many times:

```sql
SELECT first_name, middle_name, last_name, home_state
  FROM us_presidents
 ORDER BY number;
```

Even a simple query such as this is rather verbose, not to mention a big pain to
type out. The good news is we can save ourselves a lot of time in the future by
creating a VIEW:

```sql
CREATE VIEW sorted_presidents AS
SELECT first_name, middle_name, last_name, home_state
  FROM us_presidents
 ORDER BY number;
```

And now we can get the same effect by simply running:

```sql
SELECT * FROM sorted_presidents;
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
    <td align="left">New York</td>
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

Here, once we've created our VIEW, we SELECTed everything (using the wildcard *
operator) from that VIEW. A VIEW can be thought of as a 'saved query'. Note that
it is the *query* that is being saved here, not the results. For example
let's rectify the silliness we've created with William 'Henreigh' Harrison while
experimenting earlier:


```sql
BEGIN TRANSACTION;
  INSERT INTO us_states (name, region)
  VALUES ('Ohio', 'Midwest');

  UPDATE us_presidents
     SET middle_name = 'Henry',
         home_state = 'Ohio'
   WHERE first_name = 'William'
     AND last_name = 'Harrison';

  SELECT * FROM sorted_presidents;
COMMIT;
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
    <td align="left">New York</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">Henry</td>
    <td align="left">Harrison</td>
    <td align="left">Ohio</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

There are two important things to note here: First is that we nested our UPDATE
within a TRANSACTION, and that we were able to first SELECT FROM
sorted_presidents to ensure that the UPDATEs did what we were aiming to do, and
second is that the results SELECTing \* (everything) FROM sorted_presidents did
indeed change to reflect the UPDATEs we made.

###### In the [very first post](https://aeryck.com/post:SQL%20Basic%20Data%20Manipulation) in this tutorial I made a brief note on using the wildcard operator.  I argued even back there that there's nothing wrong with using the wildcard operator if you wish. Using \* becomes even more compelling when working with VIEWS, since by their very nature we're already limiting the columns present. Even still, it's generally considered a bad practice to do so, and I'll show you an example why in this post!

We aren't limited to simple SELECT queries when creating VIEWs. For example:

```sql
CREATE VIEW southern_presidents AS
SELECT p.first_name, p.middle_name, p.last_name, p.home_state
  FROM us_presidents AS p
       JOIN us_states AS s on p.home_state = s.name
 WHERE s.region = 'South'
 ORDER BY p.number;

SELECT * FROM southern_presidents;
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
    <td align="left">Andrew</td>
    <td align="left">&nbsp; </td>
    <td align="left">Jackson</td>
    <td align="left">Tennessee</td>
  </tr>
</table>
<p>(5 rows)<br />
</p>

Brownie points if you thought "Hang on, didn't we **just** CREATE a VIEW to save
us from having to type SELECT first_name, middle_name, last_name, home_state
...?" Because we can absolutely make use of old VIEWs when creating new VIEWs!

```sql
CREATE VIEW northeastern_presidents AS
SELECT * FROM sorted_presidents AS p
       JOIN us_states AS s on p.home_state = s.name
 WHERE s.region = 'Northeast';

SELECT * FROM northeastern_presidents;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
    <th align="center">middle_name</th>
    <th align="center">last_name</th>
    <th align="center">home_state</th>
    <th align="center">number</th>
    <th align="center">name</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="right">6</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Massachusetts</td>
    <td align="right">6</td>
    <td align="left">Massachusetts</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
    <td align="left">Van</td>
    <td align="left">Buren</td>
    <td align="left">New York</td>
    <td align="right">11</td>
    <td align="left">New York</td>
    <td align="left">Northeast</td>
  </tr>
</table>
<p>(3 rows)<br />
</p>

However as you can see there is some strange behavior here. We have the
**number**, **name**, and **region** columns from us_states even though we never
SELECTed them...

... or did we?

Well actually we *did* SELECT all these columns. SQL follows an order of
operations (also known as the logical query processing phase)\*. So even though we
wrote the query as SELECT * FROM sorted_presidents, then JOIN that ONTO
us_states, it was processed as JOIN sorted_presidents ONTO us_states, *then*
SELECT * FROM the result. This is one of the potential pitfalls to watch out for
when using the wildcard operator, and why it's generally considered a best
practice to avoid it.

\* For reference, the SQL order of operations is:


1. FROM (JOINs are part of the FROM family)
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY


## PROCEDUREs & FUNCTIONs
The differences between database management systems (e.g., MySQL, PostgreSQL,
etc.) are more significant when writing PROCEDUREs and FUNCTIONs. The following
may not be strictly true for all database management systems, however the
principles explored within are widely considered best practices no matter which
system you're using. 

Earlier we learned we can think of VIEWs as stored SELECT queries. PROCEDUREs
and FUNCTIONs are similar, except instead of storing SELECT queries, we're
organizing and storing multiple statements into a single call. PROCEDUREs and
FUNCTIONs are very similar to each other, however there are two key differences:
1. PROCEDUREs can manage TRANSACTIONs, while FUNCTIONs cannot.
2. FUNCTIONs must always RETURN something, PROCEDUREs never return anything.

If your goal is to fetch information from the database, you should write a
FUNCTION. If you need to somehow change the database, you should write a
PROCEDURE.

Earlier we experienced some minor headaches trying to INSERT presidents when
their home_state didn't already exist in the us_states table. We can bundle some
statements together to automatically INSERT a president's home state into
us_states if it doesn't already exist. Since this will be modifying the
database, we'll write it as a PROCEDURE:

```sql
  CREATE PROCEDURE add_president (first_name VARCHAR, last_name VARCHAR,
                                  political_party VARCHAR,
                                  home_state VARCHAR)
LANGUAGE plpgsql
      AS $$
   BEGIN
          INSERT INTO us_states (name)
          VALUES (home_state)
              ON CONFLICT (name)
              DO NOTHING;

          INSERT INTO us_presidents (first_name, last_name,
                                     political_party,
                                     home_state)
          VALUES (first_name, last_name,
                  home_state);
          COMMIT;
      END;
       $$;

CALL add_president('John', 'Tyler', 'Independent', 'Virginia');
CALL add_president('Abraham', 'Lincoln', 'Republican', 'Illinois');

SELECT * FROM sorted_presidents;
SELECT name AS State_name, region FROM us_states ORDER BY number;
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
    <td align="left">New York</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
    <td align="left">Henry</td>
    <td align="left">Harrison</td>
    <td align="left">Ohio</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
    <td align="left">&nbsp; </td>
    <td align="left">Tyler</td>
    <td align="left">Virginia</td>
  </tr>
  <tr valign="top">
    <td align="left">Abraham</td>
    <td align="left">&nbsp; </td>
    <td align="left">Lincoln</td>
    <td align="left">Illinois</td>
  </tr>
</table>
<p>(11 rows)<br />
</p>

<table border="1">
  <tr>
    <th align="center">state_name</th>
    <th align="center">region</th>
  </tr>
  <tr valign="top">
    <td align="left">Delaware</td>
    <td align="left">Northeast</td>
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
  <tr valign="top">
    <td align="left">Vermont</td>
    <td align="left">Northeast</td>
  </tr>
  <tr valign="top">
    <td align="left">Kentucky</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">Tennessee</td>
    <td align="left">South</td>
  </tr>
  <tr valign="top">
    <td align="left">Ohio</td>
    <td align="left">Midwest</td>
  </tr>
  <tr valign="top">
    <td align="left">Illinois</td>
    <td align="left">&nbsp; </td>
  </tr>
</table>
<p>(18 rows)<br />
</p>

###### Yes, Abraham Lincoln was *born* in Kentcuky, but he started his political career in Illinois

Okay there's a bit going on in our PROCEDURE. We start by giving the PROCEDURE a
name and defining the arguments we'd like it to take (first_name, last_name,
home_state). Afterwards, we're setting the language to plpgsql, which stands for
Procedural Language/PostgreSQL, this is simply a language that provides
additional features that are lacking in base SQL. The PROCEDURE body is enclosed
in 'dollar quotes' ($$)\*\* and BEGIN and END; calls. We've seen most of what
remains before, however we've added an ON CONFLICT clause and specified that
should there be a CONFLICT on a states' **name** we shall DO NOTHING. This
prevents duplicate entries from being added if that state already exists in
us_states (e.g., when CALLed the PROCEDURE with 'John', 'Tyler', Virginia').
When our PROCEDURE is CALLed and a home_state is supplied that is not already in
us_states, it's added there first to prevent a foreign key conflict (as was done
for Illinois when we CALLed with 'Abraham', 'Lincoln', 'Illinois'). Finally, we
end with the COMMIT statement. Notice we did not need to include BEGIN
TRANSACTION; because a PROCEDURE is already by definition a TRANSACTION.

Note that this PROCEDURE left the **region** of Illinois blank. This is of
course because we never specified the region when INSERTing. In times such as
these, we have a tough decision to make. We can:

- Leave the **region** of states added with this PROCEDURE blank, and hope that
  someone comes and UPDATEs them appropriately later.
- Force the user of the database to specify the **region** of every new
  president's **home_state**, even when that state already exists in us_states.
- Do away with the PROCEDURE entirely and rely solely on INSERT statements
  instead.

All have their pros and cons, and the 'best' option will depend entirely on your
specific needs and the role of your database.

Now that we've taken a crack at PROCEDUREs, let's write a FUNCTION. We could
write one that will count the number of presidents from different regions of
the United States:

```sql
  CREATE FUNCTION count_presidents_by_region (us_region VARCHAR)
 RETURNS INT
LANGUAGE plpgsql
      AS $$
 DECLARE
         result INT;
   BEGIN
         SELECT COUNT(*) INTO result
           FROM us_presidents AS p
                 JOIN us_states AS s on p.home_state = s.name
                WHERE s.region = us_region;
         RETURN result;
     END;
      $$;

SELECT count_presidents_by_region ('South') AS num_southerns;
```

<table border="1">
  <tr>
    <th align="center">num_southerns</th>
  </tr>
  <tr valign="top">
    <td align="right">6</td>
  </tr>
</table>
<p>(1 row)<br />
</p>

\*\* SQL expects the body of PROCEDUREs and FUNCTIONs to be a single string,
which will then be interpreted and executed by the database engine. It's
possible to enclose the body in regular quotes (e.g., 'BEGIN RETURN i + 1;'),
however you'll run into issues if your function body contains strings within
itself. The dollar quotes ($$) automatically converts everything enclosed within
them to a string, including strings within the string. Demonstrating how this is
useful is beyond the scope of this tutorial, but now you know what the meaning
of this symbol!

In conclusion, we can encapsulate multiple SQL statements into one using VIEWs,
PROCEDUREs, and FUNCTIONs. We use VIEWs to store the result of a SELECT query,
FUNCTIONs to store statements that fetch information from the database, and
PROCEDUREs to store statements that will somehow modify the database.


And with that we've finished this SQL tutorial! The [next post]() will feature
some exercises to test your understanding of what we've learned, and your
ability to further develop your skills on your own.
