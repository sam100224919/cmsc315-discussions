# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Implementation documentation

This implementation models connected household devices. `ParentClass` defines shared device information (`category`, `name`, and `status`) and a `describe()` method. `ChildClass` inherits from `ParentClass`, adds connection and battery attributes, tracks instances with a class variable, overrides `describe()`, and provides `recharge()`. The `super()` call reuses the parent constructor rather than duplicating its initialization logic.

`demonstrate_namespaces()` creates two child objects and prints their instance dictionaries (`__dict__`) alongside class-level information. It adds `location` to only one object to show that instance attributes can differ even when objects share a class. `demonstrate_copying()` creates nested mutable data, then compares `copy()` and `deepcopy()`: the shallow copy shares nested objects with the original, while the deep copy recursively copies them.

The student-created `AirQualityMonitor` extension inherits smart-device behavior and stores particle readings. Its `average_particles()` method returns the mean for numeric readings, returns `None` for an empty list, and raises a `TypeError` for invalid reading values. This is a practical example of using classes to model connected environmental-monitoring devices.

## Running the program

From this folder, run:

```bash
python unit1_discussion.py
```

The program demonstrates parent/child objects, method overriding, battery recharge, class and instance namespaces, shallow/deep copying, and the air-quality-monitor extension.

## Discussion board reflection (draft; personalize before posting)

Completing this assignment helped me understand how classes organize related data and behavior into reusable components. The parent class defines common device information, while the child class inherits that foundation and adds smart-device features. I also learned that class attributes are shared through the class, whereas instance attributes belong to individual objects. The namespace demonstration made this difference visible through each object's `__dict__`. One important challenge was understanding shallow and deep copying. A shallow copy creates a new outer container but still shares nested mutable objects, so changes to nested data can appear in both structures. A deep copy recursively duplicates nested data and keeps the copied values independent. Compared with procedural programming, OOP groups data and the operations that use it, which can make larger applications easier to maintain and extend. The air-quality-monitor example shows how a reusable device class can be adapted for a practical sensor application. Handling empty readings explicitly also makes the program more robust. These techniques could support future software that monitors airflow, filter performance, and indoor air quality.

*Before submitting, revise this reflection to match your own experience and what you personally found challenging.*
