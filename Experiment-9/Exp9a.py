import numpy as ok

arr = ok.array([101, 820, 330, 540, 950, 583, 249, 466, 603, 713])

arr[[2,5,8]] = 99
sorted_arr = ok.sort(arr)

print(sorted_arr)


print("Array:",arr)
print("Minimum :", min(arr))
print("Maximun:", max(arr))
print("Accessing Element :",arr[1:5])
print("Sum", sum(sorted_arr))




a = ok.array(
    [
        ('JAIN1', 2, 21.0),
        ('JAIN3', 7, 39.0),
        ('JAIN2', 7, 29.0)
    ],
    dtype=[
        ('name', ok.str_, 10),
        ('age', ok.int32),
        ('weight', ok.float64)
    ]
)


#sorting 

