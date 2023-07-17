def series_sum(n):
    return "{:.2f}".format(sum([1/(1 + 3*i) for i in range(n)]))

##The seoncod solution
# def series_sum(n):
#     a = 0
#     l = [a + 1/(1 + 3*i) for i in range(0, n)]
#     return "{:.2f}".format(sum(l))


##THe first solution
# def series_sum(n):
#     a = 0
#     for i in range(0, n):
#         a = a + 1/(1 + 3*i)
#     return "{:.2f}".format(a)