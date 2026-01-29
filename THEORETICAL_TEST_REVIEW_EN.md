# THEORETICAL TEST REVIEW - DISCRETE MATHEMATICS 2

## SAMPLE EXAM ANALYSIS

### Exam Structure (100 points)
1. **Define concepts** (20pts) - 5 concepts
2. **Prove Euler path** (10pts)
3. **Prove full binary tree property** (10pts)
4. **Binary tree traversal** (15pts) - Pre/In/Post-order
5. **Construct tree from In-order and Post-order** (10pts)
6. **DFS and BFS on graphs** (10pts)
7. **Draw Binary Search Tree** (15pts)

---

## PART 1: CONCEPT DEFINITIONS (20pts)

### Concepts that appeared in sample exam

#### 1. Tree
**Definition:** A tree is a connected undirected graph with no simple cycles.

**Properties:**
- Has a unique path between any two vertices
- With n vertices, has exactly n-1 edges
- Removing any edge makes the graph disconnected

#### 2. Complete Graph
**Definition:** A simple graph in which there is an edge connecting every pair of distinct vertices.

**Notation:** K_n (complete graph with n vertices)

**Number of edges:** C(n,2) = n(n-1)/2

#### 3. Bipartite Graph
**Definition:** A simple graph G = (V, E) is bipartite if the vertex set V can be partitioned into two disjoint subsets V1 and V2 such that every edge in E connects a vertex in V1 with a vertex in V2.

**Properties:**
- No cycles of odd length
- Can be colored with 2 colors

#### 4. Leaf
**Definition:** A leaf (or leaf node) is a vertex in a tree with degree 1, i.e., it has no children.

**In rooted trees:** A leaf is a vertex with no children.

#### 5. Balanced Tree
**Definition:** A binary tree is called balanced if for every vertex, the difference between the heights of the left and right subtrees does not exceed 1.

**Purpose:** Ensures search, insert, and delete operations have O(log n) complexity

### Other IMPORTANT concepts that may appear

#### 6. Simple Graph
**Definition:** An undirected graph with no multiple edges and no loops.

#### 7. Rooted Tree
**Definition:** A tree with one vertex designated as the root, and every edge is directed away from the root.

#### 8. Binary Tree
**Definition:** A rooted tree in which each internal vertex has at most 2 children.

#### 9. Full Binary Tree
**Definition:** A binary tree in which each internal vertex has exactly 2 children.

#### 10. Binary Search Tree (BST)
**Definition:** A binary tree in which for each vertex, all values in the left subtree are less than the vertex value, and all values in the right subtree are greater.

#### 11. DAG (Directed Acyclic Graph)
**Definition:** A directed graph with no cycles.

#### 12. Euler Path
**Definition:** A path in a graph that passes through each edge exactly once.

**Existence condition:** A connected undirected graph has an Euler path if and only if it has exactly 0 or 2 vertices of odd degree.

#### 13. Euler Circuit
**Definition:** A circuit in a graph that passes through each edge exactly once.

**Existence condition:** A connected undirected graph has an Euler circuit if and only if all vertices have even degree.

#### 14. Hamilton Path
**Definition:** A path in a graph that visits each vertex exactly once.

#### 15. Connected Graph
**Definition:** An undirected graph in which there exists a path between every pair of vertices.

#### 16. Cycle
**Definition:** A simple path with the same starting and ending vertex.

#### 17. Spanning Tree
**Definition:** A subtree of graph G that contains all vertices of G.

#### 18. Weighted Graph
**Definition:** A graph in which each edge is assigned a numerical value (weight).

#### 19. Degree of a Vertex
**Definition:** The number of edges incident with that vertex (loops contribute 2 to the degree).

#### 20. Adjacency
**Definition:** Two vertices are called adjacent if there is an edge connecting them.

---

## PART 2: PROOFS (20pts)

### Type 1: Proofs about Euler Path/Circuit

#### Question from sample exam
**Prove:** A graph with at least 3 vertices of odd degree does not contain an Euler path.

**Solution:**
1. By the handshaking theorem: Σ deg(v) = 2|E| → the number of odd-degree vertices is always even
2. Necessary condition for Euler path: connected graph with exactly 0 or 2 odd-degree vertices
3. If there are ≥ 3 odd-degree vertices → condition not satisfied → no Euler path ∎

#### Similar proofs that may appear

**1. Prove the handshaking theorem**
```
Prove: Σ deg(v) = 2|E|
```

