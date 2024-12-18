from flask import Flask, request, jsonify
from calendar_manager import CalendarManager

app = Flask(__name__)
calendar_manager = CalendarManager()

@app.route("/api/add-event", methods=["POST"])
def add_event():
    try:
        data = request.json
        calendar_manager.add_event(
            summary=data['summary'],
            location=data.get('location', ''),
            description=data.get('description', ''),
            start_time=data['start_time'],
            end_time=data['end_time']
        )
        return jsonify({"message": "Randevu başarıyla oluşturuldu!"}), 200
    except Exception as e:
        return jsonify({"message": "Bir hata oluştu.", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
