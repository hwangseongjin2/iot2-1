def sum_avg(*scores):
    sum=0
    avg=0
    count=0
    for arg in scores:
        sum = sum+arg
        count = count + 1

    avg=sum/count
    return(sum, avg)

ret_sum=0
ret_avg=0

ret_sum, ret_avg = sum_avg(30,40,80,90)
print("sum=", ret_sum, "avg=", ret_avg)

ret_sum, ret_avg = sum_avg(30,40,80)
print("sum=", ret_sum, "avg=", ret_avg)