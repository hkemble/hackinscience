def select_student(grades, cutoff):
    import operator
    accepted = []
    rejected = []
    for i in range(len(grades)):
        if grades[i][1] >= cutoff:
            accepted.append(grades[i])
        else:
            rejected.append(grades[i])
    a_sort = sorted(accepted, key=operator.itemgetter(1), reverse=True)
    r_sort = sorted(rejected, key=operator.itemgetter(1))
    return {'Accepted': a_sort, 'Refused': r_sort}