**Hint:**
- Each edge contributes 1 to the degree of two endpoint vertices
- Sum of degrees = 2 × number of edges

**2. Prove the number of odd-degree vertices is even**

**Hint:**
- From Σ deg(v) = 2|E| (even number)
- Split: Σ deg_even(v) + Σ deg_odd(v) = even number
- Since Σ deg_even(v) is even → Σ deg_odd(v) must be even
- Each odd-degree vertex contributes 1 odd number → number of odd-degree vertices must be even

**3. Prove the existence condition for Euler circuit**
```
Prove: A connected undirected graph has an Euler circuit 
⟺ All vertices have even degree
```

**4. Prove complete graph K_n has n(n-1)/2 edges**

### Type 2: Proofs about Trees

#### Question from sample exam
**Prove:** In a full binary tree, number of leaves = number of internal nodes + 1

**Solution:**
- Let L = number of leaves, I = number of internal nodes
- Total nodes: n = L + I
- Total edges in tree: n - 1 = L + I - 1
- Each internal node has 2 children, root has no parent, other nodes have 1 parent
- Number of edges = 2I (each internal node has 2 outgoing edges, minus duplicates)
- More precisely: Each node except root has exactly 1 incoming edge
- Number of edges = n - 1 = L + I - 1
- Number of edges also = total children = 2I (since each internal node has 2 children)
- But total children = total nodes - 1 (excluding root)
- → 2I = L + I - 1
- → I = L - 1
- → L = I + 1 ∎

**Alternative method (using induction):**
- Base case: Tree with 1 node (only root) → L=1, I=0 → L = I+1 ✓
- Assume true for tree with k internal nodes
- Add 1 internal node → add 2 leaves, remove 1 leaf (old leaf becomes internal)
- L' = L + 2 - 1 = L + 1, I' = I + 1
- L' = (I+1) + 1 = I' + 1 ✓

#### Similar proofs that may appear

**1. Prove a tree with n vertices has exactly n-1 edges**

**2. Prove in a full binary tree, the number of nodes is always odd**
```
Hint: n = L + I, and L = I + 1
→ n = (I+1) + I = 2I + 1 (odd)
```

**3. Prove the maximum number of leaves in a binary tree of height H is 2^H**

**4. Prove the maximum total nodes in a binary tree of height H is 2^(H+1) - 1**

**5. Prove an undirected graph is a tree ⟺ connected and has n-1 edges (n vertices)**

**6. Prove an undirected graph is a tree ⟺ has unique path between every pair of vertices**

### Type 3: Proofs about Bipartite Graphs

**Prove:** A graph is bipartite if and only if it has no cycles of odd length

**Prove:** A bipartite graph can be colored with 2 colors

---

## PART 3: BINARY TREE TRAVERSAL (15pts)

### Traversal Methods

#### 1. Pre-order
**Order:** Root → Left → Right
```
preOrder(node):
    if node == null: return
    print(node)
    preOrder(node.left)
    preOrder(node.right)
```

#### 2. In-order
**Order:** Left → Root → Right
```
inOrder(node):
    if node == null: return
    inOrder(node.left)
    print(node)
    inOrder(node.right)
```

#### 3. Post-order
**Order:** Left → Right → Root
```
postOrder(node):
    if node == null: return
    postOrder(node.left)
    postOrder(node.right)
    print(node)
```

### Example

```
Sample tree:
        5
       / \
      3   8
     / \   \
    1   4   9
```

**Results:**
- Pre-order: 5 3 1 4 8 9
- In-order: 1 3 4 5 8 9
- Post-order: 1 4 3 9 8 5

### Quick Recognition Tips

1. **Pre-order:** Root always first
2. **In-order:** In BST, gives sorted result
3. **Post-order:** Root always last

### Practice Problems

**Problem 1:**
```
        10
       /  \
      5    15
     / \     \
    2   7    20
```
Traverse Pre/In/Post?

**Problem 2:**
```
        A
       / \
      B   C
     /   / \
    D   E   F
```
Traverse Pre/In/Post?

**Problem 3:**
```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
```
Traverse Pre/In/Post?

---

## PART 4: CONSTRUCT TREE FROM TRAVERSALS (10pts)

### Case 1: Given In-order and Post-order

**Method:**
1. Last element of Post-order is root
2. Find root in In-order to divide left/right subtrees
3. Recurse on left and right subtrees

**Example from sample exam:**
```
In-order:  12 1 11 7 8 0 6 10 9 2 4 5 3
Post-order: 12 11 8 7 1 10 9 6 5 3 4 2 0
```

