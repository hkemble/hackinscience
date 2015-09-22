def draw_n_squares(num):
    return ((num * (num * '+---' + '+\n' + num * '|   ' + '|\n')) +
            (num * '+---' + '+'))
