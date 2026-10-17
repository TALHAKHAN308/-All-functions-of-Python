print("=" * 30)
print("number analyzer")
print("=" * 30)

total = 0
even = 0
odd = 0

for i in range(1,11):
    total = total + i
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
        print(f"number {i:2} | total: {total:3}")

        print("=" * 30)
        print(f"even number: {even}")
        print(f"odd number: {odd}")
        print(f"final total : {total}")