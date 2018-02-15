total = 0
for idx,num in enumerate(range(1,51)):
    total += num
    if total > 100:
        print(total, "the sum exceeded total value 100")
        break
