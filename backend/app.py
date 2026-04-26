import csv


def pickup_optimizer():

    bins = {}
    records = []

    n = int(
        input("Number of bins: ")
    )


    for i in range(n):

        name = input(
f"Bin {i+1} name: "
        ).strip()


        fill = int(
input("Fill %: ")
        )

        if fill < 0:
            fill = 0

        if fill > 100:
            fill = 100


        distance = float(
input("Distance km: ")
        )

        if distance <= 0:
            distance = 0.1


        score = fill / distance


        bins[name] = score


        records.append(
            [
             name,
             fill,
             distance,
             round(score,2)
            ]
        )



    # Save run data
    with open(
        "datasets/bin_log.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
["Bin","Fill","Distance","PriorityScore"]
        )

        writer.writerows(
            records
        )



    ranked = sorted(
        bins.items(),
        key=lambda x:x[1],
        reverse=True
    )


    print("\nOptimized Pickup Order")
    print("----------------------")

    for i,b in enumerate(
        ranked,
        1
    ):
        print(
f"{i}. {b[0]}"
        )

    print(
"\nBin data saved to datasets/bin_log.csv"
    )



def fill_prediction():

    current = float(
input("Current Fill %: ")
    )

    growth = float(
input("Growth/hour %: ")
    )


    if current >=100:
        print(
"Bin already full."
        )
        return


    if growth<=0:
        print(
"Invalid growth."
        )
        return


    hours = (
      100-current
    )/growth


    print(
f"\nPredicted overflow in {hours:.2f} hours"
    )



while True:

    print("\nSMART WASTE BACKEND")
    print("-------------------")
    print("1 Pickup Optimizer")
    print("2 Fill Prediction")
    print("3 Exit")


    choice = input(
"Choose option: "
    )


    if choice=="1":
        pickup_optimizer()

    elif choice=="2":
        fill_prediction()

    elif choice=="3":
        break

    else:
        print(
"Invalid choice"
        )