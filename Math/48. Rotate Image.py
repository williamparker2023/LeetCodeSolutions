"""
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 
90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the 
input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

https://leetcode.com/problems/rotate-image/description/
"""

"""
I decided that it would be much easier conceptually to first change basis to 
cartesian coordinates with the origin at the center of the matrix, then find
the given coord shifted 90 degrees, and then convert back. You can do this for all
4 pairs in the matrix by shifting all of the upper left quadrant numbers

This will be O(n^2) time and O(1) space since we are doing it in place, and only look 
at each element once.
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #it is easiest to convert to cartesian, do rotation, and then swap back to i,j
        #we do this for all groups of 4 elements
        def nextCoord(i,j,n):
            curX = -(n//2) + j
            curY = n//2 - i
            if n%2==0:
                if curX >=0:
                    curX += 1
                if curY <=0:
                    curY-=1

            nextX = curY
            nextY = -curX
            if n%2==0:
                if nextX>=0:
                    nextX-=1
                if nextY<=0:
                    nextY+=1
            nextI = -nextY + n//2
            nextJ = nextX + n//2
            return [nextI,nextJ]

        n = len(matrix)

        for i in range((n+1)//2):
            for j in range(n//2):
                first = [i,j]
                second = nextCoord(i,j,n)
                temp = matrix[second[0]][second[1]]
                matrix[second[0]][second[1]] = matrix[first[0]][first[1]]

                third = nextCoord(second[0],second[1],n)
                temp2 = matrix[third[0]][third[1]]
                matrix[third[0]][third[1]] = temp
                
                fourth = nextCoord(third[0],third[1],n)
                temp = matrix[fourth[0]][fourth[1]]
                matrix[fourth[0]][fourth[1]] = temp2
                
                matrix[i][j] = temp