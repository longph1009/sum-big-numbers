
# Installation and Usage Guide for `MyBigNumber` API

This guide provides step-by-step instructions to install, run, and manage the `MyBigNumber` API using Flask.

---

## **1. Prerequisites**
Before proceeding, ensure you have the following installed:
- **Python 3.x**: Download and install from [python.org](https://www.python.org/).
- **Git** (optional): For cloning the repository if applicable.

---

### **Step 1: Create a Virtual Environment**
To isolate dependencies, create a virtual environment:
```bash
python -m venv venv
```

### **Step 2: Activate the Virtual Environment**
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

After activation, you should see `(venv)` in your terminal prompt.

### **Step 3: Install Dependencies**
Install the required libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## **2. Running the Application**

### **Step 1: Start the Flask Server**
Run the application using:
```bash
python app.py
```

By default, the server runs on `http://localhost:5000`. 
```bash
flask run
```

### **Step 2: Test the API**
You can test the API using tools like Postman, cURL, or directly in your browser.

#### **Example Request**
```bash
curl -X POST http://localhost:5000/sum \
-H "Content-Type: application/json" \
-d '{"num1": "123.45", "num2": "-67.89"}'
```

#### **Example Response**
```json
{
  "result": "55.56",
  "num1": "123.45",
  "num2": "-67.89"
}
```

---

## **3. Stopping the Application**

### **Step 1: Stop the Flask Server**
To stop the server, press `Ctrl + C` in the terminal where the server is running.

### **Step 2: Deactivate the Virtual Environment**
Once the server is stopped, deactivate the virtual environment:
```bash
deactivate
```

---

## **4. Directory Structure**
Your project should look like this:
```
your_project/
├── core.py          # Contains the MyBigNumber implementation
├── app.py           # Flask API
├── requirements.txt # List of dependencies
└── venv/            # Virtual environment folder
```

---

## **5. Additional Notes**
- **Debug Mode**: The Flask server runs in debug mode by default (`debug=True` in `app.run()`). This is useful for development but should be disabled in production.
- **Scaling**: For production environments, consider deploying the API using a WSGI server like Gunicorn or uWSGI.

---

For further assistance, refer to the official Flask documentation: [Flask Documentation](https://flask.palletsprojects.com/).
```
