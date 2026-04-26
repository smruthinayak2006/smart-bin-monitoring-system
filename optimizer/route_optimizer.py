bins={}

n=int(
input("Number of bins: ")
)

for i in range(n):

    name=input(
f"Bin {i+1} name: "
)

    fill=int(
input("Fill percentage: ")
)

    distance=float(
input("Distance from depot (km): ")
)

    bins[name]={
        "fill":fill,
        "distance":distance
    }


threshold=80

pickup=[]


for name,data in bins.items():

    if data["fill"]>=threshold:

        pickup.append(
            (
             name,
             data["fill"],
             data["distance"]
            )
        )


# Sort by highest fill first
pickup.sort(
key=lambda x:x[1],
reverse=True
)


print("\nPickup Priority")
print("----------------")

for i,b in enumerate(
pickup,
1
):
 print(
f"{i}. {b[0]} Fill:{b[1]}%"
 )


# Route suggestion
route=sorted(
pickup,
key=lambda x:x[2]
)

print("\nSuggested Route")
print("----------------")

for stop in route:
    print(
f"{stop[0]} ({stop[2]} km)"
)