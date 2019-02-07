import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        if not type(account) is app.Account:
            raise AssertionError('Account should be an app.Account')
        elif account.number in self.accounts:
            raise AssertionError('Account number 1 already taken!')
        else:
            self.accounts.update({account.number: account})
            return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        if amount <= 0:
            raise AssertionError('Amount needs to be greater than 0')
        elif sender.number not in self.accounts:
            raise AssertionError('Sender has no account yet!')
        elif recipient.number not in self.accounts:
            raise AssertionError('Recipient has no account yet!')
        else:
            trans = app.Transaction(sender=sender.number,
                                    recipient=recipient.number,
                                    subject=subject,
                                    amount=amount)
            self.transactions.append(trans)
            self._update_funds(sender, recipient, amount)
            return trans

    def _update_funds(self, sender, recipient, amount):
        if sender.has_funds_for(amount):
            recipient.add_to_balance(amount)
            sender.subtract_from_balance(amount)
        else:
            self.transactions.pop()
            raise AssertionError('Account has not enough funds')

    def tot_revenue(self):
        amounts = [transaction['amount'] for transaction in self.transactions]
        return sum(amounts)

    def ind_transaction(self):
        counts = [transaction['sender'] for transaction in self.transactions]
        str.count(counts)

    def info(self):
        print('Name: ' + self.name)
        print('Account(s): ' + str(len(self.accounts)))
        for account in self.accounts:
            print('Name: ' + account['lastname'] + ', ' + account['firstname'])
        print('Transaction(s): ' + str(len(self.transactions)))
        print('Total revenue streams: {}'.format(self.tot_revenue()))
