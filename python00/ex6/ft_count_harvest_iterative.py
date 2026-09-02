def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    harvest = 1
    while harvest <= days:
        print(f"Day {harvest}")
        harvest += 1
    print("Harvest time!")
