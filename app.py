from flask import Flask, jsonify, request

app = Flask(__name__)

RULES = {
	"hours" : "We are open from 6am to 11 pm every day. ",
	"price" : "Our monthly membership costs $49.",
	"location" : "We are located downtown near the main square,",
	"contact" : "You can contact us at 555-1234."}
def get_rule_based_reply(message: str) ->str:
	message= message.lower()

	for keyword, reply in RULES.items():
		if keyword in message:
			return reply
	return "sorry, i did not understand, Can you rephrase?"

@app.route("/")
def home():
	return "Rule-based chatbot is running."

@app.route("/api/chat", methods=["POST"])
def chat():
	data = request.json
	if not data or "message" not in data:
		return jsonify({"error": message is required}), 400
	user_message= data["message"]
	reply = get_rule_based_reply(user_message)
	return jsonify({"reply" : reply})
if __name__ == "__main__":
	app.run(debug= True)
