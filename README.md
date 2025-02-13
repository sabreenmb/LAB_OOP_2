# LAB_OOP_2

Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged (make sure to handle the exception when calling the method).
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.

---------
