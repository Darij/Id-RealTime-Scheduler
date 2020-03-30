# Code Challenge # 2

## Problem
On our system, each customer's account is run on an interval to make sure we don't miss any information. For example, each account in our system needs to run once every 15 minutes. You will write a piece of code that will do this scheduling. This function will be called EVERY minute at the top of the minute.

You have access to one piece of information, the list of account ids which will be in this format

account_ids = [1000, 1001, 1002, 1003 ...]

## Solution
Create a function that will schedule these accounts every 15 minutes by returning ONLY the account ids that need to run each minute. You can be guaranteed that this function will be called every minute, on the minute passing you only the account IDs on the system.

For example, account 1000 may run at minute 0, minute 15, minute 30, minute 45 and needs to be in the list of accounts returned each time the function is called during those minutes.

You can use any libraries or imports available with a clean environment using the language of your choice.


### Prerequisites
Python 2.7 or Python 3 and above

### Example
Go to console and run the script
```
python IdScheduler.py
```

To add you own list of Ids, or schedule at different times comment OUT the following code in main before running:

```
idscheduler.set_ids(account_ids=ACCOUNT_IDS,id_buffer=60, res_interval=15)
```


## Built With
* [Python 3] -- [Should run in python 2.7 as well]



## Authors

* **Dario Alberto Lopez Pesqueira** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
