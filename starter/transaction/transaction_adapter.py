# transaction_adapter.py

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

class TransactionAdapter:
    def __init__(self, external_transaction):
        self.external_transaction = external_transaction

    def to_transaction(self):
        """Convert an external transaction to a standard Transaction."""
        # Check if it's an ExternalFreelanceIncome (which is always income)
        if hasattr(self.external_transaction, 'typ') and self.external_transaction.typ == "income":
            return Transaction(self.external_transaction.amount, TransactionCategory.INCOME)
        # For future extensibility, could handle other external transaction types
        # For now, assume all external transactions are income
        return Transaction(self.external_transaction.amount, TransactionCategory.INCOME)
