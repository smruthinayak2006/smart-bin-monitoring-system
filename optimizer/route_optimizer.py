bins = {
"A":95,
"B":42,
"C":87,
"D":20
}

threshold = 80

full_bins=[]

for bin_id,fill in bins.items():

    if fill>=threshold:
        full_bins.append(
            (bin_id,fill)
        )

full_bins.sort(
key=lambda x:x[1],
reverse=True
)

print("\nPickup Priority:\n")

for i,bin_data in enumerate(full_bins,1):
    print(
f"{i}. Bin {bin_data[0]} ({bin_data[1]}%)"
)