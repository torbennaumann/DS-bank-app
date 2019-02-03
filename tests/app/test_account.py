import unittest
import app


class TestAccount(unittest.TestCase):
    def test_account_can_be_initialized(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=100.0)
        self.assertTrue(type(account) == app.Account)
        self.assertEqual(account.firstname, 'Albert')
        self.assertEqual(account.lastname, 'Einstein')
        self.assertEqual(account.number, 1)
        self.assertEqual(account.balance, 100.0)

    def test_account_init_number_needs_to_be_an_integer(self):
        message = 'Number needs to be an integer'
        with self.assertRaisesRegex(AssertionError, message):
            app.Account(firstname='Albert',
                        lastname='Einstein',
                        number='1',
                        balance=100.0)

        message = 'Number needs to be an integer'
        with self.assertRaisesRegex(AssertionError, message):
            app.Account(firstname='Albert',
                        lastname='Einstein',
                        number=1.11,
                        balance=100.0)

    def test_account_init_balance_is_optional(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1)

        self.assertEqual(account.balance, 0.0)

    def test_account_init_balance_needs_to_be_a_float(self):
        message = 'Balance needs to be a float'
        with self.assertRaisesRegex(AssertionError, message):
            app.Account(firstname='Albert',
                        lastname='Einstein',
                        number=1,
                        balance=100)

        message = 'Balance needs to be a float'
        with self.assertRaisesRegex(AssertionError, message):
            app.Account(firstname='Albert',
                        lastname='Einstein',
                        number=1,
                        balance='100')

    def test_account_info(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=100.0)

        self.assertEqual(account.info(), 'Number 1: Albert Einstein - 100.0 €')

    def test_account_has_funds_for(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=100.0)

        self.assertTrue(account.has_funds_for(10))
        self.assertFalse(account.has_funds_for(500))

    def test_account_has_funds_for_with_zero_balance(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=0.0)

        self.assertFalse(account.has_funds_for(10))

    def test_account_add_to_balance(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=100.0)

        account.add_to_balance(50)

        self.assertEqual(account.balance, 150.0)

    def test_account_add_to_balance_with_zero_or_negative_amount(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=100.0)

        message = 'Amount needs to be greater than 0'
        with self.assertRaisesRegex(AssertionError, message):
            account.add_to_balance(0)

        self.assertEqual(account.balance, 100.0)

        message = 'Amount needs to be greater than 0'
        with self.assertRaisesRegex(AssertionError, message):
            account.add_to_balance(-10)

        self.assertEqual(account.balance, 100.0)

    def test_account_subtract_from_balance(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=100.0)

        account.subtract_from_balance(50)

        self.assertEqual(account.balance, 50.0)

    def test_account_subtract_from_balance_with_not_enough_funds(self):
        account = app.Account(firstname='Albert',
                              lastname='Einstein',
                              number=1,
                              balance=100.0)

        message = 'Account has not enough funds'
        with self.assertRaisesRegex(AssertionError, message):
            account.subtract_from_balance(150)

        self.assertEqual(account.balance, 100.0)
