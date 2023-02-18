import collections


class Solution():
    def bfs(self, r, c):

        q = collections.deque()

        self.visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc

                if (r  in range(self.rows) and 
                    c in range(self.cols) and 
                    nums[r][c] == 1 and 
                    (r, c) not in self.visit):
                    self.count[-1] += 1
                    q.append((r, c))
                    self.visit.add((r, c))
                
        self.count.append(1)
    
    def __init__(self,nums):

        if not nums:
            return 0

        self.rows, self.cols = len(nums), len(nums[0])
        self.visit = set()
        self.groups = 0
        self.people = 0

        self.count = [1]
        
        for r in range(self.rows):

            for c in range(self.cols):

                if nums[r][c] == 1 and (r, c) not in self.visit:
                    
                    self.bfs(r, c)
                    self.groups += 1

        print(str(self.groups) + " teams of " + str(sorted(self.count[:-1], reverse=True) ) + " totaling "+ str(sum(self.count[:-1])))
    

if __name__ == "__main__":
    nums = [[1,1,0,0,0,0,1,1],
            [1,1,0,1,1,0,1,1],
            [0,0,0,1,1,0,0,0],
            [1,1,0,1,1,0,1,1],
            [1,1,0,0,0,0,1,1]]
    s = Solution(nums)
    