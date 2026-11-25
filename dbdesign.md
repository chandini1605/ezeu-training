Database & SQLAlchemy – Important Notes (Sessions 16–19)
Session 16 – Database Schema Design
1. What is a database schema?
A schema defines the structure of a database, including:
- Tables
- Columns
- Data types
- Primary keys
- Foreign keys
- Relationships
2. Our project tables
Tools table
Column	Data type	Constraint
id	INTEGER	Primary Key
name	VARCHAR	NOT NULL
category	VARCHAR	NOT NULL
available	BOOLEAN	NOT NULL


Checkouts table
Column	Data type	Constraint
id	INTEGER	Primary Key
tool_id	INTEGER	Foreign Key
borrower_name	VARCHAR	NOT NULL
borrowed_at	TIMESTAMP	NOT NULL
returned_at	TIMESTAMP	NULL allowed


3. Primary Key (PK)
- Uniquely identifies each row in a table.
- Cannot contain duplicate or NULL values.
- Example: tools.id.
4. Foreign Key (FK)
- Connects two tables.
- References a primary key or unique key in another table.
- Example: checkouts.tool_id references tools.id.
5. One-to-Many Relationship
- One tool can have multiple checkout records over time.
- Each checkout record belongs to one tool.
Example: Laptop can be borrowed by Ravi, returned, and later borrowed by Priya. Both checkout records refer to the same tool ID.
6. Referential Integrity
Ensures that relationships between tables remain valid.

Example: We cannot create a checkout record for a tool ID that doesn't exist in the tools table.
7. Why is returned_at nullable?
Because a tool might still be borrowed.
- NULL → Not returned yet.
- Timestamp value → Returned.
Session 17 – PostgreSQL
1. What is PostgreSQL?
PostgreSQL is an open-source Relational Database Management System (RDBMS).

It stores structured data in tables and supports SQL queries.
2. Important terminology
Term	Meaning
PostgreSQL	Relational database management system
Database	Container for related data
Table	Stores data in rows and columns
PostgreSQL Server	Engine that manages databases
psql	Command-line tool to interact with PostgreSQL
pgAdmin	Graphical tool to manage PostgreSQL
Port 5432	Default PostgreSQL port
SQL	Language used to communicate with relational databases


3. PostgreSQL vs SQL
- PostgreSQL is the database system.
- SQL is the language used to communicate with it.
4. PostgreSQL vs pgAdmin vs psql
- PostgreSQL: Stores and manages data.
- pgAdmin: Allows database management through a graphical interface.
- psql: Allows database management through commands in a terminal.
5. Application architecture
User
  |
  v
FastAPI
  |
  v
Python Business Logic
  |
  v
SQLAlchemy ORM
  |
  v
PostgreSQL Database

6. Important installation details
- Default port: 5432.
- Default administrative role: postgres.
- psql --version checks whether the PostgreSQL command-line client is available.
- It does not confirm whether the PostgreSQL server is running.
Session 18 – SQL Important Commands
SQL stands for Structured Query Language.
Command	Purpose
SELECT	Retrieve records
INSERT	Add records
UPDATE	Modify records
DELETE	Delete records
WHERE	Filter records
ORDER BY	Sort records
GROUP BY	Group records
JOIN	Combine related tables
LIMIT	Restrict returned rows
COUNT()	Count records


Important examples
Retrieve all tools
SELECT * FROM tools;

Retrieve available tools
SELECT * FROM tools
WHERE available = TRUE;

Insert a tool
INSERT INTO tools (id, name, category, available)
VALUES (4, 'Keyboard', 'Electronics', TRUE);

Update availability
UPDATE tools
SET available = FALSE
WHERE id = 1;

Delete a tool
DELETE FROM tools
WHERE id = 4;

Sort records
SELECT * FROM tools
ORDER BY name ASC;

Count available tools
SELECT COUNT(*)
FROM tools
WHERE available = TRUE;

Join tools and checkouts
SELECT tools.name, checkouts.borrower_name
FROM tools
INNER JOIN checkouts
ON tools.id = checkouts.tool_id;

1. What is a transaction?
A transaction is a group of database operations treated as one logical unit.
2. Important transaction commands
Command	Purpose
COMMIT	Permanently commits the transaction
ROLLBACK	Cancels uncommitted changes


Important: Always use WHERE carefully with UPDATE and DELETE. Without it, all rows may be affected.
Session 19 – SQLAlchemy ORM
1. What is ORM?
ORM stands for Object Relational Mapping.

It maps:
- Python classes → Database tables
- Python objects → Database rows
- Class attributes → Database columns
2. What is SQLAlchemy?
SQLAlchemy is a Python library used to interact with relational databases.

It provides:
- SQLAlchemy Core
- SQLAlchemy ORM
We use SQLAlchemy ORM in our project.
3. Why do we use ORM?
Without ORM, we manually write SQL queries.
INSERT INTO tools (id, name, category, available)
VALUES (4, 'Keyboard', 'Electronics', TRUE);

With ORM, we work with Python objects.
new_tool = Tool(    id=4,    name="Keyboard",    category="Electronics",    available=True)db.add(new_tool)db.commit()


SQLAlchemy generates the required SQL behind the scenes.
4. What is a Model?
A model is a Python class representing a database table.

Example:
class Tool(Base):    __tablename__ = "tools"    id = mapped_column(primary_key=True)    name = mapped_column()    category = mapped_column()    available = mapped_column()


Important components:
Component	Purpose
Base	Base class for registering ORM models
Tool	Python model class
__tablename__	Specifies database table name
mapped_column()	Defines a database column
primary_key=True	Identifies the primary key


5. Pydantic vs SQLAlchemy
This is an important interview question.
Pydantic	SQLAlchemy
Validates incoming data	Maps Python objects to database tables
Defines request/response schemas	Defines database models
Checks data types and required fields	Handles database operations
Does not automatically store data	Communicates with the database


Remember:
- Pydantic = Data validation.
- SQLAlchemy = Database interaction.
6. What is a SQLAlchemy Session?
A Session manages interactions between Python objects and the database.

It manages:
- Database operations
- ORM objects
- Transactions
7. Important Session methods
Method	Purpose
db.add()	Adds an object to the session
db.get()	Retrieves an object using its primary key
db.commit()	Commits the transaction
db.rollback()	Rolls back uncommitted changes
db.flush()	Sends pending SQL statements without committing
db.delete()	Marks an object for deletion
db.close()	Closes the session


8. Difference between flush() and commit()
flush()	commit()
Sends pending SQL statements to the database	Commits the transaction
Does not commit the transaction	Completes the transaction
Changes can still be rolled back	Transaction is committed


Example:
db.add(new_tool)db.flush()# Additional database operationsdb.commit()


9. SQLAlchemy 2.x query style
The older ORM approach uses:
db.query(Tool).all()


Modern SQLAlchemy 2.x commonly uses:
from sqlalchemy import selectstatement = select(Tool)result = db.scalars(statement).all()


Final Quick Revision – Must Remember
Concept	Important point
PostgreSQL	Stores project data persistently
SQL	Language used to communicate with databases
Primary Key	Uniquely identifies a row
Foreign Key	Connects two tables
One-to-Many	One tool can have many checkout records
ORM	Maps Python objects to relational database records
SQLAlchemy	Python ORM library
Model	Python class representing a database table
Pydantic	Validates API data
SQLAlchemy Session	Manages ORM operations and transactions
Flush	Sends pending SQL without committing
Commit	Commits the transaction
Rollback	Cancels uncommitted changes