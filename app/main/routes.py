from flask import jsonify
from . import main
from .services import process_transaction

@main.route('/transaction', methods=['POST'])
async def transaction():
    transaction_status = await process_transaction()
    return jsonify({'status': transaction_status})
