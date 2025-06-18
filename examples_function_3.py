sum=0
avg=0

def sum_avg(*scores):
    count=0
    global sum
    for arg in scores:
        sum +=arg
        count+=1

    global avg
    avg = sum/count


sum=0
sum_avg(30,40,80,90)
print("sum=", sum, ",avg=", avg)

sum=0
sum_avg(30,40,80)
print("sum=", sum, ",avg=", avg)