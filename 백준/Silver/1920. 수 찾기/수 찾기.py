n = int(input())
a = list(map(int,input().split()))
m = int(input())
x_list = list(map(int, input().split()))

a.sort()
for x in x_list:
    answer = 0
    
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] > x:
            if right != mid:
                right = mid
            else:
                if a[left] == x:
                    answer = 1
                right = -1
            continue
        
        if a[mid] < x:
            if left != mid:
                left = mid
            else:
                if a[right] == x:
                    answer = 1
                right = -1
            continue
        answer = 1
        right = -1
    print(answer)