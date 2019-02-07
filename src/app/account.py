class Account:

    def __init__(self, *, firstname, lastname, number, balance=0.0):
        assert isinstance(number, int), 'Number needs to be an integer'
        assert isinstance(balance, float), 'Balance needs to be a float'

        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.balance = balance

        # path_info = {
        #     'root': '/path/to/docs',
        #     'number': self.number,
        #     'type': 'statements',
        #     'filename': 'ABCDEFG'}
        #
        # statement_path = self.path_template.format(**path_info)
        #
        # statement_path = self.path_template.format('root': '/path/to/docs',
        #                                            'number': self.number,
        #                                            'type': 'statements',
        #                                            'filename': 'ABCDEFG')

    def info(self):
        template = 'Number {number}: {firstname} {lastname} - {balance} €'
        return template.format(number=self.number, firstname=self.firstname, lastname=self.lastname, balance=self.balance)

    # alternative(n) für .info:
    # def info(self):
    #     return f'Number {self.number}: {self.firstname} {self.lastname} - {self.balance} €'

    def has_funds_for(self, amount):
        return self.balance >= amount

    def add_to_balance(self, amount):
        assert amount > 0, 'Amount needs to be greater than 0'
        self.balance = self.balance + amount

    def subtract_from_balance(self, amount):
        assert amount < self.balance, 'Account has not enough funds'
        self.balance = self.balance - amount
