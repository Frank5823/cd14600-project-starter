# transaction_factory.py
"""
Factory Pattern Implementation for Transaction Creation.

The TransactionFactory provides a centralized, reusable way to create Transaction
objects without exposing the creation logic to the client. This ensures consistent
transaction creation and makes it easier to modify transaction creation behavior
in the future without changing client code.

Benefits:
- Encapsulates transaction creation logic
- Ensures valid transactions are created
- Simplifies client code
- Makes it easy to extend with new transaction types
"""

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TransactionFactory:
    """
    Factory for creating Transaction objects.

    This class uses the Factory Pattern to centralize the creation of transactions.
    Instead of clients directly instantiating Transaction objects, they use factory
    methods that ensure proper transaction creation.
    """

    @staticmethod
    def create_income(amount):
        """
        Create an Income transaction.

        Args:
            amount (float): The income amount.

        Returns:
            Transaction: A transaction with INCOME category.

        Raises:
            ValueError: If amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError(f"Income amount must be positive, got {amount}")
        return Transaction(amount, TransactionCategory.INCOME)

    @staticmethod
    def create_expense(amount):
        """
        Create an Expense transaction.

        Args:
            amount (float): The expense amount.

        Returns:
            Transaction: A transaction with EXPENSE category.

        Raises:
            ValueError: If amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError(f"Expense amount must be positive, got {amount}")
        return Transaction(amount, TransactionCategory.EXPENSE)

    @staticmethod
    def create_transaction(amount, category):
        """
        Create a Transaction with explicit category.

        This is a generic factory method for creating transactions. For specific
        transaction types, prefer create_income() or create_expense() for better
        type safety.

        Args:
            amount (float): The transaction amount.
            category (TransactionCategory): The transaction category.

        Returns:
            Transaction: A transaction with the specified amount and category.

        Raises:
            ValueError: If amount is negative or zero, or category is invalid.
        """
        if amount <= 0:
            raise ValueError(f"Transaction amount must be positive, got {amount}")
        if category not in TransactionCategory:
            raise ValueError(f"Invalid transaction category: {category}")
        return Transaction(amount, category)
