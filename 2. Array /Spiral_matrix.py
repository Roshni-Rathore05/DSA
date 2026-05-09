# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=len(matrix)
        c=len(matrix[0])
        top=0
        left=0
        right=c-1
        bottom=r-1

        ans=[]

        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range (top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1

            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        
        return ans
