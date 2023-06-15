import asyncio
from app.models import Transaction

async def process_transaction(transaction_id: str):
    # simulate delay with asyncio.sleep
    await asyncio.sleep(2)

    # Get the transaction from the database
    transaction = Transaction.query.get(transaction_id)

    if transaction:
        # Business logic here, e.g. process the transaction
        # ...

        return True, {'status': 'Transaction processed successfully'}
    else:
        return False, {'error': 'Transaction not found'}
