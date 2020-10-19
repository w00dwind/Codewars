'''
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
'''


def create_phone_number(n):
    frm = ''.join([str(elem) for elem in n])
    res = str('('+ frm[:3]+') '+ frm[3:6]+ '-'+frm[6:])
    return res


# from genius with loveщв
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
