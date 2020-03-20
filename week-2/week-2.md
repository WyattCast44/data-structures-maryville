1. Give three examples of life-critical applications.

a. Pacemakers
b. Ventilator systems
c. Water purifications systems

2. Suppose you are on the design team for a new e-book reader. What are the primary classes and methods that the Python software for your reader will need? You should include an inheritance diagram for this code but you do not need to write any actual code. Your software architecture should at least include ways for customers to buy new books, view their list of purchased books, and read their purchased books.  The example for a transportation program below should reflect how your visual should look.

## Classes

- User
    - description: A user is anyone with an account, they can manage thier account, purchase new e-books and register new devices.
    - attributes:
        - id
        - name
        - email
        - password
        - created_at
        - updated_at
    - methods/abilities/interfaces:
        - registerAccount()
        - viewAccountDetails()
        - updateAccountDetails()
        - updatePaymentInformation()
        - deactiveAccount()

- UserDevices
    - description: A user can have many devices attached to their account
    - attributes:
        - id
        - user_id
        - type (DeviceType)
        - created_at
        - updated_at
    - methods/abilities/interfaces:
        - registerNewDevice()
        - listRegisteredDevices()
        - unregisterDevice()

- UserLibrary
    - description: A user has one library of books, magazines, etc
    - attributes:
        - id
        - user_id
        - created_at
        - updated_at
    - methods/abilities/interfaces:
        - purchaseItems()
        - listItems()
        - returnItems()

- UserLibraryItem
    - description: A users library consists of items
    - attributes:
        - id
        - name
        - excerpt
        - contents
        - chapers
    - methods/abilities/interfaces:
        - readItem()
        
        



3. In addition to these tasks, you must post a explaining your inheritance diagram from question #2.  This allows for you to demonstrate what would theoretically be occurring and how it is organized.  