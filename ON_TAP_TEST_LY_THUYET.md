# ÔN TẬP TEST LÝ THUYẾT - TOÁN RỜI RẠC 2

## PHÂN TÍCH ĐỀ THI MẪU

### Cấu trúc đề thi (100 điểm)
1. **Định nghĩa các khái niệm** (20đ) - 5 khái niệm
2. **Chứng minh Euler path** (10đ)
3. **Chứng minh tính chất cây nhị phân đầy đủ** (10đ)
4. **Duyệt cây nhị phân** (15đ) - Pre/In/Post-order
5. **Xây dựng cây từ In-order và Post-order** (10đ)
6. **DFS và BFS trên đồ thị** (10đ)
7. **Vẽ Binary Search Tree** (15đ)

---

## PHẦN 1: ĐỊNH NGHĨA CÁC KHÁI NIỆM (20đ)

### Các khái niệm đã xuất hiện trong đề mẫu

#### 1. Tree (Cây)
**Định nghĩa:** Một cây là một đồ thị vô hướng liên thông không có chu trình đơn.

**Tính chất:**
- Có đường đi duy nhất giữa hai đỉnh bất kỳ
- Với n đỉnh, có đúng n-1 cạnh
- Loại bỏ bất kỳ cạnh nào sẽ làm đồ thị không liên thông

#### 2. Complete Graph (Đồ thị đầy đủ)
**Định nghĩa:** Một đồ thị đơn trong đó có cạnh nối giữa mỗi cặp đỉnh phân biệt.

**Ký hiệu:** K_n (đồ thị đầy đủ với n đỉnh)

**Số cạnh:** C(n,2) = n(n-1)/2

#### 3. Bipartite Graph (Đồ thị hai phía)
**Định nghĩa:** Một đồ thị đơn G = (V, E) là đồ thị hai phía nếu tập đỉnh V có thể được phân chia thành hai tập con V1 và V2 rời nhau sao cho mọi cạnh trong E nối một đỉnh trong V1 với một đỉnh trong V2.

**Tính chất:**
- Không có chu trình độ dài lẻ
- Có thể tô màu bằng 2 màu

#### 4. Leaf (Lá - trong cây)
**Định nghĩa:** Một lá (hay nút lá) là một đỉnh trong cây có bậc bằng 1, tức là không có đỉnh con.

**Trong cây có gốc:** Lá là đỉnh không có con.

#### 5. Balanced Tree (Cây cân bằng)
**Định nghĩa:** Một cây nhị phân được gọi là cân bằng nếu với mọi đỉnh, hiệu giữa chiều cao của cây con trái và cây con phải không vượt quá 1.

**Mục đích:** Đảm bảo các thao tác tìm kiếm, chèn, xóa có độ phức tạp O(log n)

### Các khái niệm QUAN TRỌNG khác có thể xuất hiện

#### 6. Simple Graph (Đồ thị đơn)
**Định nghĩa:** Một đồ thị vô hướng không có cạnh song song (multiple edges) và không có khuyên (loops).

#### 7. Rooted Tree (Cây có gốc)
**Định nghĩa:** Một cây có một đỉnh được chỉ định làm gốc, và mọi cạnh được hướng ra khỏi gốc.

#### 8. Binary Tree (Cây nhị phân)
**Định nghĩa:** Một cây có gốc trong đó mỗi đỉnh nội có không quá 2 con.

#### 9. Full Binary Tree (Cây nhị phân đầy đủ)
**Định nghĩa:** Một cây nhị phân trong đó mỗi đỉnh nội có đúng 2 con.

#### 10. Binary Search Tree (BST)
**Định nghĩa:** Một cây nhị phân trong đó với mỗi đỉnh, tất cả các giá trị trong cây con trái nhỏ hơn giá trị đỉnh đó, và tất cả các giá trị trong cây con phải lớn hơn.

#### 11. DAG (Directed Acyclic Graph)
**Định nghĩa:** Một đồ thị có hướng không chứa chu trình.

