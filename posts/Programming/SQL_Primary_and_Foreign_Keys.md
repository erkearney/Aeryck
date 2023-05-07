### [Basic Data Manipulation](https://aeryck.com/post:SQL: Basic Data Manipulation)
### [Joins and Relationships](https://aeryck.com/post:SQL Intermediate Querying and Joins)
### [Primary and Foreign Keys (this post)](https://aeryck.com/post:SQL Primary and Foreign Keys)

### Primary and Foreign Keys
Take a moment to imagine how this database might evolve over time. Clearly we'd
add the remaining states and presidents, but we might also want a
political_parties table. Perhaps also a vice_presidents table, and/or a senators
and representatives table? As the size of this database grows we're going to
need to introduce some constraints and rules in order to manage the complexity
and also help catch errors. We can add some by designating columns as Primary or
Foreign keys.

The purpose of the Primary Key column is to uniquely identify each row, thus a
column designated as a Primary Key automatically has the following constraints
added to it:

- Each value in the column must be unique
- No value in the column can be NULL

Columns of any data type are allowed to become primary keys, however in practice
an **id** column of type INT that automatically increments is often chosen, as
it's easy to ensure the above constraints are followed. Other columns, such as a
*name* column should only be used as a Primary Key if you are absolutely certain
that no other row will *ever* be added to that table with the same name. For
example, designating *first_name*, *middle_name*, or *last_name* as the Primary
Key in our us_presidents table would be a horrible idea (as we've already seen
with John Adams), so we will use the *number* column instead. However using
*name* in the us_states table as the Primary Key is probably safe to do, as we
can be reasonably certain there will never be two different states with the same
name.

```sql
ALTER TABLE us_presidents
  ADD PRIMARY KEY (number);

ALTER TABLE us_states
  ADD PRIMARY KEY (name);
```

A Foreign Key is a column in one table that references the primary key of
another table. 
