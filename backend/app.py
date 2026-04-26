def pickup_optimizer():

    bins = {}

    n = int(input("Number of bins: "))

    for i in range(n):

        name = input(
            f"Bin {i+1} name: "
        )

        fill = int(
            input("Fill %: ")
        )

        distance = float(
            input("Distance km: ")
        )

        if distance <= 0:
            distance = 0.1

        score = fill / distance

        bins[name] = score


    ranked = sorted(
        bins.items(),
        key=lambda x:x[1],
        reverse=True
    )

    print("\nOptimized Pickup Order\n")

    for i,b in enumerate(
        ranked,
       1
    ):
        print(
f"{i}. {b[0]}"
        )


def fill_prediction():

    current = float(
        input("Current Fill %: ")
    )

    growth = float(
        input("Growth/hour %: ")
    )

    if growth <= 0:
        print("Invalid growth")
        return

    hours = (
        100-current
    ) / growth


    print(
f"Overflow in {hours:.2f} hours"
)


while True:

    print("\nSMART WASTE BACKEND")
    print("1 Pickup Optimizer")
    print("2 Fill Prediction")
    print("3 Exit")

    choice=input(
        "Choose option: "
    )

    if choice=="1":
        pickup_optimizer()

    elif choice=="2":
        fill_prediction()

    elif choice=="3":
        break

    else:
        print("Invalid choice")