#### 12. Euler Path (Đường đi Euler)
**Định nghĩa:** Một đường đi trong đồ thị đi qua mỗi cạnh đúng một lần.

**Điều kiện tồn tại:** Đồ thị vô hướng liên thông có Euler path khi và chỉ khi có đúng 0 hoặc 2 đỉnh bậc lẻ.

#### 13. Euler Circuit (Chu trình Euler)
**Định nghĩa:** Một chu trình trong đồ thị đi qua mỗi cạnh đúng một lần.

**Điều kiện tồn tại:** Đồ thị vô hướng liên thông có Euler circuit khi và chỉ khi tất cả các đỉnh có bậc chẵn.

#### 14. Hamilton Path (Đường đi Hamilton)
**Định nghĩa:** Một đường đi trong đồ thị đi qua mỗi đỉnh đúng một lần.

#### 15. Connected Graph (Đồ thị liên thông)
**Định nghĩa:** Một đồ thị vô hướng trong đó tồn tại đường đi giữa mọi cặp đỉnh.

#### 16. Cycle (Chu trình)
**Định nghĩa:** Một đường đi đơn có cùng đỉnh đầu và đỉnh cuối.

#### 17. Spanning Tree (Cây khung)
**Định nghĩa:** Một cây con của đồ thị G chứa tất cả các đỉnh của G.

#### 18. Weighted Graph (Đồ thị có trọng số)
**Định nghĩa:** Một đồ thị trong đó mỗi cạnh được gán một giá trị số (trọng số).

#### 19. Degree of a Vertex (Bậc của đỉnh)
**Định nghĩa:** Số cạnh liên thuộc với đỉnh đó (khuyên đóng góp 2 vào bậc).

#### 20. Adjacency (Đỉnh kề)
**Định nghĩa:** Hai đỉnh được gọi là kề nhau nếu có cạnh nối giữa chúng.

---

## PHẦN 2: CHỨNG MINH (20đ)

### Dạng 1: Chứng minh về Euler Path/Circuit

#### Câu đã có trong đề mẫu
**Chứng minh:** Một đồ thị có ít nhất 3 đỉnh bậc lẻ không chứa đường đi Euler.

**Lời giải:**
1. Theo định lý bắt tay: Σ deg(v) = 2|E| → số đỉnh bậc lẻ luôn chẵn
2. Điều kiện cần để có Euler path: đồ thị liên thông và có đúng 0 hoặc 2 đỉnh bậc lẻ
3. Nếu có ≥ 3 đỉnh bậc lẻ → không thỏa điều kiện → không có Euler path ∎

#### Các câu chứng minh tương tự có thể xuất hiện

**1. Chứng minh định lý bắt tay (Handshaking Theorem)**
```
Chứng minh: Σ deg(v) = 2|E|
```

**Gợi ý:**
- Mỗi cạnh đóng góp 1 vào bậc của hai đỉnh đầu cuối
- Tổng bậc = 2 × số cạnh

**2. Chứng minh số đỉnh bậc lẻ là số chẵn**

**Gợi ý:**
- Từ Σ deg(v) = 2|E| (số chẵn)
- Tách: Σ deg_chẵn(v) + Σ deg_lẻ(v) = số chẵn
- Vì Σ deg_chẵn(v) là chẵn → Σ deg_lẻ(v) phải chẵn
- Mỗi đỉnh bậc lẻ đóng góp 1 số lẻ → số đỉnh bậc lẻ phải chẵn

**3. Chứng minh điều kiện tồn tại Euler circuit**
```
Chứng minh: Đồ thị vô hướng liên thông có Euler circuit 
⟺ Tất cả các đỉnh có bậc chẵn
```

**4. Chứng minh đồ thị đầy đủ K_n có n(n-1)/2 cạnh**

### Dạng 2: Chứng minh về Cây

#### Câu đã có trong đề mẫu
**Chứng minh:** Trong cây nhị phân đầy đủ, số lá = số đỉnh nội + 1

