class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix)
        l, r = 0, len(matrix[0])
        row = u + (d-u)//2
        mid = l + (r-l)//2
        print("final row: ", row)

        while d > u + 1:
            print(u,d,row)
            print(matrix[row][0])

            if matrix[row][0] > target:
                print("case 1", matrix[row][0], target)
                d = row - 1
                
            elif matrix[row][0] < target:
                print("case 2")
                u = row
            else:
                print("case 3")
                return True
            row = u + (d-u)//2
        while r > l:
            if matrix[row][mid] > target:
                r = mid
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
            mid = l + (r-l)//2
        return False

        
        