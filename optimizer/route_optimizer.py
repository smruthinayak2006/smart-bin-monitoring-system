bins = {}

n = int(input("Number of bins: "))

for i in range(n):

    name = input(
        f"Bin {i+1} name: "
    )

    fill = int(
        input("Fill percentage: ")
    )

    distance = float(
        input("Distance from depot (km): ")
    )

    if distance <= 0:
        distance = 0.1

    bins[name] = {
        "fill": fill,
        "distance": distance
    }


threshold = 80
pickup = []


for name,data in bins.items():

    if data["fill"] >= threshold:

        score = (
            data["fill"] /
            data["distance"]
        )

        pickup.append(
            (
                name,
                data["fill"],
                data["distance"],
                score
            )
        )


pickup.sort(
    key=lambda x:x[3],
    reverse=True
)


print("\nOptimized Pickup Route")
print("---------------------")


for i,b in enumerate(
    pickup,
    1
):
    print(
f"{i}. {b[0]} | Fill:{b[1]}% | Distance:{b[2]} km | Score:{b[3]:.2f}"
)