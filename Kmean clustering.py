from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy

input_matrix=numpy.array([
               [17,17,2],
               [50,31,3],
               [11,9,4],
               [35,23,3],
               [25,21,2],
               [75,33,3]
               ])
distance_matrix=numpy.array([])
Euclidean_distance_matrix=numpy.array([])

print('''
###############
#distance_matrix
#        a               b            c             ...
#
#a    [0, 0, 0]     [33, 14,  1]    [6, 8, 2]
#
#b     ...             ...            ...           ...
#.
#.
#.
###############
''')
for i in input_matrix:
    print("calculate distance form", i," to others:")
    for j in input_matrix:
        print("to", j,"=",abs(i-j))
        distance_matrix=numpy.append(distance_matrix,abs(i-j))
    print("_____")



distance_matrix=distance_matrix.reshape(len(input_matrix),len(input_matrix),
                                        len(input_matrix[0]))
print("distance_matrix=")
print(distance_matrix)


print('''
###############
#Euclidean_distance_matrix
#        a               b            c             ...
#
#a    [0+0+0]        [33+14+1]     [6+8+2]
#
#b     ...             ...            ...           ...
#.
#.
#.
###############

''')

for i in range(len(input_matrix)):
    for j in range(len(input_matrix)):
        Euclidean_distance_matrix=numpy.append(Euclidean_distance_matrix,distance_matrix[i][j].sum())		

Euclidean_distance_matrix=Euclidean_distance_matrix.reshape(len(input_matrix),len(input_matrix))
print("Euclidean_distance_matrix")
print(Euclidean_distance_matrix)


print('''
###############
#
#
#
#the best number of cluster 
#by silhouette_score
#
#
###############

''')
the_best_K=int()
silhouette_avg=list()
range_n_clusters = range(2,len(Euclidean_distance_matrix))
for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters)
    cluster_labels = clusterer.fit_predict(Euclidean_distance_matrix)
    silhouette_avg.append(silhouette_score(Euclidean_distance_matrix, cluster_labels))

for index,item in enumerate(silhouette_avg) :
    print("silhouette_avg for k=",index+2," is ",item)
print("the best silhouette_avg is:" ,min(silhouette_avg),". K=",(silhouette_avg.index(min(silhouette_avg)))+2)
the_best_K=(silhouette_avg.index(min(silhouette_avg)))+2


print('''
###############
#
#
#
#kmeans with the best K 
#
#
#
###############

''')
kmeans = KMeans(the_best_K).fit(Euclidean_distance_matrix)
print(kmeans.labels_)
