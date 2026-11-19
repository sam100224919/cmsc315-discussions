# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used a Python dictionary to demonstrate hash table behavior through a restaurant reservation system. Each reservation confirmation code served as a key, and its guest name, reservation time, and party size were stored as the associated value.

## Implementation Summary

I created an initially empty dictionary and inserted six reservation records. I then looked up two existing confirmation codes, updated an existing reservation, and deleted a reservation. The program displayed the relevant values before and after the update and deletion so that the changes were observable.

I also tested edge cases. A lookup for a missing confirmation code used `get()` and returned `None` instead of raising a `KeyError`. I safely attempted to delete a missing key with `pop(key, None)`. I displayed an empty dictionary and tested what happened when an existing confirmation code was assigned a new value. The dictionary updated that reservation instead of creating a second entry with the same key.

## Hash Table Concepts and Performance

A hash table stores key-value pairs and uses a hash function to help determine where a key belongs in its internal structure. Python dictionaries provide average-case constant-time, O(1), lookup, insertion, and deletion operations. This makes a dictionary useful when a restaurant needs to find a reservation quickly among many bookings.

A collision occurs when two different keys produce the same hash value or map to the same internal table location. A collision must be resolved so that both entries remain accessible. Python handles collisions internally; this program uses the built-in dictionary and does not implement its own collision-resolution algorithm. As collisions and table occupancy increase, operations can require additional work, and worst-case lookup can become O(n). Resizing and the implementation's collision-handling strategy help maintain efficient average performance.

For a busy restaurant, fast lookups can reduce the time a host spends searching for a guest. The application would also need validation to prevent duplicate confirmation codes, careful handling of missing reservations, and testing with large booking volumes. In a production system, reservation changes would also need persistence and concurrency controls; the in-memory dictionary in this demonstration does not provide those features.

## Discussion Board Reflection

While completing this assignment, I learned how Python dictionaries demonstrate the key-value organization used by hash tables. I practiced inserting records, retrieving values by key, updating an existing entry, and deleting entries. I also learned why edge-case handling matters. For example, using `get()` or `pop()` with a default value allowed the program to handle a missing confirmation code without stopping with an exception.

One challenge was distinguishing an update from a duplicate insertion. When I assigned a new reservation value to an existing confirmation code, Python replaced the old value and kept the number of keys unchanged. I addressed this by displaying the reservation before and after the assignment and comparing the dictionary size. Hash tables use a hash function to locate keys efficiently, but different keys can produce collisions. Collision-resolution mechanisms allow those keys to remain stored and retrievable. With a well-distributed hash function, hash tables typically provide average-case O(1) lookup, insertion, and deletion, which is useful when restaurant staff need to search many reservations quickly. Poor collision behavior can increase the work required and reduce performance.

## Limitations

This assignment demonstrated Python's built-in dictionary rather than implementing a hash table from scratch. The program therefore illustrated dictionary operations and discussed collisions, but did not expose or modify Python's internal hashing or collision-resolution process.
