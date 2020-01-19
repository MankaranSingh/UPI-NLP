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
- check my card balance
- balance
- check my account
- what's the balance in my account
- show available money on my account
- how much money is available on my account
- how much money is available in my account
- check how much money do i have
- how much money do I have 
- how much money do I have on the card
- check my balance
- can you show balance on the card
- check money on my card
- show balance
- check my account
- what money i got
- how much money i got

## intent:send_money
- i need to send [2.2566](amount) bucks to [aadil](PERSON)
- send money to [dad](PERSON)
- transfer [100](amount) rupees to [shivam](PERSON)
- transfer [100.2129](amount) rupees to [utkarsh](PERSON)
- pay [100](amount) rupees to [mom](PERSON)
- send [100.5829](amount) rupees to [shivam goyal](PERSON)
- i need to send [2](amount) bucks to [mankaran singh](PERSON)
- can you send some money to [mankaran singh](PERSON)
- transfer to [utkarash mishra](PERSON)
- send to [shivam goyal](PERSON)
- pay to [mankaran singh](PERSON)
- i want to transfer money to [utkarsh mishra](PERSON)
- tansfer money between accounts
- can you help me send some money to [mankaran singh](PERSON)
- card payment 
- transfer money to [utkarsh mishra](PERSON)
- send money to [shivam goyal](PERSON)
- can you make a money transfer to [mankaran](PERSON)
- can you send money to [mankaran singh](PERSON)
- i need to pay [5000](amount) rupees to [shivam goyal](PERSON)
- transfer [100](amount) to [aadil](PERSON)
- transfer money from one card to another

## lookup:PERSON
names_cleaned.txt

## regex:amount
- (?=.)(([0-9]+)( ?\. ?([0-9]+))?)

## intent:recieve_money
- i need to recieve some bucks 
- i need to recieve some rupees money
- can i recieve some money
- qr code to recieve some money 
- my qr code
- my bhim qr image
- recieve money 
- recieve
- recieve money
- recieve money from one card to another

## intent:scan
- scan qr code
- scan
- qr code scanner
- qr code
- i need to scan a qr code
- scan it 

## intent:request_money
- request [100 . 589](amount) rupees from [mankaran singh](PERSON)
- request [100 .589](amount)  from [utkarsh singh](PERSON)
- request [100. 589](amount) bucks from [shivam singh](PERSON)
- request from [utkarsh mishra](PERSON)
- i want to request money from [shivam goyal](PERSON)
- request money between accounts 
- can you help me request some money from [mankaran](PERSON)
- [5000.85939239](amount) should be requested from [shivam goyal](PERSON)
- request money from [utkarsh singh](PERSON)
- can you make a money requests from [mankaran singh](PERSON)
- can you request money from [lowinder sethi](PERSON)
- i need to request [5000](amount) rupees from [mankaran singh](PERSON)
- request [100.5554](amount) from [shivam](PERSON)
- get [100](amount) rupees from [utkarsh chauhan](PERSON)
- i need to get [2](amount) bucks from [mankaran singh](PERSON)
- can you request some money from [aadil](PERSON)

## lookup:PERSON
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