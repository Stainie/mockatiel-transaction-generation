from flask import jsonify
from . import bp
from .services import process_transaction

@bp.route('/transaction', methods=['POST'])
async def transaction():
    transaction_status = await process_transaction()
    return jsonify({'status': transaction_status})
