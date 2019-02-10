import unittest
import pandas as pd

import app


class TestBankInitialization(unittest.TestCase):
    def test_bank_can_be_initialized(self):
        # Initialize the Bank with the name GLS
        bank = app.Bank('GLS')

        # Assert the Bank
        self.assertTrue(type(bank) == app.Bank)
        self.assertEqual(bank.name, 'GLS')

    def test_bank_accounts_dataframe(self):
        # Initialize the Bank with the name GLS
        bank = app.Bank('GLS')

        # Expect self.accounts to be a pd.DataFrame
        self.assertEqual(type(bank.accounts), pd.DataFrame)

        # Expect self.accounts dataframe to have the following columns
        expected_columns = ['id', 'firstname', 'lastname', 'balance']
        self.assertEqual(list(bank.accounts.columns), expected_columns)

    def test_bank_transactions_dataframe(self):
        # Initialize the Bank with the name GLS
        bank = app.Bank('GLS')

        # Expect self.transactions to be a pd.DataFrame
        self.assertEqual(type(bank.transactions), pd.DataFrame)

        # Expect self.transactions dataframe to have the following columns
        expected_columns = ['id', 'sender_id', 'recipient_id', 'amount', 'subject', 'category', 'timestamp']
        self.assertEqual(list(bank.transactions.columns), expected_columns)
