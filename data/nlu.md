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

## intent:check_transfer_history
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
- show me [last](which_transaction) transaction 
- whats was my [last](which_transaction) transaction
- how much was my [last](which_transaction) transaction
- transaction details
- [last](which_transaction) transaction details
- [last](which_transaction) transaction
- last

## synonym:deposit
- transaction
- credit

## intent:check_rewards
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

## intent:check_balance
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

## intent:send_money
- i need to send [2.2566](amount) bucks to [aadil](name)
- send money to [mankaran](name)
- transfer [100](amount) rupees to [shivam](name)
- transfer [100.2129](amount) rupees to [utkarsh](name)
- pay [100](amount) rupees to [mankaran](name)
- send [100.5829](amount) rupees to [shivam goyal](name)
- i need to send [2](amount) bucks to [mankaran singh](name)
- can you send some money to [mankaran singh](name)
- transfer to [utkarash mishra](name)
- send to [shivam goyal](name)
- pay to [mankaran singh](name)
- i want to transfer money to [utkarsh mishra](name)
- tansfer money between accounts
- can you help me send some money to [mankaran singh](name)
- card payment 
- transfer money to [utkarsh mishra](name)
- send money to [shivam goyal](name)
- can you make a money transfer to [mankaran](name)
- can you send money to [mankaran singh](name)
- i need to pay [5000](amount) rupees to [shivam goyal](name)
- transfer [100](amount) to [aadil](name)
- transfer money from one card to another

## lookup:name
names_cleaned.txt

## regex:amount
- (?=.)(([0-9]+)( ?\. ?([0-9]+))?)

## intent:receive_money
- i need to receive some bucks 
- i need to receive some rupees money
- can i receive some money
- qr code to receive some money 
- my qr code
- my bhim qr image
- receive money 
- receive
- receive money
- receive money from one card to another

## intent:scan
- scan qr code
- scan
- qr code scanner
- qr code
- i need to scan a qr code
- scan it 

## intent:request_money
- request [100 . 589](amount) rupees from [mankaran singh](name)
- request [100 .589](amount)  from [utkarsh singh](name)
- request [100. 589](amount) bucks from [shivam singh](name)
- request from [utkarsh mishra](name)
- i want to request money from [shivam goyal](name)
- request money between accounts 
- can you help me request some money from [mankaran](name)
- [5000.85939239](amount) should be requested from [shivam goyal](name)
- request money from [utkarsh singh](name)
- can you make a money requests from [mankaran singh](name)
- can you request money from [lowinder sethi](name)
- i need to request [5000](amount) rupees from [mankaran singh](name)
- request [100.5554](amount) from [shivam](name)
- get [100](amount) rupees from [utkarsh chauhan](name)
- i need to get [2](amount) bucks from [mankaran singh](name)
- can you request some money from [aadil](name)

## lookup:name
names_cleaned.txt

## regex:amount
- (?=.)(([0-9]+)( ?\. ?([0-9]+))?)

## synonym:transfer
- send
- sent

## synonym:card
- account
- credit card
- debit card

