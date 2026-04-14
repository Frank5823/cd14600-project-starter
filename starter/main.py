"""This module serves as the entry point for the program."""
from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer import PrintObserver
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome


def main():
    print("=" * 70)
    print("🏦 FINANCIAL TRANSACTION SYSTEM - Live Simulation")
    print("=" * 70)
    print()

    # Initialize the balance system (Singleton Pattern)
    print("🔄 Initializing Balance System (Singleton Pattern)...")
    balance = Balance.get_instance()
    balance.reset()
    print(f"   ✓ Balance reset to: ${balance.get_balance():.2f}")
    print()

    # Set up observers (Observer Pattern)
    print("👀 Setting up Observers (Observer Pattern)...")
    print_observer = PrintObserver()
    low_balance_observer = LowBalanceAlertObserver(threshold=100)

    balance.register_observer(print_observer)
    balance.register_observer(low_balance_observer)
    print("   ✓ PrintObserver: Will display transaction details")
    print("   ✓ LowBalanceAlertObserver: Will alert when balance < $100")
    print()

    # Create transactions using different methods
    print("💰 Creating Transactions...")

    # Standard transactions (Direct creation)
    print("   📝 Standard transactions (Direct creation):")
    transactions = [
        Transaction(100, TransactionCategory.INCOME),   # Initial deposit
        Transaction(50, TransactionCategory.EXPENSE),   # Grocery shopping
        Transaction(200, TransactionCategory.INCOME),   # Salary payment
        Transaction(75, TransactionCategory.EXPENSE),   # Utility bill
    ]

    for i, txn in enumerate(transactions, 1):
        if txn.category == TransactionCategory.INCOME:
            print(f"      {i}. Income: +${txn.amount}")
        else:
            print(f"      {i}. Expense: -${txn.amount}")

    # External transaction via Adapter Pattern
    print("   🔄 External transaction (Adapter Pattern):")
    freelance_income = ExternalFreelanceIncome(1200, "INV-98765", "Mobile App Project")
    print(f"      External source: {freelance_income.description}")
    print(f"      Invoice: {freelance_income.invoice_id}")
    print(f"      Amount: ${freelance_income.amount}")

    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()
    print(f"      ✓ Adapted to: {adapted_transaction}")
    print()

    # Combine all transactions
    all_transactions = transactions + [adapted_transaction]

    # Process transactions
    print("⚡ Processing Transactions...")
    print("-" * 70)

    for i, transaction in enumerate(all_transactions, 1):
        if transaction.category == TransactionCategory.INCOME:
            txn_type = "💰 INCOME"
            amount_str = f"+${transaction.amount}"
        else:
            txn_type = "💸 EXPENSE"
            amount_str = f"-${transaction.amount}"

        print(f"Transaction {i}: {txn_type} {amount_str}")
        balance.apply_transaction(transaction)
        print()

    # Final summary
    print("=" * 70)
    print("📊 FINAL SUMMARY")
    print("=" * 70)
    final_balance = balance.get_balance()
    print(f"💰 Final Balance: ${final_balance:.2f}")

    # Analyze the transaction history
    total_income = sum(t.amount for t in all_transactions
                       if t.category == TransactionCategory.INCOME)
    total_expenses = sum(t.amount for t in all_transactions
                         if t.category == TransactionCategory.EXPENSE)
    net_flow = total_income - total_expenses

    print(f"📈 Total Income: ${total_income:.2f}")
    print(f"📉 Total Expenses: ${total_expenses:.2f}")
    print(f"⚖️  Net Flow: ${net_flow:.2f}")
    print(f"📊 Transaction Count: {len(all_transactions)}")

    # Design pattern demonstration
    print()
    print("🎯 DESIGN PATTERNS DEMONSTRATED:")
    print("   • Singleton Pattern: One Balance instance manages all state")
    print("   • Observer Pattern: Automatic notifications for balance changes")
    print("   • Adapter Pattern: External data seamlessly integrated")
    print("   • Factory Pattern: Transaction creation (used in tests)")

    if final_balance >= 0:
        print(f"✅ Account Status: HEALTHY (Balance: ${final_balance:.2f})")
    else:
        print(f"⚠️  Account Status: OVERDRAWN (Balance: ${final_balance:.2f})")

    print()
    print("🏁 Simulation Complete!")


if __name__ == "__main__":
    main()
