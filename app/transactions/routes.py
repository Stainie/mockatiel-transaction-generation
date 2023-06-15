from flask import jsonify, request
from app.transactions import bp
from app.transactions.services import process_transaction

@bp.route('/mock', methods=['POST'])
async def mock_transaction():
    data = request.get_json()
    # here we just suppose that the data sent by the user contains a key "transaction_id"
    transaction_id = data['transaction_id'] 
    success, response = await process_transaction(transaction_id)
    if success:
        return jsonify(response), 200
    else:
        return jsonify(response), 400
