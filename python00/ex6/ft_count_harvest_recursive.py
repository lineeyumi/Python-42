def ft_aux_recursive(harvest: int, days: int) -> None:
    if harvest > days:
        print("Harvest time")
        return
    print(f"Day {harvest}")
    ft_aux_recursive(harvest + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    if days <= 0:
        print("Harvest time!")
        return
    ft_aux_recursive(1, days)
