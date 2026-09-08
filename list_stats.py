def list_stats(numbers):
    count=0
    total=0
    small = None 
    big = None
    if not numbers:
        print("error")
        return 0, 0, None, None, None
    else:
        for n in numbers:
            count+=1
            total+=n
            if small is None or small > n:
                small = n
            if big is None or big< n:
                big = n
        average=total/count
        return count,total,average,small,big
print(list_stats([]))