from flask import Flask,jsonify

app=Flask(__name__)

bin_data={
"bin_id":"BIN01",
"fill":62,
"status":"NORMAL"
}

@app.route('/')
def home():
    return "Smart Waste API Running"

@app.route('/bin-status')
def status():
    return jsonify(bin_data)

@app.route('/health')
def health():
    return jsonify({"status":"ok"})

if __name__=='__main__':
    app.run(debug=True)