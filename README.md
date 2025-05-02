# Testing Guide for `test_core.py`

This guide provides step-by-step instructions to run the test suite for the `MyBigNumber` class implemented in `core.py`.

---

## **Prerequisites**
1. **Python 3.x** installed on your system.
2. Ensure `core.py` (containing the `MyBigNumber` class) is in the same directory as `test_core.py`.

---

## **Project Structure**
Your project directory should look like this:
```
your_project_folder/
├── core.py          # Contains the MyBigNumber implementation
└── test_core.py     # Test suite for MyBigNumber
```

---

## **Running the Tests**

### **1. Using `unittest` Module**
Open a terminal and navigate to the project directory. Run:
```bash
python -m unittest test_core.py
```

### **2. Direct Execution**
Alternatively, execute the test file directly:
```bash
python test_core.py
```

---

## **Expected Output**
- **All tests pass**:  
  ```
  .....
  ----------------------------------------------------------------------
  Ran 5 tests in 0.001s

  OK
  ```
- **Test failures/errors**:  
  Detailed logs about which test(s) failed and why.

---

## **Test Cases Overview**
The test suite validates the `MyBigNumber.sum()` method for:
1. **Positive/Negative Integers**  
   - `test_sum_positive_integers`  
   - `test_sum_negative_integers`
2. **Decimal Numbers**  
   - `test_sum_positive_decimals`  
   - `test_sum_negative_decimals`
3. **Edge Cases**  
   - Leading zeros (`test_sum_leading_zeros`).  
   - Mixing integers and decimals (`test_sum_integer_and_decimal`).  
4. **Input Validation** 
   - Rejects multiple commas/decimals (`test_multiple_commas`).  
   - Rejects invalid characters (`test_invalid_characters`).

---

## **Troubleshooting**
- **ImportError**: Ensure `core.py` exists and contains the `MyBigNumber` class.
- **Test Failures**:  
  - Check if `MyBigNumber.sum()` handles edge cases (e.g., decimals, negative numbers).  
  - Verify input validation logic (e.g., commas vs. periods).
- **Syntax Errors**: Ensure Python 3 compatibility.

For further details, inspect the test logs or debug specific test cases.


**Brief Overview of the Large Number Summation Code (`MyBigNumber`):**

This code implements the `MyBigNumber` class to perform **addition of large numbers** (in string format), supporting integers, decimals, and negative numbers. Key features include:

---

### **Core Functionality:**
1. **Flexible Input Handling**:
   - Supports both **commas (`,`)** and **periods (`.`)** as decimal separators.
   - Automatically removes **leading zeros** (e.g., `00123` → `123`).
   - Validates inputs: rejects numbers with **multiple decimal separators** or invalid characters (e.g., letters).

2. **Integer and Decimal Addition**:
   - Splits numbers into **integer** and **decimal parts** for separate processing.
   - Uses **carry-over logic** for digit-by-digit addition (e.g., `9 + 9 = 18` → carry `1`).

3. **Negative Number Handling**:
   - Converts addition of negative numbers into **subtraction** (e.g., `10 + (-5)` → `10 - 5`).
   - Uses comparison logic to determine the sign of the result when numbers have mixed signs.

4. **Comparison Logic**:
   - The `compare()` method checks if one number is larger than another by analyzing digits, which is critical for subtraction operations.

5. **Detailed Logging**:
   - Logs all operations to `core.log` for debugging (e.g., input validation, intermediate steps).

---

### **Key Components:**
- **`sum()` Method**:
  - Validates inputs (`checkBigNumber`).
  - Splits numbers into integer/decimal parts and processes their signs.
  - Combines results after handling addition/subtraction for each part.

- **Helper Methods**:
  - `sumDigit()`: Adds single digits with carry-over.
  - `subtractDigit()`: Subtracts single digits with borrowing.
  - `sumDecimal()`/`sumInteger()`: Handles decimal and integer parts separately.

---

### **Example Workflow:**
- **Input**: `"123.45" + "-67.89"`  
  **Processing**:
  1. Split into:  
     - Number 1: `123` (integer), `45` (decimal), sign `+`  
     - Number 2: `67` (integer), `89` (decimal), sign `-`  
  2. Convert to subtraction: `123.45 - 67.89`  
  3. Result: `"55.56"`.

---

The code ensures **high precision** for extremely large numbers (beyond primitive data type limits) and focuses on **exception handling** to gracefully manage invalid inputs.