**Steps:**
1. Root = 0 (last in Post-order)
2. In In-order: [12 1 11 7 8] | 0 | [6 10 9 2 4 5 3]
3. Left subtree has 5 elements → take first 5 elements from Post-order (excluding root)
4. Right subtree has 7 elements → take next 7 elements
5. Recurse...

### Case 2: Given Pre-order and In-order

**Method:**
1. First element of Pre-order is root
2. Find root in In-order to divide left/right subtrees
3. Recurse on left and right subtrees

**Example:**
```
Pre-order: 5 3 1 2 4 8 7 9
In-order:  1 2 3 4 5 7 8 9
```

**Steps:**
1. Root = 5 (first in Pre-order)
2. In In-order: [1 2 3 4] | 5 | [7 8 9]
3. Left subtree has 4 elements, right subtree has 3 elements
4. Recurse...

### Case 3: Given Pre-order of BST

**Special:** Only Pre-order of BST is enough to construct the tree!

**Method:**
1. First element is root
2. Elements smaller than root → left subtree
3. Elements larger than root → right subtree
4. Recurse...

**Example:**
```
Pre-order: 5 3 1 4 8 7 9
```

**Construction:**
- Root = 5
- Left (< 5): 3 1 4
- Right (> 5): 8 7 9
- Recurse on each subtree...

### Practice Problems

**Problem 1:**
```
In-order:  4 2 5 1 6 3 7
Post-order: 4 5 2 6 7 3 1
Construct tree → find Pre-order?
```

**Problem 2:**
```
Pre-order: 10 5 1 7 40 50
In-order:  1 5 7 10 40 50
Construct tree → find Post-order?
```

**Problem 3:**
```
Pre-order BST: 8 3 1 6 4 7 10 14 13
Construct tree → find In-order and Post-order?
```

---

## PART 5: DFS AND BFS ON GRAPHS (10pts)

### DFS (Depth First Search)

**Algorithm:**
```
DFS(v):
    mark v as visited
    add v to result
    for each neighbor u of v (in order):
        if u not visited:
            DFS(u)
```

**Lexicographically largest:** Visit neighbors from large to small

**Lexicographically smallest:** Visit neighbors from small to large

### BFS (Breadth First Search)

**Algorithm:**
```
BFS(start):
    create queue Q
    mark start as visited
    add start to Q
    while Q is not empty:
        v = dequeue from Q
        add v to result
        for each neighbor u of v (in order):
            if u not visited:
                mark u as visited
                enqueue u to Q
```

### Example from sample exam

```
Graph (adjacency list):
0: [1, 2]
1: [0, 3, 4]
2: [0, 4, 5]
3: [1, 4, 7]
4: [1, 2, 3]
5: [2]
6: [8, 9]
7: [3, 8, 9]
8: [6, 7, 9]
9: [6, 7, 8]

Lexicographically largest DFS from 6:
- Visit from large to small
- Result: 6 9 8 7 3 4 2 5 1 0
```

### Practice Problems

**Problem 1:** DFS/BFS from vertex 0
```
    0---1---4
    |   |   |
    2   3   5
```

**Problem 2:** Lexicographically smallest DFS from A
```
    A---B---C
    |\ /|
    | X |
    |/ \|
    D---E
```

**Problem 3:** Compare DFS and BFS from 1
```
        1
       /|\
      2 3 4
     /|   |\
    5 6   7 8
```

---

## PART 6: DRAW BINARY SEARCH TREE (15pts)

### BST Insertion Rules

1. Start from root
2. If value < root → go left
3. If value > root → go right
4. Repeat until finding a null position
5. Insert at that position

### Example from sample exam

**Insertion sequence:** 31, 20, 72, 96, 76, 13, 18, 78, 98, 26, 94, 97, 80, 1, 83, 38, 86

**Steps:**
```
Step 1: 31 (root)
        31

Step 2: 20 < 31 → left
        31
       /
      20

Step 3: 72 > 31 → right
        31
       /  \
      20   72

Step 4: 96 > 31, > 72 → right right
        31
       /  \
      20   72
            \
            96

... continue until end
```

**Final result:**
```
                31
              /    \
            20      72
           /  \       \
          13   26      96
         /      \     /
        1       38   76
               /       \
              18       78
                         \
                         80
                        /  \
                      94   83
                     /       \
                    97       86
                   /
                  98
```

### Quick Drawing Tips

