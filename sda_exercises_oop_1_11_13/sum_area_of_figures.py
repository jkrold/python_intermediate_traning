def sum_area_of_figures(figure_list: list) -> float:
    summed_area: float = 0
    for figure in figure_list:
        summed_area += figure.get_area()
    return round(summed_area, 2)