**Lời giải:**
- Gọi L = số lá, I = số đỉnh nội
- Tổng số đỉnh: n = L + I
- Tổng số cạnh trong cây: n - 1 = L + I - 1
- Mỗi đỉnh nội có 2 con, gốc không có cha, các đỉnh khác có 1 cha
- Số cạnh = 2I (mỗi đỉnh nội có 2 cạnh đi ra, trừ các cạnh trùng)
- Chính xác hơn: Mỗi đỉnh trừ gốc có đúng 1 cạnh đi vào
- Số cạnh = n - 1 = L + I - 1
- Số cạnh cũng = tổng con = 2I (vì mỗi đỉnh nội có 2 con)
- Nhưng tổng con = tổng đỉnh - 1 (trừ gốc)
- → 2I = L + I - 1
- → I = L - 1
- → L = I + 1 ∎

**Cách khác (dùng quy nạp):**
- Cơ sở: Cây có 1 đỉnh (chỉ gốc) → L=1, I=0 → L = I+1 ✓
- Giả sử đúng với cây có k đỉnh nội
- Thêm 1 đỉnh nội → thêm 2 lá, bớt 1 lá (lá cũ thành nội)
- L' = L + 2 - 1 = L + 1, I' = I + 1
- L' = (I+1) + 1 = I' + 1 ✓

#### Các câu chứng minh tương tự có thể xuất hiện

**1. Chứng minh cây với n đỉnh có đúng n-1 cạnh**

**2. Chứng minh trong cây nhị phân đầy đủ, số đỉnh luôn lẻ**
```
Gợi ý: n = L + I, và L = I + 1
→ n = (I+1) + I = 2I + 1 (lẻ)
```

**3. Chứng minh số lá tối đa trong cây nhị phân cao H là 2^H**

**4. Chứng minh tổng số đỉnh tối đa trong cây nhị phân cao H là 2^(H+1) - 1**

**5. Chứng minh đồ thị vô hướng là cây ⟺ liên thông và có n-1 cạnh (n đỉnh)**

**6. Chứng minh đồ thị vô hướng là cây ⟺ có đường đi duy nhất giữa mọi cặp đỉnh**

### Dạng 3: Chứng minh về Đồ thị hai phía

**Chứng minh:** Một đồ thị là hai phía khi và chỉ khi không có chu trình độ dài lẻ

**Chứng minh:** Đồ thị hai phía có thể tô màu bằng 2 màu

---

## PHẦN 3: DUYỆT CÂY NHỊ PHÂN (15đ)

### Các phương pháp duyệt

#### 1. Pre-order (Tiền tự)
**Thứ tự:** Gốc → Trái → Phải
```
preOrder(node):
    if node == null: return
    print(node)
    preOrder(node.left)
    preOrder(node.right)
```

#### 2. In-order (Trung tự)
**Thứ tự:** Trái → Gốc → Phải
```
inOrder(node):
    if node == null: return
    inOrder(node.left)
    print(node)
    inOrder(node.right)
```

#### 3. Post-order (Hậu tự)
**Thứ tự:** Trái → Phải → Gốc
```
postOrder(node):
    if node == null: return
    postOrder(node.left)
    postOrder(node.right)
    print(node)
```

### Ví dụ minh họa

```
Cây mẫu:
        5
       / \
      3   8
     / \   \
    1   4   9
```

**Kết quả:**
- Pre-order: 5 3 1 4 8 9
- In-order: 1 3 4 5 8 9
- Post-order: 1 4 3 9 8 5

### Mẹo nhận biết nhanh

1. **Pre-order:** Gốc luôn đầu tiên
2. **In-order:** Trong BST, cho kết quả tăng dần
3. **Post-order:** Gốc luôn cuối cùng

### Bài tập luyện tập

**Bài 1:**
```
        10
       /  \
      5    15
     / \     \
    2   7    20
```
Duyệt Pre/In/Post?

**Bài 2:**
```
        A
       / \
      B   C
     /   / \
    D   E   F
```
Duyệt Pre/In/Post?

