from flask import jsonify
from . import bp
from .services import process_transaction

@bp.route('/transaction', methods=['POST'])
def transaction():
    transaction_status = process_transaction()
    return jsonify({'status': transaction_status}), 200