1. Write root first
2. Divide into 2 columns: < root (left), > root (right)
3. Recurse on each column

### Practice Problems

**Problem 1:** Draw BST with sequence: 50, 30, 70, 20, 40, 60, 80

**Problem 2:** Draw BST with sequence: 10, 5, 15, 2, 7, 12, 20, 1, 3

**Problem 3:** Draw BST with sequence: 100, 50, 150, 25, 75, 125, 175

**Problem 4:** Draw BST with sequence: 15, 10, 20, 8, 12, 16, 25, 6, 11, 13, 27

---

## PART 7: ADDITIONAL QUESTIONS THAT MAY APPEAR

### Type 1: True/False

1. Every tree is a bipartite graph ✓
2. Complete graph K_5 has 10 edges ✓
3. A tree with 100 vertices has 99 edges ✓
4. Every connected graph has an Euler path ✗
5. BST always gives sorted In-order ✓
6. Every binary tree is a binary search tree ✗
7. DFS and BFS give the same result ✗
8. A graph with cycles cannot be a tree ✓
9. A binary tree of height h has at most 2^h leaves ✓
10. Topological sort only applies to DAG ✓

### Type 2: Calculations

**1. Calculate number of edges in complete graph K_n**
- Formula: C(n,2) = n(n-1)/2

**2. Calculate minimum height of binary tree with n nodes**
- Formula: ⌈log₂(n+1)⌉ - 1

**3. Given vertex degrees, determine number of edges**
- Use: Σ deg(v) = 2|E|

**4. Determine if a tree can have a given degree sequence**

### Type 3: Algorithms

**1. Kruskal's algorithm (minimum spanning tree)**

**2. Prim's algorithm (minimum spanning tree)**

**3. Dijkstra's algorithm (shortest path)**

**4. Kahn's algorithm (Topological Sort)**

**5. Algorithm to check if graph is bipartite**

---

## PART 8: STUDY STRATEGY

### 1. Memorize definitions (20pts)

**List of 20 most important concepts:**
1. Tree
2. Rooted Tree
3. Binary Tree
4. Full Binary Tree
5. Complete Graph
6. Bipartite Graph
7. Leaf
8. Balanced Tree
9. Binary Search Tree
10. Simple Graph
11. DAG
12. Euler Path
13. Euler Circuit
14. Hamilton Path
15. Connected Graph
16. Cycle
17. Spanning Tree
18. Weighted Graph
19. Degree of Vertex
20. Topological Sort

**Tip:** Create flashcards, study 5 concepts per day

### 2. Practice proofs (20pts)

**5 MUST-KNOW proofs:**
1. Handshaking theorem: Σ deg(v) = 2|E|
2. Number of odd-degree vertices is even
3. In full binary tree: number of leaves = number of internal nodes + 1
4. Tree with n vertices has n-1 edges
5. Conditions for Euler path/circuit

**Tip:** Rewrite each proof 3-5 times

### 3. Master tree traversal (15pts)

**Practice:**
- Do at least 10 Pre/In/Post-order traversal problems
- Practice drawing trees step by step
- Familiarize with order memorization

**Tips:** 
- Pre = Me first
- In = Left-Me-Right
- Post = Kids first

### 4. Construct trees from traversals (10pts)

**Practice:**
- Do 5 In-order + Post-order problems
- Do 5 Pre-order + In-order problems
- Do 5 Pre-order BST problems

**Tip:** Always find root first, then divide left/right

### 5. Master DFS/BFS (10pts)

**Practice:**
- Draw graphs and traverse using DFS/BFS yourself
- Practice both lexicographically largest and smallest
- Understand the difference between Stack vs Queue

**Tips:**
- DFS = Stack = Go deep
- BFS = Queue = Go wide

### 6. Draw BST (15pts)

**Practice:**
- Draw 10 BSTs with different sequences
- Practice drawing fast, neat, clean
- Verify BST property

**Tips:**
- Always compare with current root
- Left < Root < Right
- Draw balanced for better visualization

### 7. Time Management

**Time allocation in exam (assuming 90 minutes):**
- Definitions (20pts): 15 minutes
- Proof 1 (10pts): 10 minutes
- Proof 2 (10pts): 10 minutes
- Tree traversal (15pts): 12 minutes
- Tree construction (10pts): 12 minutes
- DFS/BFS (10pts): 12 minutes
- Draw BST (15pts): 15 minutes
- Review: 4 minutes

**Note:** Do easy questions first!

---

## PART 9: COMPREHENSIVE EXERCISES