**Bài 3:**
```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
```
Duyệt Pre/In/Post?

---

## PHẦN 4: XÂY DỰNG CÂY TỪ DUYỆT (10đ)

### Trường hợp 1: Cho In-order và Post-order

**Phương pháp:**
1. Phần tử cuối của Post-order là gốc
2. Tìm gốc trong In-order để chia cây con trái/phải
3. Đệ quy với cây con trái và phải

**Ví dụ từ đề mẫu:**
```
In-order:  12 1 11 7 8 0 6 10 9 2 4 5 3
Post-order: 12 11 8 7 1 10 9 6 5 3 4 2 0
```

**Các bước:**
1. Gốc = 0 (cuối Post-order)
2. Trong In-order: [12 1 11 7 8] | 0 | [6 10 9 2 4 5 3]
3. Cây con trái có 5 phần tử → lấy 5 phần tử đầu Post-order (trừ gốc)
4. Cây con phải có 7 phần tử → lấy 7 phần tử tiếp theo
5. Đệ quy...

### Trường hợp 2: Cho Pre-order và In-order

**Phương pháp:**
1. Phần tử đầu của Pre-order là gốc
2. Tìm gốc trong In-order để chia cây con trái/phải
3. Đệ quy với cây con trái và phải

**Ví dụ:**
```
Pre-order: 5 3 1 2 4 8 7 9
In-order:  1 2 3 4 5 7 8 9
```

**Các bước:**
1. Gốc = 5 (đầu Pre-order)
2. Trong In-order: [1 2 3 4] | 5 | [7 8 9]
3. Cây con trái có 4 phần tử, cây con phải có 3 phần tử
4. Đệ quy...

### Trường hợp 3: Cho Pre-order của BST

**Đặc biệt:** Chỉ cần Pre-order của BST cũng có thể xây dựng cây!

**Phương pháp:**
1. Phần tử đầu là gốc
2. Các phần tử nhỏ hơn gốc → cây con trái
3. Các phần tử lớn hơn gốc → cây con phải
4. Đệ quy...

**Ví dụ:**
```
Pre-order: 5 3 1 4 8 7 9
```

**Xây dựng:**
- Gốc = 5
- Trái (< 5): 3 1 4
- Phải (> 5): 8 7 9
- Đệ quy với mỗi cây con...

### Bài tập luyện tập

**Bài 1:**
```
In-order:  4 2 5 1 6 3 7
Post-order: 4 5 2 6 7 3 1
Xây dựng cây → tìm Pre-order?
```

**Bài 2:**
```
Pre-order: 10 5 1 7 40 50
In-order:  1 5 7 10 40 50
Xây dựng cây → tìm Post-order?
```

**Bài 3:**
```
Pre-order BST: 8 3 1 6 4 7 10 14 13
Xây dựng cây → tìm In-order và Post-order?
```

---

## PHẦN 5: DFS VÀ BFS TRÊN ĐỒ THỊ (10đ)

### DFS (Depth First Search)

**Thuật toán:**
```
DFS(v):
    đánh dấu v đã thăm
    thêm v vào kết quả
    for each hàng xóm u của v (theo thứ tự):
        if u chưa thăm:
            DFS(u)
```

**Lexicographically largest:** Duyệt hàng xóm từ lớn đến nhỏ

**Lexicographically smallest:** Duyệt hàng xóm từ nhỏ đến lớn

### BFS (Breadth First Search)

**Thuật toán:**
```
BFS(start):
    tạo queue Q
    đánh dấu start đã thăm
    thêm start vào Q
    while Q không rỗng:
        v = lấy phần tử đầu Q
        thêm v vào kết quả
        for each hàng xóm u của v (theo thứ tự):
            if u chưa thăm:
                đánh dấu u đã thăm
                thêm u vào Q
```

### Ví dụ từ đề mẫu

