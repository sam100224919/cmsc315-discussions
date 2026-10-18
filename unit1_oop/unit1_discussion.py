"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    """Represent a basic device with shared class information."""

    category = "General Device"  # Class variable shared by all ParentClass objects.

    def __init__(self, name, status):
        # Instance variables belong to each individual object.
        self.name = name
        self.status = status

    def describe(self):
        """Return a readable description of this device."""
        return f"{self.name} is a {self.category}; current status: {self.status}."

    def __str__(self):
        return self.describe()


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    """Represent a smart device with additional features."""

    device_count = 0  # New class variable for tracking created smart devices.

    def __init__(self, name, status, connection, battery_level):
        # Reuse the parent's initialization for name and status.
        super().__init__(name, status)
        self.connection = connection
        self.battery_level = battery_level
        ChildClass.device_count += 1

    def describe(self):
        """Override the parent method to include smart-device details."""
        return (
            f"{self.name} is a smart device; status: {self.status}, "
            f"connection: {self.connection}, battery: {self.battery_level}%."
        )

    def recharge(self, amount):
        """Increase the battery level while keeping it between 0 and 100."""
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Recharge amount must be a number.")
        if amount < 0:
            raise ValueError("Recharge amount cannot be negative.")
        self.battery_level = min(100, self.battery_level + amount)
        return self.battery_level


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    device_one = ChildClass("Living Room Camera", "Online", "Wi-Fi", 85)
    device_two = ChildClass("Front Door Lock", "Locked", "Wi-Fi", 100)

    # Access the class variable through the class and through an instance.
    print("Class category:", ParentClass.category)
    print("Category through device_one:", device_one.category)
    print("Child class device count:", ChildClass.device_count)

    # This attribute belongs only to device_one, not to device_two or the class.
    device_one.location = "Living room"

    print("device_one namespace:", device_one.__dict__)
    print("device_two namespace:", device_two.__dict__)
    print("ChildClass namespace keys:", sorted(ChildClass.__dict__.keys()))
    print("device_one description:", device_one.describe())
    print("device_two description:", device_two.describe())


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = {
        "device": "Air Quality Monitor",
        "readings": {"temperature": [21, 22], "particles": [12, 10]},
    }

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy creates a new outer dictionary, but nested objects are shared.
    # A deep copy recursively copies nested objects, so nested changes stay separate.
    original["readings"]["temperature"].append(23)
    original["readings"]["particles"][0] = 99

    print("Original:", original)
    print("Shallow copy (nested data reflects changes):", shallow_copy)
    print("Deep copy (nested data remains unchanged):", deep_copy)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.


# Student-created extension: a specialized air-quality monitor.
class AirQualityMonitor(ChildClass):
    """A smart device that stores particulate readings and summarizes them."""

    def __init__(self, name, status, connection, battery_level, readings=None):
        super().__init__(name, status, connection, battery_level)
        self.readings = list(readings) if readings is not None else []

    def average_particles(self):
        """Return the average reading, or None when no readings are available."""
        if not self.readings:
            return None
        if any(not isinstance(value, (int, float)) or isinstance(value, bool) for value in self.readings):
            raise TypeError("All particle readings must be numeric values.")
        return sum(self.readings) / len(self.readings)

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object.
    basic_device = ParentClass("Desk Fan", "On")
    print("\nParent object:", basic_device.describe())

    # Create and test a child object; it inherits name/status and describe behavior
    # structure from ParentClass, while ChildClass overrides describe().
    smart_device = ChildClass("Smart Thermostat", "Running", "Wi-Fi", 72)
    print("\nChild object:", smart_device.describe())
    print("Battery after recharge:", smart_device.recharge(10), "%")

    # Student-created extension: analyze readings from an air-quality monitor.
    monitor = AirQualityMonitor("Bedroom Air Monitor", "Monitoring", "Wi-Fi", 90, [12, 15, 9])
    print("\nExtension object:", monitor.describe())
    print("Average particle reading:", monitor.average_particles())

    # Edge case: an empty readings list has no average, so the method returns None.
    empty_monitor = AirQualityMonitor("New Air Monitor", "Ready", "Wi-Fi", 100)
    print("Average for empty readings:", empty_monitor.average_particles())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
