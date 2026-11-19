"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # The reservation confirmation code is the key, and the
    # guest/reservation details are the value. Python dictionaries
    # use hashing to organize keys for efficient average-case access.
    reservations = {}
    reservations["R1001"] = {"guest": "Maya Chen", "time": "6:00 PM", "party": 2}
    reservations["R1002"] = {"guest": "Jordan Lee", "time": "6:15 PM", "party": 4}
    reservations["R1003"] = {"guest": "Avery Patel", "time": "6:30 PM", "party": 3}
    reservations["R1004"] = {"guest": "Noah Williams", "time": "6:45 PM", "party": 5}
    reservations["R1005"] = {"guest": "Sofia Garcia", "time": "7:00 PM", "party": 2}
    print("Initial reservation hash table:")
    for confirmation, details in reservations.items():
        print(f"{confirmation}: {details}")

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    # A new unique confirmation code adds a new key-value entry.
    reservations["R1006"] = {"guest": "Ethan Brooks", "time": "7:15 PM", "party": 6}
    print(f"Added R1006: {reservations['R1006']}")
    print(f"Reservation count: {len(reservations)}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")
    # Looking up a confirmation code hashes the key and uses the
    # dictionary's internal index structure to locate its value.
    for confirmation in ("R1002", "R1005"):
        print(f"Lookup {confirmation}: {reservations[confirmation]}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    print(f"Before update, R1003: {reservations['R1003']}")
    # Assigning a new value to an existing key replaces its previous value;
    # it does not create a second entry with the same key.
    reservations["R1003"] = {"guest": "Avery Patel", "time": "7:30 PM", "party": 4}
    print(f"After update, R1003:  {reservations['R1003']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    print(f"Before deletion, R1004 exists: {'R1004' in reservations}")
    # Deleting a key removes its key-value entry from the dictionary.
    del reservations["R1004"]
    print(f"After deletion, R1004 exists: {'R1004' in reservations}")
    print(f"Reservation count after deletion: {len(reservations)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: A missing confirmation code should not crash the
    # reservation search. get() returns None when the key is absent.
    missing = reservations.get("R9999")
    print(f"Lookup missing R9999: {missing} (None means no reservation was found)")

    # Edge case 2: Deleting a missing key with pop(..., None) safely
    # avoids the KeyError that del would raise for an absent key.
    removed = reservations.pop("R9999", None)
    print(f"Safe deletion of missing R9999: {removed}")

    # Edge case 3: An empty reservation dictionary contains no entries.
    empty_reservations = {}
    print(f"Empty reservation table: {empty_reservations}; count: {len(empty_reservations)}")

    # Duplicate confirmation codes: assigning an existing key updates
    # that entry rather than storing a duplicate key. A production system
    # should validate codes and reject accidental duplicate booking IDs.
    before_duplicate = len(reservations)
    reservations["R1001"] = {"guest": "Maya Chen", "time": "6:00 PM", "party": 3}
    print(
        "Reusing R1001 updated the existing reservation; "
        f"count stayed {before_duplicate} -> {len(reservations)}"
    )
    print(f"Final reservation table: {reservations}")


if __name__ == "__main__":
    main()