```
Đồ thị (danh sách kề):
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

Lexicographically largest DFS từ 6:
- Duyệt từ lớn đến nhỏ
- Kết quả: 6 9 8 7 3 4 2 5 1 0
```

### Bài tập luyện tập

**Bài 1:** DFS/BFS từ đỉnh 0
```
    0---1---4
    |   |   |
    2   3   5
```

**Bài 2:** Lexicographically smallest DFS từ A
```
    A---B---C
    |\ /|
    | X |
    |/ \|
    D---E
```

**Bài 3:** So sánh DFS và BFS từ 1
```
        1
       /|\
      2 3 4
     /|   |\
    5 6   7 8
```

---

## PHẦN 6: VẼ BINARY SEARCH TREE (15đ)

### Quy tắc chèn vào BST

1. Bắt đầu từ gốc
2. Nếu giá trị < gốc → đi sang trái
3. Nếu giá trị > gốc → đi sang phải
4. Lặp lại cho đến khi tìm thấy vị trí null
5. Chèn vào vị trí đó

### Ví dụ từ đề mẫu

**Dãy chèn:** 31, 20, 72, 96, 76, 13, 18, 78, 98, 26, 94, 97, 80, 1, 83, 38, 86

**Các bước:**
```
Bước 1: 31 (gốc)
        31

Bước 2: 20 < 31 → trái
        31
       /
      20

Bước 3: 72 > 31 → phải
        31
       /  \
      20   72

Bước 4: 96 > 31, > 72 → phải phải
        31
       /  \
      20   72
            \
            96

... tiếp tục cho đến hết
```

**Kết quả cuối cùng:**
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

### Mẹo vẽ nhanh

1. Viết gốc trước
2. Chia làm 2 cột: < gốc (trái), > gốc (phải)
3. Đệ quy với mỗi cột

### Bài tập luyện tập

**Bài 1:** Vẽ BST với dãy: 50, 30, 70, 20, 40, 60, 80

**Bài 2:** Vẽ BST với dãy: 10, 5, 15, 2, 7, 12, 20, 1, 3

**Bài 3:** Vẽ BST với dãy: 100, 50, 150, 25, 75, 125, 175

**Bài 4:** Vẽ BST với dãy: 15, 10, 20, 8, 12, 16, 25, 6, 11, 13, 27

---

## PHẦN 7: CÂU HỎI BỔ SUNG CÓ THỂ XUẤT HIỆN

### Dạng 1: True/False

1. Mọi cây đều là đồ thị hai phía ✓
2. Đồ thị đầy đủ K_5 có 10 cạnh ✓
3. Cây với 100 đỉnh có 99 cạnh ✓
4. Mọi đồ thị liên thông đều có đường đi Euler ✗
5. BST luôn cho In-order tăng dần ✓
6. Mọi cây nhị phân đều là cây tìm kiếm nhị phân ✗
7. DFS và BFS cho cùng kết quả ✗
8. Đồ thị có chu trình không thể là cây ✓
9. Cây nhị phân cao h có tối đa 2^h lá ✓
10. Topological sort chỉ áp dụng cho DAG ✓

### Dạng 2: Tính toán

**1. Tính số cạnh trong đồ thị đầy đủ K_n**
- Công thức: C(n,2) = n(n-1)/2

**2. Tính chiều cao tối thiểu của cây nhị phân có n đỉnh**
- Công thức: ⌈log₂(n+1)⌉ - 1

**3. Cho bậc các đỉnh, xác định số cạnh**
- Dùng: Σ deg(v) = 2|E|

**4. Xác định cây có thể có từ danh sách bậc**

### Dạng 3: Thuật toán

**1. Thuật toán Kruskal (tìm cây khung nhỏ nhất)**

**2. Thuật toán Prim (tìm cây khung nhỏ nhất)**

**3. Thuật toán Dijkstra (đường đi ngắn nhất)**

**4. Thuật toán Kahn (Topological Sort)**

**5. Thuật toán kiểm tra đồ thị hai phía**

---

## PHẦN 8: CHIẾN LƯỢC ÔN TẬP

