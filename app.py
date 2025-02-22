from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Mock database schema (replace with real schema if needed)
DATABASE_SCHEMA = {
    "users": ["id", "name", "email"],
    "orders": ["id", "user_id", "amount", "date"],
    "products": ["id", "name", "price", "category"]
}

@app.route("/process_query", methods=["POST"])
def process_query():
    data = request.get_json()
    user_query = data.get("query", "").lower()

    # Simple logic to match tables based on keywords in the query
    relevant_tables = [table for table in DATABASE_SCHEMA if any(word in user_query for word in table.split("_"))]

    # If no match, return a random table as a fallback
    if not relevant_tables:
        relevant_tables = [random.choice(list(DATABASE_SCHEMA.keys()))]

    return jsonify({"selected_tables": relevant_tables, "schema": {t: DATABASE_SCHEMA[t] for t in relevant_tables}})

if __name__ == "__main__":
    app.run(debug=True)
