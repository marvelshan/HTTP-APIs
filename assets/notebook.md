## Tool Research

### pydantic

Cuz python is Dynamic Typing, in order to make it specifically and I try to implement Pydantic to validate code.

```python
class Sign_up_input (BaseModel):
    username: str
    password: str

    @field_validator("username")
    def username_length(cls, v):
        if len(v) < 3 or len(v) > 32:
            error_message = "Username length must be between 3 and 32 characters"
            raise ValueError(error_message)
        return v

    @field_validator("password")
    def password_length(cls, v):
        if len(v) < 8 or len(v) > 32:
            error_message = "Password length must be between 8 and 32 characters"
            raise ValueError(error_message)
        return v

    @field_validator("password")
    def password_complexity(cls, v):
        if not any(char.isupper() for char in v):
            raise ValueError(
                "Password must contain at least one uppercase letter")
        if not any(char.islower() for char in v):
            raise ValueError(
                "Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one number")
        return v
```

### SQLAlchemy

**CRUD:** (example on the Internet)

```python
#Create
def create_test(db: Session, test_data: dict) -> Test:
    created_test = Test(**test_data)
    db.add(created_test)
    db.commit()
    return created_test
```

```python
#Read
def get_test_by_id(db: Session, test_id: int) -> Test:
    result = db.query(Test).filter_by(id=test_id).first()
    db.commit()
    return result
```

```python
#Update
def update_test(db: Session, test_id: int, _update_data: dict) -> int:
    r = db.query(Test).filter_by(id=test_id).update(_update_data)
    db.commit()
    return r
```

```python
#Delete
def delete_test(db: Session, test_id: int) -> int:
    r = db.query(Test).filter_by(id=test_id).delete()
    db.commit()
    return r
```

Source by:
[Postgresql + Sqlalchemy ORM CRUD 方式 - HackMD](https://hackmd.io/@UTRxSLfpRa6ds1oeI2U7Lw/s9891326)

### WSGI, Gunicorn:

![WSGI](https://github.com/marvelshan/HTTP-APIs/blob/develop/assets/WSGI.png)

Asking ChatGPT:

> Why does Flask need to use WSGI, while a NodeJS server does not require it?

Flask, a Python microframework, typically uses WSGI (Web Server Gateway Interface) to communicate between the Python web application and the web server. WSGI acts as a bridge, allowing the Python application (like Flask) to interface with various web servers like Apache or Nginx. It provides a standardized way for web servers to forward requests to Python applications and receive responses back.

On the other hand, Node.js, being a server-side JavaScript runtime, doesn't need a separate interface like WSGI. Instead, it includes its own built-in web server capabilities through libraries like **`http`** or **`Express.js`**. Node.js applications can directly listen for incoming HTTP requests and handle responses without needing an additional interface layer like WSGI.

So, the difference in usage of WSGI between Flask and Node.js is primarily due to the architectural differences between Python and JavaScript for web server development. Python web applications typically rely on WSGI for interoperability with web servers, while Node.js applications handle HTTP communication internally without the need for such an interface.

> What pros and cons?

### **Pros of WSGI (with Flask):**

1. **Interoperability**: WSGI provides a standardized interface between Python web applications and various web servers. This means Flask applications can run on different server environments without modification.
2. **Flexibility**: Developers can choose from a variety of WSGI-compliant web servers (e.g., Gunicorn, uWSGI) to deploy Flask applications, allowing them to select the server that best suits their performance and scaling needs.
3. **Middleware Support**: WSGI supports middleware, allowing developers to easily integrate additional functionalities like authentication, caching, or logging into their Flask applications.

### **Cons of WSGI (with Flask):**

1. **Complexity**: Configuring and deploying WSGI servers can be more complex compared to Node.js, which typically involves fewer moving parts since Node.js applications often handle HTTP communication internally.
2. **Performance Overhead**: While WSGI serves as a reliable interface, it may introduce some performance overhead compared to Node.js's built-in server capabilities, where the HTTP handling is tightly integrated into the language runtime.

```bash
pip install gunicorn
```

```bash
gunicorn -b 0.0.0.0:5000 app:app
```

### Virtual environment:

The `venv` module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their [site](https://docs.python.org/3/library/site.html#module-site) directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

Source by:
[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

### PEP8 Coding Style:

As Guido van Rossum said, “Code is read much more often than it’s written.” You may spend a few minutes, or a whole day, writing a piece of code to process user authentication. Once you’ve written it, you’re never going to write it again.

But you’ll definitely have to read it again. That piece of code might remain part of a project you’re working on. Every time you go back to that file, you’ll have to remember what that code does and why you wrote it, so readability matters.

It can be difficult to remember what a piece of code does a few days, or weeks, after you wrote it.

If you follow PEP 8, you can be sure that you’ve named your variables well. You’ll know that you’ve added enough whitespace so it’s easier to follow logical steps in your code. You’ll also have commented your code well. All of this will mean your code is more readable and easier to come back to. If you’re a beginner, following the rules of PEP 8 can make learning Python a much more pleasant task.

Source by:
[How to Write Beautiful Python Code With PEP 8 – Real Python](https://realpython.com/python-pep8/)

---

_The completion year for the above: 2024_