### 1. Học thuộc định nghĩa (20đ)

**Danh sách 20 khái niệm quan trọng nhất:**
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

**Mẹo:** Viết flashcard, học mỗi ngày 5 khái niệm

### 2. Luyện chứng minh (20đ)

**5 chứng minh PHẢI BIẾT:**
1. Định lý bắt tay: Σ deg(v) = 2|E|
2. Số đỉnh bậc lẻ là số chẵn
3. Trong full binary tree: số lá = số nội + 1
4. Cây n đỉnh có n-1 cạnh
5. Điều kiện Euler path/circuit

**Mẹo:** Viết lại chứng minh 3-5 lần cho mỗi bài

### 3. Thành thạo duyệt cây (15đ)

**Luyện tập:**
- Làm ít nhất 10 bài duyệt Pre/In/Post-order
- Tập vẽ cây theo từng bước
- Làm quen với cách ghi nhớ thứ tự

**Mẹo:** 
- Pre = Me first (tôi trước)
- In = Left-Me-Right (trái-tôi-phải)
- Post = Kids first (con trước)

### 4. Xây dựng cây từ duyệt (10đ)

**Luyện tập:**
- Làm 5 bài In-order + Post-order
- Làm 5 bài Pre-order + In-order
- Làm 5 bài Pre-order BST

**Mẹo:** Luôn tìm gốc trước, rồi chia trái/phải

### 5. Thành thạo DFS/BFS (10đ)

**Luyện tập:**
- Vẽ đồ thị và tự duyệt DFS/BFS
- Luyện cả lexicographically largest và smallest
- Hiểu sự khác biệt Stack vs Queue

**Mẹo:**
- DFS = Stack = Đi sâu
- BFS = Queue = Đi rộng

### 6. Vẽ BST (15đ)

**Luyện tập:**
- Vẽ 10 BST với các dãy khác nhau
- Luyện vẽ nhanh, gọn, đẹp
- Kiểm tra lại tính chất BST

**Mẹo:**
- Luôn so sánh với gốc hiện tại
- Trái < Gốc < Phải
- Vẽ cân đối để dễ nhìn

### 7. Quản lý thời gian

**Phân bổ thời gian trong bài thi (giả sử 90 phút):**
- Định nghĩa (20đ): 15 phút
- Chứng minh 1 (10đ): 10 phút
- Chứng minh 2 (10đ): 10 phút
- Duyệt cây (15đ): 12 phút
- Xây dựng cây (10đ): 12 phút
- DFS/BFS (10đ): 12 phút
- Vẽ BST (15đ): 15 phút
- Kiểm tra lại: 4 phút

**Lưu ý:** Làm câu dễ trước!

---

## PHẦN 9: BÀI TẬP TỔNG HỢP

### Set 1: Định nghĩa
Viết định nghĩa cho 5 khái niệm sau:
1. Spanning Tree
2. Hamilton Path
3. Complete Binary Tree
4. Directed Graph
5. Multigraph

### Set 2: Chứng minh
1. Chứng minh đồ thị hai phía không có chu trình lẻ
2. Chứng minh K_n có n(n-1)/2 cạnh
3. Chứng minh cây nhị phân đầy đủ có số đỉnh lẻ

### Set 3: Duyệt cây
```
Duyệt cây sau với Pre/In/Post-order:
        15
       /  \
      10   20
     / \   / \
    8  12 18 25
   /     \
  5      19
```

### Set 4: Xây dựng cây
```
1. In-order:  5 10 15 20 25 30 35
   Post-order: 5 15 10 25 35 30 20
   → Tìm Pre-order?

2. Pre-order: 50 25 10 30 75 60 80
   In-order:  10 25 30 50 60 75 80
   → Tìm Post-order?

3. Pre-order BST: 20 10 5 15 30 25 40
   → Vẽ cây và tìm In-order?
```

