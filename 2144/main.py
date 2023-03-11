def minimumcost(cost: list[int]) -> int:
    cost.sort(reverse=True)
    total, i, no = 0, 0, len(cost)
    while i<no:
        total += sum(cost[i:i+2])
        i+=3
    return total

print(minimumcost([1,2,3]))

#!Completed