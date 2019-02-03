import unittest
import app


class TestTransaction(unittest.TestCase):
    def test_transaction_can_be_initialized(self):
        transaction = app.Transaction(sender=1,
                                      recipient=2,
                                      subject='Test transaction',
                                      amount=10.0)
        self.assertTrue(type(transaction) == app.Transaction)
        self.assertEqual(transaction.sender, 1)
        self.assertEqual(transaction.recipient, 2)
        self.assertEqual(transaction.subject, 'Test transaction')
        self.assertEqual(transaction.amount, 10.0)

    def test_transaction_init_sender_needs_to_be_an_integer(self):
        message = 'Sender needs to be an integer'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender=1.0,
                            recipient=2,
                            subject='Test transaction',
                            amount=10.0)

        message = 'Sender needs to be an integer'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender='1',
                            recipient=2,
                            subject='Test transaction',
                            amount=10.0)

    def test_transaction_init_recipient_needs_to_be_an_integer(self):
        message = 'Recipient needs to be an integer'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender=1,
                            recipient=2.0,
                            subject='Test transaction',
                            amount=10.0)

        message = 'Recipient needs to be an integer'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender=1,
                            recipient='2',
                            subject='Test transaction',
                            amount=10.0)

    def test_transaction_init_amount_needs_to_be_a_float(self):
        message = 'Amount needs to be a float'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender=1,
                            recipient=2,
                            subject='Test transaction',
                            amount=10)

        message = 'Amount needs to be a float'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender=1,
                            recipient=2,
                            subject='Test transaction',
                            amount='10')

    def test_transaction_init_amount_needs_to_be_greater_than_zero(self):
        message = 'Amount needs to be greater than 0'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender=1,
                            recipient=2,
                            subject='Test transaction',
                            amount=0.0)

        message = 'Amount needs to be greater than 0'
        with self.assertRaisesRegex(AssertionError, message):
            app.Transaction(sender=1,
                            recipient=2,
                            subject='Test transaction',
                            amount=-10.0)

    def test_transaction_info(self):
        transaction = app.Transaction(sender=1,
                                      recipient=2,
                                      subject='Test transaction',
                                      amount=10.0)

        self.assertEqual(transaction.info(),
                         'From 1 to 2: Test transaction - 10.0 €')
