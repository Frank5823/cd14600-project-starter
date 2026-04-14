import unittest
from transaction.transaction_factory import TransactionFactory
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestTransactionFactory(unittest.TestCase):
    """Test cases for the TransactionFactory (Factory Pattern)."""

    def test_create_income_transaction(self):
        """Test creating an income transaction using the factory."""
        txn = TransactionFactory.create_income(500)
        self.assertEqual(txn.amount, 500)
        self.assertEqual(txn.category, TransactionCategory.INCOME)
        self.assertIsInstance(txn, Transaction)

    def test_create_expense_transaction(self):
        """Test creating an expense transaction using the factory."""
        txn = TransactionFactory.create_expense(75)
        self.assertEqual(txn.amount, 75)
        self.assertEqual(txn.category, TransactionCategory.EXPENSE)
        self.assertIsInstance(txn, Transaction)

    def test_create_transaction_with_category(self):
        """Test creating a transaction with explicit category using the factory."""
        txn = TransactionFactory.create_transaction(200, TransactionCategory.INCOME)
        self.assertEqual(txn.amount, 200)
        self.assertEqual(txn.category, TransactionCategory.INCOME)

    def test_income_with_negative_amount_raises_error(self):
        """Test that negative income amounts raise ValueError."""
        with self.assertRaises(ValueError):
            TransactionFactory.create_income(-100)

    def test_income_with_zero_amount_raises_error(self):
        """Test that zero income amounts raise ValueError."""
        with self.assertRaises(ValueError):
            TransactionFactory.create_income(0)

    def test_expense_with_negative_amount_raises_error(self):
        """Test that negative expense amounts raise ValueError."""
        with self.assertRaises(ValueError):
            TransactionFactory.create_expense(-50)

    def test_expense_with_zero_amount_raises_error(self):
        """Test that zero expense amounts raise ValueError."""
        with self.assertRaises(ValueError):
            TransactionFactory.create_expense(0)

    def test_create_transaction_with_negative_amount_raises_error(self):
        """Test that negative amounts raise ValueError for generic factory method."""
        with self.assertRaises(ValueError):
            TransactionFactory.create_transaction(-100, TransactionCategory.INCOME)

    def test_factory_creates_equivalent_transactions(self):
        """Test that factory-created transactions are equivalent to direct creation."""
        factory_txn = TransactionFactory.create_income(150)
        direct_txn = Transaction(150, TransactionCategory.INCOME)
        self.assertEqual(factory_txn, direct_txn)


if __name__ == "__main__":
    unittest.main()
