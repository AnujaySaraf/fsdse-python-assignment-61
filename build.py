def solution(list_of_nums):
    even_num = 0
    odd_num = 0
    dic_of_num = {}
    for i in list_of_nums:
        if(i % 2 == 0):
            even_num = even_num + 1
        else:
            odd_num = odd_num + 1
    dic_of_num['EVEN'] = even_num
    dic_of_num['ODD'] = odd_num
    return dic_of_num

print solution([1, 2, 3, 5, 8, 9])
