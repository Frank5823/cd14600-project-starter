from balance.balance import Balance
from balance.balance_observer import PrintObserver, LowBalanceAlertObserver
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

# Get singleton balance instance
balance = Balance.get_instance()
balance.reset()

# Create and register observers
print_observer = PrintObserver()
low_balance_observer = LowBalanceAlertObserver(threshold=50)

balance.register_observer(print_observer)
balance.register_observer(low_balance_observer)

print('=== Applying Transactions with Observers ===\n')

# Apply transactions
print('Transaction 1: Income of 100')
balance.apply_transaction(Transaction(100, TransactionCategory.INCOME))

print('\n' + '='*50 + '\n')
print('Transaction 2: Expense of 60')
balance.apply_transaction(Transaction(60, TransactionCategory.EXPENSE))

print('\n' + '='*50 + '\n')
print('Transaction 3: Expense of 40 (triggers low balance alert)')
balance.apply_transaction(Transaction(40, TransactionCategory.EXPENSE))

print('\n' + '='*50 + '\n')
print('Transaction 4: Income of 100 (clears alert)')
balance.apply_transaction(Transaction(100, TransactionCategory.INCOME))
