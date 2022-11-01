#DFS
#Time Complexity:: O(n)-all nodes are visited in each level and Null values are also process
#Space Complexity::  default dict-O(n) + O(h)-Recursive Stack
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        adj = defaultdict(list) #creating an adjacency list
        self.dict(root, adj) #creating dict
        
        res = [] #result array
        self.dfs(target.val, 0, k, res, adj, set()) #dfs function call
        return res
        
    def dict(self, curr, adj): # 
        if curr.left:    #traversing the left sub array
            adj[curr.val].append(curr.left.val) #append the root value with adjacent left val
            adj[curr.left.val].append(curr.val) #append the left val
            self.dict(curr.left, adj) 
        if curr.right:    #traverse the right sub array
            adj[curr.val].append(curr.right.val) #append the root value with adjacent right val
            adj[curr.right.val].append(curr.val) #append the right val
            self.dict(curr.right, adj)
        return
    
    def dfs(self, curr, current, previous, res, adj, visited): #passing all 
        if current == previous:    #appending in result when hit k
            res.append(curr)    #appending in result
            return
        visited.add(curr) #adding in visited
        for next_ in adj[curr]:    #traversing all adjacent nodes of curr
            if next_ not in visited: 
                visited.add(next_) #keeping track of visited nodes
                self.dfs(next_, current + 1, previous, res, adj, visited)
        return
