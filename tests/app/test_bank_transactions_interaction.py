import unittest
import datetime

import app


class TestBankInitialization(unittest.TestCase):
    def test_add_transaction(self):
        bank = app.Bank('GLS')

        bank.open_account(account_id=1,
                          firstname='Albert',
                          lastname='Einstein',
                          balance=100.)

        bank.open_account(account_id=2,
                          firstname='Paul',
                          lastname='Ehrenfest',
                          balance=55.5)

        timestamp = datetime.datetime.utcnow()
        bank.add_transaction(transaction_id=1,
                             sender_id=1,
                             recipient_id=2,
                             subject='Mein Weltbild',
                             amount=100.0,
                             category='Bücher',
                             timestamp=timestamp)

        # Expect self.transactions to have 1 row (a length of 1)
        self.assertEqual(len(bank.transactions), 1)

        # Expect self.transactions first row to have the right values
        self.assertEqual(list(bank.transactions.iloc[0]), [1, 1, 2, 100.0, 'Mein Weltbild', 'Bücher', timestamp])

    def test_add_transaction_with_zero_or_negative_amount(self):
        bank = app.Bank('GLS')

        bank.open_account(account_id=1,
                          firstname='Albert',
                          lastname='Einstein',
                          balance=100.)

        bank.open_account(account_id=2,
                          firstname='Paul',
                          lastname='Ehrenfest',
                          balance=55.5)

        message = 'Amount needs to be greater than 0'
        with self.assertRaisesRegex(AssertionError, message):
            bank.add_transaction(transaction_id=1,
                                 sender_id=1,
                                 recipient_id=2,
                                 subject='Mein Weltbild',
                                 amount=0.0,
                                 category='Bücher',
                                 timestamp=datetime.datetime.utcnow())

        message = 'Amount needs to be greater than 0'
        with self.assertRaisesRegex(AssertionError, message):
            bank.add_transaction(transaction_id=1,
                                 sender_id=1,
                                 recipient_id=2,
                                 subject='Mein Weltbild',
                                 amount=-100.0,
                                 category='Bücher',
                                 timestamp=datetime.datetime.utcnow())

        # No transaction is saved
        self.assertEqual(len(bank.transactions), 0)

    def test_add_transaction_with_invalid_sender(self):
        bank = app.Bank('GLS')

        # Just the account
        bank.open_account(account_id=2,
                          firstname='Paul',
                          lastname='Ehrenfest',
                          balance=55.5)

        message = 'Sender has no account yet!'
        with self.assertRaisesRegex(AssertionError, message):
            bank.add_transaction(transaction_id=1,
                                 sender_id=1,
                                 recipient_id=2,
                                 subject='Mein Weltbild',
                                 amount=100.0,
                                 category='Bücher',
                                 timestamp=datetime.datetime.utcnow())

        # No transaction is saved
        self.assertEqual(len(bank.transactions), 0)

    def test_add_transaction_with_invalid_recipient(self):
        bank = app.Bank('GLS')

        bank.open_account(account_id=1,
                          firstname='Albert',
                          lastname='Einstein',
                          balance=100.)

        message = 'Recipient has no account yet!'
        with self.assertRaisesRegex(AssertionError, message):
            bank.add_transaction(transaction_id=1,
                                 sender_id=1,
                                 recipient_id=2,
                                 subject='Mein Weltbild',
                                 amount=100.0,
                                 category='Bücher',
                                 timestamp=datetime.datetime.utcnow())

        # No transaction is saved
        self.assertEqual(len(bank.transactions), 0)
