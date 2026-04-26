current_fill = float(
input("Current fill %: ")
)

growth = float(
input(
"Estimated fill increase per hour %: "
)
)

if growth <= 0:
    print("No growth detected.")

elif current_fill >=100:
    print("Bin already full.")

else:

    hours = (
        100-current_fill
    ) / growth

    print(
f"\nPredicted overflow in {hours:.2f} hours"
)