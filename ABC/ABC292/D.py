from collections import defaultdict

import sys
sys.setrecursionlimit(10**6)

class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        #各要素の親要素の番号を格納するリスト
        #要素がrootの場合は -(配下要素数) を格納する
        self.parents = [-1] * n
    
    #木を統合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        #すでに同じ木に属する場合
        if x == y:
            return
        
        #xよりyの方が要素数が多い場合、xとyを入れ替え
        #これにより、 size(y) <= size(x)が保証される
        if self.parents[x] < self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    #親を取得
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N, M = map(int, input().split())

uf = UnionFind(N)

m = {}

for i in range(N):
    m[i] = 0

for i in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1

    uf.union(u, v)
    m[u] += 1
    m[v] += 1

flag = True

groups = uf.all_group_members()

for g in groups:
    members = groups[g]


    count = 0
    for mem in members:
        count += m[mem]
    
    if len(members)*2 != count:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")