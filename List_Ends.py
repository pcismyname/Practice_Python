def First_Last(arr):
    for i in range(0,len(arr)):
        if i==0 or i == len(arr)-1:
            print(arr[i])

"""def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]] """


a = [1,2,3,4,100,8,2,1,1,5,1,100,41]

First_Last(a)


    