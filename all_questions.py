# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] ="Agglomerative hierarchical clustering handles outliers better than k-means because it forms clusters step by step, making it less affected by extreme values."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = " K-means can give different results each time it's run because it starts with random points. In contrast, agglomerative hierarchical clustering always gives the same result for the same data because it follows a set process without randomness."
    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means is generally faster and uses less memory than agglomerative hierarchical clustering because it involves simpler calculations and fewer steps. However, it's not the most efficient clustering algorithm in all scenarios since efficiency can depend on the specific characteristics of the dataset and the context in which clustering is applied."
    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting a cluster lowers the sum of squared errors because it creates two centers for the same group, leading to a shorter distance to the nearest centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In K-means clustering, a decrease in SSE (Sum of Squared Errors) means that data points are closer to their respective cluster centroids, indicating increased cohesion within clusters."
    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In K-means clustering, an increase in SSB (Between Sum of Squares) indicates that clusters are further apart from each other, which means that the separation between clusters has increased."
    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In k-means, making clusters tighter (cohesion) doesn't always mean they'll be further apart (separation)."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In k-means, the total sum of squares (TSS) is the addition of SSE and SSB, and it stays the same throughout the clustering process."
   
    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Splitting a cluster into two lowers error by creating two closer centers, shortening distances."
    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = "True"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In the figure, the clusters are positioned too distant from the centroid to draw points from other areas."

    # type: bool (True/False)
    answers["(b)"] = "False"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The figure shows that the shaded areas are near each other, meaning the clusters will include points from both shaded areas."

    # type: bool (True/False)
    answers["(c)"] = "True"

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid at 12.5 is too distant from any points, leading to all other clusters being left without any points."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * R^2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 * (a**2 + b**2 + c**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*(R^2 + 0^2 + (R/2)^2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "All points in circle A will go to its centroid. Around one-third of circle B's points, specifically those on the left side, will belong to the left centroid in B. The rest of B's points and all points in C will be grouped with the centroid at B's center, causing the right centroid in B to shift to circle C due to C's larger number of points. In the following iteration, points in circles A, B, and C will align with their respective centroids, leading to convergence of the K-means algorithm."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "
Given that circles A and B are near each other and far from circle C, the points from A and B will cluster around the centroid in A. The points in C will be evenly divided among the two centroids there, with each getting 50,000 points. Since A and B have an equal number of points, the centroid in A will shift between them. The centroids in C will slightly separate but stay within C, each holding half of the points from C."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since circles A and B are situated closely to each other and a considerable distance from circle C, the points from A and B will cluster around the centroid in A. Meanwhile, the points within C will be equally distributed between two centroids, with each holding 50,000 points. Given that A and B each contain an equal number of points, the centroid in A will oscillate between them. Although the centroids within C will drift slightly apart, they will remain within C, each encompassing half of C's points."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group B', 'Group A'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B are close enough to join because the farthest point on the right of A and the nearest point on the left of B are the closest to each other."

    # type: set
    answers["(b)"] = {'Group C', 'Group A'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "
Groups A and C will be combined because the distance between A's farthest right point and C's farthest point is the shortest when compared to the distances between A's leftmost point and B's rightmost point, and between B's rightmost point and C's farthest point."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'I', 'G', 'J', 'E', 'M', 'B', 'L', 'F', 'D', 'C'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 shows the highest entropy because its categories are more evenly spread out."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 displays low entropy because its data is mostly concentrated in one category, resulting in high uniformity."

    return answers

    

# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Two diagonal entries appear bluer and clearer, suggesting that clusters B and C are more tightly knit compared to clusters A and D."
    
    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Rows 1 and 3 represent clusters A and C, showing different distances to other clusters with changing colors: A is closest to C (blue), nearer to B (green), and farthest from D (yellow), and the same pattern applies to C. Row 2 matches B, with equal distances to A and C (green) and the farthest from D (red). Row 4 matches D, equally distant from A and C (yellow) and farthest from B (red)."
   
    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal entries are bluer and sharper, showing that clusters B and C are tighter than A and D."
    
    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "1.Rows 1 and 4, which are less clear, show varying colors for different clusters, meaning each cluster is at a distinct distance from them (for example, Cluster A is closest to B, then C, and farthest from D, with no two clusters at the same distance from A). 2.Rows with clearer diagonal entries have two identical colors (besides the diagonal), indicating equal distances to two clusters and being farthest from another (for example, B is equally distant from A and C, but farthest from D)."
    
    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries are bluer and clearer, showing that clusters B and C are more closely knit than A and D."
    
    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Each row has two matching and one unique color off the diagonal, showing every cluster is closer to two clusters than to the last one (for example, B is equally near to A and C but farther from D)."
    
    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Less clear diagonal means the cluster isn't very tight. Different colors off-diagonal show varying distances to others (nearest to B, then C, farthest from A)."
   
    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Sharper diagonal suggests a tight cluster. Two off-diagonals are the same color, showing closeness to two clusters (A and C, even if A's distance looks fuzzier), and farthest from one cluster (D)."
    
    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Sharper diagonal suggests a tight cluster. Two off-diagonals are the same color, showing closeness to two clusters (A and C, even if A's distance looks fuzzier), and farthest from one cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Different colors off-diagonal indicate distances to others vary (closest to A, next is C, and most distant from B). A less clear diagonal suggests the cluster is not tightly knit, reversing the original order."
    return answers







# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Partial', 'Overlapping']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']


    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Letter grades are unique and do not mix, meaning a student gets just one grade for each class, and every student in the class gets a grade."
    return answers





# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN is suitable for (b) as the points representing the nose, eyes, and mouth are closer to each other compared to the spaces between them, allowing DBSCAN to identify these features. In contrast, for (a), the high density of noise compared to the key features means DBSCAN would likely remove the nose, eyes, and mouth areas."
    
    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means can be effective for (b) if it's configured with four clusters, though it will also group points of lower density. However, K-means is not suitable for (a)."
    
    # type: string
    answers["(c)"] = "Use the inverse of density as the new density value and apply DBSCAN using this adjusted metric."
    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
