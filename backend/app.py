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



if __name__=="__main__":
 app.run(
 debug=True
 )