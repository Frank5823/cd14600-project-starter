"""
Factory Pattern Example and Documentation

This module demonstrates the Factory Pattern implementation for transaction creation.
The Factory Pattern provides several key benefits:

1. ENCAPSULATION: Transaction creation logic is centralized in one place
2. VALIDATION: All created objects go through consistent validation
3. FLEXIBILITY: Easy to change creation logic without affecting client code
4. CONSISTENCY: Ensures all transactions are created in a valid state

PATTERN EXPLANATION:
The Factory Pattern defines an interface for creating objects, but lets subclasses
decide which class to instantiate. In our simplified implementation, we use static
factory methods that encapsulate the creation logic.

Without Factory Pattern (CLIENT PROBLEM):
    # Client code must know how to create valid transactions
    # Client code must validate inputs
    # Changes to creation logic require changes everywhere
    
    transaction = Transaction(100, TransactionCategory.INCOME)  # What if amount is invalid?
    
With Factory Pattern (CLEAN SOLUTION):
    # Factory handles all creation details
    # Single point of control for validation
    # Easy to extend without breaking client code
    
    transaction = TransactionFactory.create_income(100)  # Let factory handle details
"""

from transaction.transaction_factory import TransactionFactory
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from balance.balance import Balance
from balance.balance_observer import PrintObserver


def example_1_basic_usage():
    """Example 1: Basic factory method usage."""
    print("=" * 60)
    print("EXAMPLE 1: Basic Factory Method Usage")
    print("=" * 60)
    
    # Using factory to create income transaction
    income = TransactionFactory.create_income(500)
    print(f"Created income transaction: {income}")
    
    # Using factory to create expense transaction
    expense = TransactionFactory.create_expense(75)
    print(f"Created expense transaction: {expense}")
    
    print()


def example_2_validation():
    """Example 2: Factory validation prevents invalid transactions."""
    print("=" * 60)
    print("EXAMPLE 2: Factory Validation")
    print("=" * 60)
    
    # Try to create invalid transactions
    test_cases = [
        ("Positive income", 100, "income"),
        ("Zero amount", 0, "income"),
        ("Negative amount", -50, "expense"),
    ]
    
    for description, amount, txn_type in test_cases:
        try:
            if txn_type == "income":
                txn = TransactionFactory.create_income(amount)
                print(f"✓ {description}: Successfully created {txn}")
            else:
                txn = TransactionFactory.create_expense(amount)
                print(f"✓ {description}: Successfully created {txn}")
        except ValueError as e:
            print(f"✗ {description}: {e}")
    
    print()


def example_3_with_balance():
    """Example 3: Using factory with Balance singleton."""
    print("=" * 60)
    print("EXAMPLE 3: Factory Pattern with Balance Singleton")
    print("=" * 60)
    
    # Reset balance
    balance = Balance.get_instance()
    balance.reset()
    
    # Register observer
    print_observer = PrintObserver()
    balance.register_observer(print_observer)
    
    # Create and apply transactions using factory
    transactions = [
        ("Freelance income", TransactionFactory.create_income(1000)),
        ("Grocery shopping", TransactionFactory.create_expense(80)),
        ("Project payment", TransactionFactory.create_income(500)),
        ("Utility bill", TransactionFactory.create_expense(120)),
    ]
    
    print("Applying transactions created by factory:\n")
    for description, txn in transactions:
        print(f"[{description}]")
        balance.apply_transaction(txn)
        print()
    
    print()


def example_4_factory_extends_adapter():
    """Example 4: Factory pattern complements Adapter pattern."""
    print("=" * 60)
    print("EXAMPLE 4: Factory + Adapter Pattern Integration")
    print("=" * 60)
    
    from transaction.external_income_transaction import ExternalFreelanceIncome
    from transaction.transaction_adapter import TransactionAdapter
    
    print("Processing external freelance income through Adapter to Transaction:")
    
    # Create external transaction
    external = ExternalFreelanceIncome(750, "INV-2024-001", "Mobile app development")
    print(f"External source: {external.description} (Invoice: {external.invoice_id})")
    
    # Adapt external transaction
    adapted = TransactionAdapter(external).to_transaction()
    print(f"Adapted to: {adapted}")
    
    print("\nAlternatively, you could create a similar transaction directly with factory:")
    factory_created = TransactionFactory.create_income(750)
    print(f"Factory created: {factory_created}")
    
    print(f"Both are equivalent: {adapted == factory_created}")
    
    print()


def example_5_comparison():
    """Example 5: Compare factory approach vs direct instantiation."""
    print("=" * 60)
    print("EXAMPLE 5: Factory vs Direct Instantiation Comparison")
    print("=" * 60)
    
    print("❌ WITHOUT FACTORY (Direct instantiation):")
    print("   # Requires knowing implementation details")
    print("   # No validation")
    print("   txn = Transaction(100, TransactionCategory.INCOME)")
    print()
    
    print("✓ WITH FACTORY (Using static factory methods):")
    print("   # Clear intent through method name")
    print("   # Built-in validation for positive amounts")
    print("   # Easy to extend with business rules")
    print("   txn = TransactionFactory.create_income(100)")
    print()
    
    # Demonstrate the difference
    valid_txn = TransactionFactory.create_income(100)
    print(f"Created valid transaction: {valid_txn}")
    
    print()


if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "FACTORY PATTERN DEMONSTRATION" + " " * 20 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    example_1_basic_usage()
    example_2_validation()
    example_3_with_balance()
    example_4_factory_extends_adapter()
    example_5_comparison()
    
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Factory methods provide a clean API for object creation")
    print("2. Validation is centralized and consistent")
    print("3. Changes to creation logic don't affect client code")
    print("4. Code is more maintainable and easier to test")
    print("5. Factory Pattern complements other patterns (Adapter, Singleton)")
    print()
