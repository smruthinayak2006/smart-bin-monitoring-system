from flask import Flask,jsonify

app=Flask(__name__)


bins=[
{
"id":"A",
"fill":95,
"distance":5
},

{
"id":"B",
"fill":82,
"distance":1
},

{
"id":"C",
"fill":90,
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

    html = """
    <html>
    <head>
    <title>Smart Waste Dashboard</title>
    </head>

    <body>
    <h1>Smart Waste Dashboard</h1>

    <table border="1" cellpadding="10">
      <tr>
       <th>Bin</th>
       <th>Fill %</th>
       <th>Status</th>
      </tr>

      <tr>
       <td>A</td>
       <td>95</td>
       <td>OVERFLOW</td>
      </tr>

      <tr>
       <td>B</td>
       <td>82</td>
       <td>FULL</td>
      </tr>

      <tr>
       <td>C</td>
       <td>90</td>
       <td>FULL</td>
      </tr>

    </table>

    </body>
    </html>
    """

    return html 

if __name__=="__main__":
 app.run(
 debug=True
 )
