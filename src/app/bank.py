class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        message1 = 'Account number 1 already taken!'
        account_already_exists = 0
        for old_account in self.accounts:
            if old_account['number'] == account['number']:
                account_already_exists = 1
        assert account_already_exists == 0, message1
        self.accounts.append(account)
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        transaction = {'sender': sender,
                       'recipient': recipient,
                       'subject': subject,
                       'amount': amount}
        message2 = 'Amount has to be greater than 0'
        assert amount > 0, message2
        self.transactions.append(transaction)
        return transaction

    def tot_revenue(self):
        amounts = [transaction['amount'] for transaction in self.transactions]
        return sum(amounts)

    def info(self):
        print('Name: ' + self.name)
        print('Account(s): ' + str(len(self.accounts)))
        for account in self.accounts:
            print('Name: ' + account['lastname'] + ', ' + account['firstname'])
        print('Transaction(s): ' + str(len(self.transactions)))
        print('Total revenue streams: {}' .format(self.tot_revenue()))
