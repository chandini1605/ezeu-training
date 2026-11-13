Pydantic is a Python library used to validate data against a model that we define.

In our Tool Library API, each tool should contain these four fields:
Field	Python type	Meaning
id	int	Unique tool ID
name	str	Name of the tool
category	str	Tool category
available	bool	Whether the tool is available


3. What is BaseModel?
BaseModel is the base class provided by Pydantic. We create our own model by defining a class that inherits from BaseModel.
from pydantic import BaseModel

class Tool(BaseModel):
    id: int
    name: str
    category: str
    available: bool
This Tool model describes the expected structure of tool data. The field annotations tell Pydantic which fields are required and the types expected for them.
4. Add the model to app.py
Add the Pydantic import with the other imports:
from pydantic import BaseModel
Add the Tool class below the imports and above app = FastAPI():
class Tool(BaseModel):
    id: int
    name: str
    category: str
    available: bool
For this step, leave the existing API endpoints unchanged.
5. Example request data
A valid example tool request body is:
{
  "id": 4,
  "name": "Keyboard",
  "category": "Electronics",
  "available": true
}
An example of incomplete or incorrectly typed data is:
{
  "id": "hello",
  "name": "Keyboard"
}
The model defines the expected fields and types. We will connect this model to the POST endpoint and test valid and invalid requests during this session.
6. Important distinction
Creating a Pydantic model does not add a new tool to the original tools list. It defines and validates the expected shape of incoming data.


Common validation errors
Error code|	Meaning	Example
422	| Unprocessable Entity	Missing required field
422	| Unprocessable Entity	Incorrect data type
422	| Unprocessable Entity	Invalid request body
400	| Bad Request	Application-defined invalid request
500	| Internal Server Error	Unexpected server-side error