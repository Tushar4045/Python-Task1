#For  space separated values of arr
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique_scores = list(set(arr))

    unique_scores.remove(max(unique_scores))

    runner_up_score = max(unique_scores)

    print(runner_up_score)



#if we want to input the the values without sapce separated in arr we can use this but it will work only from 0 to 9
#  n = int(input())
# arr = int(input())

# arr_l = [int(i) for i in str(arr)]
# print(arr_l)
# uni_sc = list(set(arr_l))
# print(uni_sc)
# max_sc = max(uni_sc)
# print(max_sc)
# uni_sc.remove(max_sc)
# print(uni_sc)
# run_sc = max(uni_sc)
# print(run_sc)