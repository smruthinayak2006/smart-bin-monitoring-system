from flask import Flask,jsonify

app=Flask(__name__)


bins=[
{
"id":"A",
"fill":50,
"distance":5
},

{
"id":"B",
"fill":60,
"distance":1
},

{
"id":"C",
"fill":99,
"distance":4
}
]


@app.route("/")
def home():

    return "Smart Waste Backend API Running"



@app.route("/bins")
def get_bins():

    return jsonify(
        bins
    )



@app.route("/pickup-priority")
def priority():

    ranked=sorted(
        bins,
        key=lambda x:
        x["fill"]/x["distance"],
        reverse=True
    )

    return jsonify(
        ranked
    )



@app.route("/predict/<int:fill>/<int:growth>")
def predict(
fill,
growth
):

    if growth<=0:
        return jsonify(
{"error":"invalid growth"}
        )

    hours=(
      100-fill
    )/growth

    return jsonify(
{
"overflow_in_hours":
round(hours,2)
}
    )

@app.route("/dashboard")
def dashboard():

    rows=""

    for b in bins:

        if b["fill"]>=95:
            status="OVERFLOW"

        elif b["fill"]>=80:
            status="FULL"

        else:
            status="NORMAL"


        rows += f"""
        <tr>
         <td>{b['id']}</td>
         <td>{b['fill']}</td>
         <td>{status}</td>
        </tr>
        """


    html=f"""
    <html>
    <body>

    <h1>Smart Waste Dashboard</h1>

    <table border='1' cellpadding='12' style='border-collapse:collapse;'>

    <tr>
    <th>Bin ID</th>
    <th>Fill %</th>
    <th>Status</th>
    </tr>

    {rows}

    </table>

    </body>
    </html>
    """

    return html 

@app.route("/anomaly-check/<int:fill>")
def anomaly(fill):

    if fill < 0 or fill > 100:
        return {
          "status":"anomaly",
          "reason":"invalid sensor reading"
        }

    elif fill > 98:
        return {
         "status":"warning",
         "reason":"possible overflow"
        }

    else:
        return {
         "status":"normal"
        }

if __name__=="__main__":
 app.run(
 debug=True
 )