### Set 5: DFS/BFS
```
Cho đồ thị:
    A---B---C
    |   |   |
    D---E---F
    |       |
    G-------H

1. DFS từ A (thứ tự alphabet)
2. BFS từ A (thứ tự alphabet)
3. Lexicographically largest DFS từ H
```

### Set 6: Vẽ BST
Vẽ BST với các dãy sau:
1. 45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40
2. 100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87
3. 60, 40, 80, 20, 50, 70, 90, 10, 30, 45, 55, 65, 75, 85, 95

---

## PHẦN 10: ĐÁP ÁN MẪU CHO ĐỀ THI

### Câu 1: Định nghĩa (20đ)
*(Đã trình bày ở phần 1)*

### Câu 2: Chứng minh Euler path (10đ)
*(Đã trình bày ở phần 2)*

### Câu 3: Chứng minh Full Binary Tree (10đ)
*(Đã trình bày ở phần 2)*

### Câu 4: Duyệt cây (15đ)
**Cần xem hình trong đề gốc để giải**

### Câu 5: Xây dựng cây (10đ)
```
In-order:  12 1 11 7 8 0 6 10 9 2 4 5 3
Post-order: 12 11 8 7 1 10 9 6 5 3 4 2 0

Gốc = 0 (cuối Post-order)
Chia: [12 1 11 7 8] 0 [6 10 9 2 4 5 3]

Cây con trái:
In: 12 1 11 7 8
Post: 12 11 8 7 1
Gốc = 1
Chia: [12] 1 [11 7 8]
...

Cây con phải:
In: 6 10 9 2 4 5 3
Post: 10 9 6 5 3 4 2
Gốc = 2
...

Cây kết quả:
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

### Câu 6: DFS/BFS (10đ)
**DFS từ 6 (lexicographically largest):**
- Duyệt từ lớn đến nhỏ: 6 → 9 → 8 → 7 → 3 → 4 → 2 → 1 → 5 → 0
- (Cần xem đồ thị để xác định chính xác)

**BFS từ 6:**
- (Cần xem đồ thị để giải)

### Câu 7: Vẽ BST (15đ)
**Dãy:** 31, 20, 72, 96, 76, 13, 18, 78, 98, 26, 94, 97, 80, 1, 83, 38, 86

**Kết quả:** *(Cần vẽ trên giấy)*

---

## KẾT LUẬN VÀ LỜI KHUYÊN

### Điểm mạnh cần duy trì
1. ✓ Học thuộc định nghĩa chính xác
2. ✓ Hiểu rõ các bước chứng minh
3. ✓ Luyện tập nhiều bài tập tương tự
4. ✓ Quản lý thời gian tốt

### Các lỗi thường gặp cần tránh
1. ✗ Nhầm lẫn Pre/In/Post-order
2. ✗ Quên điều kiện Euler path (0 hoặc 2 đỉnh lẻ)
3. ✗ Vẽ BST sai thứ tự trái/phải
4. ✗ Xây dựng cây không đúng phân chia
5. ✗ DFS/BFS nhầm thứ tự duyệt

### Checklist trước khi thi
- [ ] Học thuộc 20 định nghĩa quan trọng
- [ ] Biết chứng minh 5 định lý cơ bản
- [ ] Làm thành thạo 10 bài duyệt cây
- [ ] Làm 15 bài xây dựng cây từ duyệt
- [ ] Làm 10 bài DFS/BFS
- [ ] Vẽ thành thạo 10 BST
- [ ] Ôn lại đề thi mẫu
- [ ] Chuẩn bị giấy nháp A4 viết tay

### Tài liệu tham khảo
1. Discrete Mathematics and Its Applications - Kenneth H. Rosen
2. Các slide bài giảng MATH202
3. File tổng hợp: TONG_HOP_TOAN_ROI_RAC_2.md

---

**Chúc bạn học tốt và đạt điểm cao! 🎓**

**Lưu ý:** Đề thi có thể thay đổi nhưng cấu trúc và dạng bài tương tự. Tập trung vào việc hiểu bản chất và luyện tập nhiều.