### Set 1: Definitions
Write definitions for the following 5 concepts:
1. Spanning Tree
2. Hamilton Path
3. Complete Binary Tree
4. Directed Graph
5. Multigraph

### Set 2: Proofs
1. Prove a bipartite graph has no odd-length cycles
2. Prove K_n has n(n-1)/2 edges
3. Prove a full binary tree has an odd number of nodes

### Set 3: Tree traversal
```
Traverse the following tree with Pre/In/Post-order:
        15
       /  \
      10   20
     / \   / \
    8  12 18 25
   /     \
  5      19
```

### Set 4: Tree construction
```
1. In-order:  5 10 15 20 25 30 35
   Post-order: 5 15 10 25 35 30 20
   → Find Pre-order?

2. Pre-order: 50 25 10 30 75 60 80
   In-order:  10 25 30 50 60 75 80
   → Find Post-order?

3. Pre-order BST: 20 10 5 15 30 25 40
   → Draw tree and find In-order?
```

### Set 5: DFS/BFS
```
Given graph:
    A---B---C
    |   |   |
    D---E---F
    |       |
    G-------H

1. DFS from A (alphabetical order)
2. BFS from A (alphabetical order)
3. Lexicographically largest DFS from H
```

### Set 6: Draw BST
Draw BST with the following sequences:
1. 45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40
2. 100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87
3. 60, 40, 80, 20, 50, 70, 90, 10, 30, 45, 55, 65, 75, 85, 95

---

## PART 10: SAMPLE ANSWERS FOR EXAM

### Question 1: Definitions (20pts)
*(Presented in Part 1)*

### Question 2: Prove Euler path (10pts)
*(Presented in Part 2)*

### Question 3: Prove Full Binary Tree (10pts)
*(Presented in Part 2)*

### Question 4: Tree traversal (15pts)
**Need to see diagram in original exam to solve**

### Question 5: Tree construction (10pts)
```
In-order:  12 1 11 7 8 0 6 10 9 2 4 5 3
Post-order: 12 11 8 7 1 10 9 6 5 3 4 2 0

Root = 0 (last in Post-order)
Divide: [12 1 11 7 8] 0 [6 10 9 2 4 5 3]

Left subtree:
In: 12 1 11 7 8
Post: 12 11 8 7 1
Root = 1
Divide: [12] 1 [11 7 8]
...

Right subtree:
In: 6 10 9 2 4 5 3
Post: 10 9 6 5 3 4 2
Root = 2
...

Result tree:
           0
         /   \
        1     2
       / \   / \
     12   8 6   4
         /   \   /\
        7    9  5  3
       /    /
      11   10
```

### Question 6: DFS/BFS (10pts)
**DFS from 6 (lexicographically largest):**
- Visit from large to small: 6 → 9 → 8 → 7 → 3 → 4 → 2 → 1 → 5 → 0
- (Need to see graph for exact answer)

**BFS from 6:**
- (Need to see graph to solve)

### Question 7: Draw BST (15pts)
**Sequence:** 31, 20, 72, 96, 76, 13, 18, 78, 98, 26, 94, 97, 80, 1, 83, 38, 86

**Result:** *(Need to draw on paper)*

---

## CONCLUSION AND ADVICE

### Strengths to maintain
1. ✓ Memorize definitions accurately
2. ✓ Understand proof steps clearly
3. ✓ Practice many similar problems
4. ✓ Manage time well

### Common mistakes to avoid
1. ✗ Confusing Pre/In/Post-order
2. ✗ Forgetting Euler path condition (0 or 2 odd-degree vertices)
3. ✗ Drawing BST with wrong left/right order
4. ✗ Incorrect tree construction division
5. ✗ Wrong DFS/BFS traversal order

### Checklist before exam
- [ ] Memorize 20 important definitions
- [ ] Know how to prove 5 basic theorems
- [ ] Master 10 tree traversal problems
- [ ] Complete 15 tree construction problems
- [ ] Complete 10 DFS/BFS problems
- [ ] Master drawing 10 BSTs
- [ ] Review sample exam
- [ ] Prepare A4 scratch paper for handwriting

### References
1. Discrete Mathematics and Its Applications - Kenneth H. Rosen
2. MATH202 lecture slides
3. Summary file: TONG_HOP_TOAN_ROI_RAC_2.md

---

**Good luck with your studies and achieve high scores! 🎓**

**Note:** The exam may change but the structure and question types are similar. Focus on understanding the fundamentals and practice extensively.
