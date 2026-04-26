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

    bins[name]=fill


threshold=80

pickup=[]

for bin_id,fill in bins.items():

    if fill>=threshold:
        pickup.append(
            (bin_id,fill)
        )


pickup.sort(
key=lambda x:x[1],
reverse=True
)


print("\nPickup Priority:\n")

if len(pickup)==0:
    print("No bins require pickup")

else:

    for i,b in enumerate(
        pickup,
        1
    ):
        print(
f"{i}. Bin {b[0]} ({b[1]}%)"
)