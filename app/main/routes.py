from flask import jsonify
from . import bp
from .services import process_transaction

@bp.route('/transactions', methods=['POST'])
def transaction():
    transaction_status = process_transaction()
    print(transaction_status)
    return jsonify(transaction_status), 200
