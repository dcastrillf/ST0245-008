answer1 = []

nugg = int(input('Cuantos nuggets desea comprar: '))


def min_cantidad(nuggets):
    curr_answer = [0] * 3
    if nuggets >= 20:
        curr_answer[0] = nuggets // 20
        nuggets = nuggets - (curr_answer[0] * 20)
    if nuggets >= 9:
        curr_answer[1] = nuggets // 9
        nuggets = nuggets - (curr_answer[1] * 9)
    if nuggets >= 6:
        curr_answer[2] = nuggets // 6
        nuggets = nuggets - (curr_answer[2] * 6)
    return curr_answer


print(min_cantidad(nugg))