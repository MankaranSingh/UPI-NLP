## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:account.transactions.check
- where was my [last](which_transaction) deposit from
- who have I got the [last](which_transaction) credit from
- who sent me the [last](which_transaction) credit
- who was my [last](which_transaction) deposit from
- how much money did i send
- how much money did i recieve
- when was my [last](which_transaction) transfer
- date of my [last](which_transaction) deposit
- check the [last](which_transaction) deposit
- can you show the date of my [last](which_transaction) credit
- when was the [last](which_transaction) credit
- when was my [last](which_transaction) deposit
- check my [last](which_transaction) credit
- how much was my [last](which_transaction) deposit
- was my [last](which_transaction) deposit large
- check the amount of my [last](which_transaction) credit
- show me the transaction history
- what is the transaction history
- transaction history
- transactions list

## synonym:deposit
- transaction
- credit

## intent:account.rewards.check
- what was my last reward 
- how much reward i got from last transaction
- what was the last reward 
- who was my last reward 
- how much money did i earn from last award
- when was my last reward 
- date of my last reward
- check the last reward
- can you show the date of my last reward
- when was the last reward
- when was my last reward
- check my last reward
- how much was my last reward
- check the amount of my last reward
- show me the rewards
- rewards history
- rewards list

## intent:account.balance.check
- check my [card] balance
- balance
- check my account
- what's the balance in my account
- show available money on my account
- how much money is available on my account
- how much money is available in my account
- check how much money do i have
- how much money do I have 
- how much money do I have on the [card]
- check my balance
- can you show balance on the [card]
- check money on my [card]
- show balance
- check my account
- what money i got
- how much money i got

## intent:transfer.money.send
- i need to send [2](amount) bucks to [mankaran](amount_to) 
- send money to [mankaran](amount_to)
- transfer [100](amount) rupees to [mankaran singh](account_to)
- pay [100](amount) rupees to [utkarsh mishra](account_to)
- send [100](amount) rupees to [mankaran](account_to)
- i need to send [2](amount) bucks to [utkarsh](account_to)
- can you send some money
- transfer
- send
- pay
- i want to transfer money
- tansfer money between accounts
- transfer to [shivam](account_to)
- pay for [utkarsh mishra](account_to)
- can you help me send some money
- card payment to [mankaran](account_to)
- [5000](amount) should be transferred to [mankaran](account_to)
- transfer money
- send money
- can you make a money transfer
- can you send money
- i need to pay [5000](amount) rupees to [shivam goyal](account_to)
- transfer [100](amount) to [shivam goyal](account_to)
- transfer money from one card to another

## lookup:account_to
names.txt

## intent:transfer.money.request
- i need to recieve [2](amount) bucks from [mankaran](amount_from) 
- recieve money from [mankaran](amount_from)
- request [100](amount) rupees from [mankaran singh](amount_from)
- get [100](amount) rupees from [utkarsh mishra](amount_from)
- i need to get [2](amount) bucks from [utkarsh](amount_from)
- can you request some money
- request
- recieve
- i want to request money
- request money between accounts
- request from [shivam](amount_from)
- recieve from [utkarsh mishra](amount_from)
- can you help me request some money
- card payment from [mankaran](amount_from)
- [5000](amount) should be requested from [mankaran](amount_from)
- request money
- recieve money
- can you make a money requests
- can you request money
- i need to request [5000](amount) rupees from [shivam goyal](amount_from)
- request [100](amount) from [shivam goyal](amount_from)
- recieve money from one card to another

## lookup:account_from
    names.txt

## synonym:transfer
- send
- sent

## synonym:card
- account
- credit card
- debit card

