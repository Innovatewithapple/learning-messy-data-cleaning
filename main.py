# Numpy practice
import numpy as np
import pandas as pd

# a = np.array([28,30,24,26])
# # print(a)
# # print(type(a))

# # # lets do math:
# # print(a+5)
# # print(a+5)

# # print("Other operations:-")
# # print(a.sum())
# # print(np.sum(a))
# # print(np.mean(a))# average
# # print(np.std(a))# deviation
# # print(np.max(a))
# # print(np.min(a))
# # print(np.percentile(a,90))


# a = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
# # print(a.shape)

# c = np.array([[1],[2],[4]])
# # print(c.shape)
# # print(c)


# #3d Array
# d = np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ])

# # print(d.ndim)
# # print(d[0,1])

# print(a[1:13:2])

# arr1 = np.array([10,20,30])
# arr2 = np.array([5,5,5])
# print(arr1+arr2)

#Loop:
a = np.array([[1, 2, 3],
              [4, 5, 6]])
a = np.array([1,2,3,4,5,6])
print(a)
result = []
for x in a:
    if x > 2:
        result.append(1)
    else:
        result.append(0)

# print(result)
print(np.where(a>2,1,0))