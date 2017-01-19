# not memory efficient
[i*j for i in range(1,10) for j in range(1,10)]

#memory efficient
(i*j for i in range(1,10) for j in range(1,10))
