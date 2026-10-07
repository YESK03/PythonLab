# Experiment 7: Object-Oriented Programming (OOP) in Python

## AIM

The aim of this experiment is to understand and implement the fundamental concepts of Object-Oriented Programming (OOP) in Python, including:
- Creating classes and objects
- Understanding global and local variables within a class
- Implementing methods to perform various operations
- Demonstrating the concept of data encapsulation
- Applying OOP principles to solve real-world problems like calculator operations and student grade calculation

## OBJECTIVES

1. **Understand Classes and Objects**: Learn how to define a class and create instances (objects) of that class.
2. **Global vs Local Variables**: Understand the scope of variables within a class (class variables vs instance variables).
3. **Methods and Functions**: Implement methods within a class to perform specific operations.
4. **Method Invocation**: Learn how to call methods using object references with the `self` parameter.
5. **Real-world Application**: Apply OOP concepts to build practical programs like calculators and grade management systems.

---

## ALGORITHM

### **Algorithm 1: Calculator Class (Exp_7.py)**

#### Problem: Create a calculator class that performs basic arithmetic operations

**Steps:**
1. Define a class named `calcu`
2. Declare class variables:
   - `x` ← Input integer value
   - `y` ← Input integer value
3. Define methods:
   - `Add()`: Calculate and print x + y
   - `Sub()`: Calculate and print x - y
   - `Mul()`: Calculate and print (x * y) * local_variable
   - `div()`: Calculate and print x / y
4. Create an object of the class `calcu`
5. Call all methods using the object reference
6. Display the results

**Pseudocode:**
```
CLASS calcu:
    x = input("Enter X")
    y = input("Enter Y")
    
    METHOD Add():
        PRINT x + y
    
    METHOD Sub():
        PRINT x - y
    
    METHOD Mul():
        c = 2  (local variable)
        PRINT (x * y) * c
    
    METHOD div():
        PRINT x / y

END CLASS

obj = CREATE calcu()
obj.Add()
obj.Mul()
obj.Sub()
obj.div()
```

---

### **Algorithm 2: Student Grade Calculation - Average Based (Exp_7a.py)**

#### Problem: Calculate student grades based on the average of five subjects

**Steps:**
1. Define a class named `Stud`
2. Declare class variables to store marks:
   - `m1, m2, m3, m4, m5` ← Input marks for 5 subjects
3. Calculate:
   - `tot` ← m1 + m2 + m3 + m4 + m5
   - `avg` ← tot / 5
4. Define method `bigcal()`:
   - IF avg >= 90 → Print "Grade 1st"
   - ELSE IF avg >= 81 → Print "Grade 2nd"
   - ELSE IF avg >= 71 → Print "Grade 3rd"
   - ELSE → Print "Fourth Grade"
5. Create object and call method

**Pseudocode:**
```
CLASS Stud:
    m1 = input("Enter Marks1")
    m2 = input("Enter Marks2")
    m3 = input("Enter Marks3")
    m4 = input("Enter Marks4")
    m5 = input("Enter Marks5")
    
    tot = m1 + m2 + m3 + m4 + m5
    avg = tot / 5
    
    METHOD bigcal():
        IF avg >= 90:
            PRINT "Grade 1st"
        ELSE IF avg >= 81:
            PRINT "Grade 2nd"
        ELSE IF avg >= 71:
            PRINT "Grade 3rd"
        ELSE:
            PRINT "Fourth Grade"

END CLASS

s = CREATE Stud()
s.bigcal()
```

---

### **Algorithm 3: Student Grade Calculation - Total Marks Based (Exp_7o.py)**

#### Problem: Calculate student grades based on the total marks of five subjects

**Steps:**
1. Define a class named `Stud`
2. Declare class variables:
   - `m1, m2, m3, m4, m5` ← Input marks for 5 subjects
3. Calculate:
   - `tot` ← m1 + m2 + m3 + m4 + m5
   - `avg` ← tot / 5
4. Define method `bigcal()`:
   - IF tot >= 90 AND tot <= 100 → Print "Grade 1st"
   - ELSE IF tot >= 81 AND tot <= 89 → Print "Grade 2nd"
   - ELSE IF tot >= 71 AND tot <= 79 → Print "Grade 3rd"
   - ELSE → Print "Fourth Grade"
5. Create object and call method

**Pseudocode:**
```
CLASS Stud:
    m1 = input("Enter Marks1")
    m2 = input("Enter Marks2")
    m3 = input("Enter Marks3")
    m4 = input("Enter Marks4")
    m5 = input("Enter Marks5")
    
    tot = m1 + m2 + m3 + m4 + m5
    avg = tot / 5
    
    METHOD bigcal():
        IF (tot >= 90 AND tot <= 100):
            PRINT "Grade 1st"
        ELSE IF (tot >= 81 AND tot <= 89):
            PRINT "Grade 2nd"
        ELSE IF (tot >= 71 AND tot <= 79):
            PRINT "Grade 3rd"
        ELSE:
            PRINT "Fourth Grade"

END CLASS

s = CREATE Stud()
s.bigcal()
```

---

### **Algorithm 4: Multiple Methods Demonstration (example.py)**

#### Problem: Demonstrate the use of global and local variables in a class with multiple methods

**Steps:**
1. Define a class named `KSEC`
2. Declare a global class variable:
   - `X = 10`
3. Define multiple methods:
   - `Name()`: Create local variable Y = 100, print X + Y
   - `Proj()`: Create local variable Y = 200, print X + Y
   - `Proj1()`: Create local variable Y = 300, print X * Y
4. Create an object of the class
5. Call all methods using the object reference

**Pseudocode:**
```
CLASS KSEC:
    X = 10  (Global variable)
    
    METHOD Name():
        Y = 100  (Local variable)
        PRINT X + Y  (110)
    
    METHOD Proj():
        Y = 200  (Local variable)
        PRINT X + Y  (210)
    
    METHOD Proj1():
        Y = 300  (Local variable)
        PRINT X * Y  (3000)

END CLASS

obj = CREATE KSEC()
obj.Name()
obj.Proj()
obj.Proj1()
```

---

## KEY CONCEPTS

1. **Class**: A blueprint for creating objects with attributes and methods
2. **Object**: An instance of a class
3. **Self Parameter**: Represents the instance of the class; used to access class variables and methods
4. **Global Variable**: Class variable defined at class level; accessible to all methods
5. **Local Variable**: Variable defined within a method; accessible only within that method
6. **Method**: A function defined inside a class that performs specific operations
7. **Scope**: The region where a variable is accessible and valid

---

## LEARNING OUTCOMES

After completing this experiment, students will be able to:
- ✓ Define and create classes in Python
- ✓ Understand the difference between global and local variables
- ✓ Implement methods within a class
- ✓ Use the `self` parameter correctly
- ✓ Create objects from classes and invoke methods
- ✓ Solve practical problems using OOP concepts
