With the introduction of FOREIGN KEYs, we've caught a small glimpse of measures
we can take to protect our database from faulty information, but what if despite
our best efforts something terrible happens to our database, such as false data
being INSERTed, or even worse, a bunch of real data being DELETEd? One important
measure we can take to protect ours database is to ensure that our work be
implemented as TRANSACTIONs. 

### [Basic Data Manipulation](https://aeryck.com/post:SQL Basic Data Manipulation)
### [Joins and Relationships](https://aeryck.com/post:SQL Intermediate Querying and Joins)
### [Primary and Foreign Keys](https://aeryck.com/post:SQL Primary and Foreign Keys)
### [Transactions and ACID properties (this post)](https://aeryck.com/post:SQL Transactions and ACID Properties)
### [Views Procedures and Functions](https://aeryck.com/post:SQL Views Procedures and Functions)


When changes are made as TRANSACTIONs, it becomes
easy to un/re-do them. SQL TRANSACTIONs follow **ACID** properties:

+ **A**tomicity: Transactions are indivisible units. They either succeed or
  fail completely, no in-between.
+ **C**onsistency: TRANSACTIONs leave the database in a valid\* state.
+ **I**solation: TRANSACTIONs leave the database in the same state
  regardless of whether they are executed sequentially or in parallel (the value
  of this property becomes relevant when you're working with a huge database
  exposed to a large number of users).
+ **D**urability: Once a TRANSACTION is COMMITed, the changes will remain
  even if the entire system fails.

Let's begin with a basic example of how TRANSACTIONs can be useful, imagine the
following statements were run (either through accident or malice)

```sql
BEGIN TRANSACTION;
  UPDATE us_presidents
     SET home_state = 'Massachusetts'
   WHERE home_state = 'Virginia';

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
    <td align="left">Massachusetts</td>
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
    <td align="left">Massachusetts</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Madison</td>
    <td align="left">Massachusetts</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
    <td align="left">&nbsp; </td>
    <td align="left">Monroe</td>
    <td align="left">Massachusetts</td>
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

By calling the BEGIN TRANSACTION; statement, all subsequent work will now be
done within this TRANSACTION, until we either cancel or COMMIT.


We have a problem now, the **home_state** of every president from Virginia has
been changed to Massachusetts. We can't just fix the problem the same way it was
introduced either:

```sql
UPDATE us_presidents
   SET home_state = 'Virginia'
 WHERE home_state = 'Massachusetts';

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
    <td align="left">John</td>
    <td align="left">Quincy</td>
    <td align="left">Adams</td>
    <td align="left">Virginia</td>
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

While we've correctly set the **home_state** of Washington, Jefferson, Madison,
and Monroe back to Virginia, we've also *incorrectly* done the same for both
John Adams and John Quincy Adams! If we were not working within a TRANSACTION as
before, we'd have to choice but to manually UPDATE the afflicted rows to correct
them. However thankfully we can simply run:

```sql
ROLLBACK;

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

By invoking the ROLLBACK command, we've successfully undone everything since the
BEGIN TRANSACTION statement. Note that calling ROLLBACK also ends the current
TRANSACTION.

If we are happy with the work done within a TRANSACTION and wish to keep it, we
need to use the COMMIT statement instead:

```sql
BEGIN TRANSACTION;
  UPDATE us_states
     SET name = 'New York'
   WHERE name = 'New Amsterdam';
COMMIT;
```

Now that we've COMMITed our changes, the TRANSACTION is complete, and we lose
the chance to ROLLBACK the work. This is in adherence to the **D**urability
principle of **ACID**.

Speaking of **ACID** principles, let's more closely examine **A**tomicity
principle, which asserts that a TRANSACTION must either completely succeed or
completely fail. That means that if there is an error anywhere within a
TRANSACTION, **all** statements within that TRANSACTION, even those that
executed without error will automatically be rolled back, even if the
transaction ends with the COMMIT statement:

```sql
BEGIN TRANSACTION;
  UPDATE us_presidents
     SET first_name = 'Johnathan'
   WHERE first_name = 'John';

  UPDATE us_presidents
     SET home_state = 'Ohiio'
   WHERE last_name = 'Harrison';
COMMIT;
```

> ERROR:  insert or update on table "us_presidents" violates foreign key constraint "fk_us_presidents_us_states"
> 
> DETAIL:  Key (home_state)=(Ohiio) is not present in table "us_states".

Here we tried to rename both John Adams to *Johnathan* Adams, we also tried to set
William "Henreigh" Harrison's home state to "Ohiio" again which, as demonstrated
in the [previous
post](https://aeryck.com/post:SQL%20Primary%20and%20Foreign%20Keys) fails due to
the FOREIGN KEY CONSTRAINT we've placed on **home_state**.

```sql
SELECT first_name
  FROM us_presidents
 ORDER BY number;
```

<table border="1">
  <tr>
    <th align="center">first_name</th>
  </tr>
  <tr valign="top">
    <td align="left">George</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
  </tr>
  <tr valign="top">
    <td align="left">Thomas</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
  </tr>
  <tr valign="top">
    <td align="left">James</td>
  </tr>
  <tr valign="top">
    <td align="left">John</td>
  </tr>
  <tr valign="top">
    <td align="left">Andrew</td>
  </tr>
  <tr valign="top">
    <td align="left">Martin</td>
  </tr>
  <tr valign="top">
    <td align="left">William</td>
  </tr>
</table>
<p>(9 rows)<br />
</p>

Because there was an error in the TRANSACTION, the "Johnathan" UPDATEs were
rolled back.

In the [next post]() we'll cover VIEWs, PRODCEDUREs, and FUNCTIONs.


\* The database designer can determine what is and is not a valid state. An
example of when this could come in handy is if you manage the backend database
for a bank. Imagine you're implementing logic to allow your users to perform
internal transfers; you could add a constraint dictating that in order for this
transaction to be valid the total amount of money between the two accounts must
be the same before and after the transaction. This would ensure that if money is
subtracted from one account, it's added to another (and vice versa). If, after
performing the TRANSACTION, the sum of money between the accounts is different
than it was before the constraint would be violated, and a ROLLBACK would
automatically be executed.
