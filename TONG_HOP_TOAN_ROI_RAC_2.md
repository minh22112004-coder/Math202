# TỔNG HỢP TOÁN RỜI RẠC 2 (DISCRETE MATHEMATICS 2)

## MỤC LỤC

1. [Đồ Thị (Graphs)](#1-đồ-thị-graphs)
2. [Cây (Trees)](#2-cây-trees)
3. [Duyệt Đồ Thị (Graph Traversal)](#3-duyệt-đồ-thị-graph-traversal)
4. [Sắp Xếp Tô-pô (Topological Sorting)](#4-sắp-xếp-tô-pô-topological-sorting)

---

## 1. ĐỒ THỊ (GRAPHS)

### 1.1. Định nghĩa cơ bản

#### Đồ thị đơn (Simple Graph)
**Định nghĩa:** Một đồ thị đơn G = (V, E) bao gồm:
- **V**: Tập hợp không rỗng các đỉnh (vertices)
- **E**: Tập hợp các cặp không có thứ tự của các phần tử khác nhau trong V, gọi là cạnh (edges)

**Đặc điểm:**
- Là đồ thị vô hướng (undirected graph)
- Cạnh luôn là "hai chiều"
- Không có cạnh song song (multiple edges)
- Không có khuyên (loops)

**Số cạnh tối đa:** Trong đồ thị đơn có n đỉnh, số cạnh tối đa là: **C(n,2) = n(n-1)/2**

#### Đa đồ thị (Multigraph)
**Định nghĩa:** Trong đa đồ thị G = (V, E), hai hoặc nhiều cạnh có thể kết nối cùng một cặp đỉnh.

**Ứng dụng:** 
- Biểu diễn nhiều đường dây điện thoại giữa hai máy tính trong mạng
- Mạng lưới giao thông có nhiều tuyến đường giữa hai điểm

#### Đồ thị có hướng (Directed Graph)
**Định nghĩa:** Trong đồ thị có hướng G = (V, E), các cạnh là các cặp có thứ tự của các đỉnh (không nhất thiết phải khác nhau).

**Ứng dụng:**
- Biểu diễn đường dây điện thoại một chiều
- Luồng dữ liệu
- Quan hệ phụ thuộc

#### Đa đồ thị có hướng (Directed Multigraph)
**Định nghĩa:** Kết hợp đặc điểm của đồ thị có hướng và đa đồ thị - có thể có nhiều cạnh cùng hướng giữa hai đỉnh.

#### Đồ thị có trọng số (Weighted Graph)
- Mỗi cạnh có một trọng số (weight) hoặc chi phí (cost)
- Thường là số nguyên không âm
- Một số đồ thị cho phép trọng số âm

### 1.2. Các khái niệm quan trọng

#### Đỉnh kề nhau (Adjacent Vertices/Neighbors)
**Định nghĩa:** Hai đỉnh u và v trong đồ thị vô hướng G được gọi là kề nhau (hoặc là hàng xóm) nếu {u, v} là một cạnh của G.

**Cạnh liên thuộc:** Một cạnh e kết nối u và v được gọi là liên thuộc với các đỉnh u và v, hoặc được nói là kết nối u và v. Các đỉnh u và v được gọi là các điểm cuối của cạnh {u, v}.

#### Bậc của đỉnh (Degree of a vertex)
**Định nghĩa:** Bậc của một đỉnh trong đồ thị vô hướng là số cạnh liên thuộc với nó, ngoại trừ khuyên tại một đỉnh đóng góp hai lần vào bậc của đỉnh đó.

**Ký hiệu:** deg(v)

**Quy ước đặc biệt:**
- Khuyên (loop) đóng góp 2 vào bậc của đỉnh
- Đỉnh cô lập (không có cạnh nào): deg(v) = 0

**Định lý bắt tay (Handshaking Theorem):**
```
Σ deg(v) = 2|E|
```
Tổng bậc của tất cả các đỉnh = 2 × số cạnh

#### Bậc trong đồ thị có hướng
- **Bậc vào (in-degree):** Số cạnh đi vào đỉnh
- **Bậc ra (out-degree):** Số cạnh đi ra khỏi đỉnh

---

## 2. CÂY (TREES)

### 2.1. Định nghĩa

**Định nghĩa 1:** Cây là một đồ thị vô hướng liên thông không có chu trình đơn.

**Định lý 1:** Một đồ thị vô hướng là cây khi và chỉ khi có một đường đi đơn duy nhất giữa bất kỳ hai đỉnh nào của nó.

### 2.2. Cây có gốc (Rooted Tree)

**Tạo cây có gốc:**
1. Chỉ định một đỉnh làm gốc (root)
2. Hướng mỗi cạnh ra khỏi gốc
3. Kết quả là một đồ thị có hướng gọi là cây có gốc

**Lưu ý:** Chọn gốc khác nhau sẽ tạo ra các cây có gốc khác nhau.

### 2.3. Các khái niệm quan trọng

#### Nút lá (Leaf nodes)
- Các nút không có con
- Còn gọi là nút cuối (terminal nodes)

#### Nút nội (Internal vertices)
- Các đỉnh có con
- Không phải là nút lá

#### Nút anh em (Sibling nodes)
- Các nút có cùng cha

#### Cây con (Subtree)
- Cây con tại đỉnh v là đồ thị con của cây bao gồm đỉnh v và tất cả các con cháu của nó và tất cả các cạnh liên thuộc với các con cháu đó

#### Mức (Level)
- **Mức 0:** Gốc
- **Mức 1:** Con của gốc
- **Mức 2:** Cháu của gốc
- Và cứ thế tiếp tục...

#### Chiều cao của cây (Height)
- Mức lớn nhất trong cây
- Chiều cao = số mức - 1

### 2.4. Cây nhị phân (Binary Tree)

**Định nghĩa:** Một cây có gốc được gọi là cây nhị phân nếu mỗi đỉnh nội có không quá 2 con.

#### Cây nhị phân đầy đủ (Full Binary Tree)
- Mỗi đỉnh nội có đúng 2 con

**Số nút tối đa trong cây nhị phân cao H:**
- Tổng số nút: 2^(H+1) - 1
- Số lá tối đa: 2^H

**Tính chất quan trọng:**
1. Trong cây nhị phân đầy đủ, số đỉnh luôn là số lẻ
2. Số lá = số đỉnh nội + 1

### 2.5. Cây tìm kiếm nhị phân (Binary Search Tree - BST)

**Tính chất:**
- Tất cả giá trị ở cây con bên trái < giá trị nút gốc
- Tất cả giá trị ở cây con bên phải > giá trị nút gốc
- Mỗi cây con cũng là BST

### 2.6. Các phương pháp duyệt cây

#### 1. Duyệt tiền tự (Pre-order)
**Thứ tự:** Gốc → Trái → Phải
```
Thuật toán:
1. Thăm nút gốc
2. Duyệt cây con trái
3. Duyệt cây con phải
```

#### 2. Duyệt trung tự (In-order)
**Thứ tự:** Trái → Gốc → Phải
```
Thuật toán:
1. Duyệt cây con trái
2. Thăm nút gốc
3. Duyệt cây con phải
```
**Đặc biệt:** Duyệt in-order trên BST cho kết quả các giá trị theo thứ tự tăng dần.

#### 3. Duyệt hậu tự (Post-order)
**Thứ tự:** Trái → Phải → Gốc
```
Thuật toán:
1. Duyệt cây con trái
2. Duyệt cây con phải
3. Thăm nút gốc
```

### 2.7. Bài tập quan trọng

1. **Xác định cây:** Liệt kê 3 cách kiểm tra một đồ thị vô hướng là cây
   - Kiểm tra liên thông và không có chu trình
   - Kiểm tra có n-1 cạnh và liên thông (với n đỉnh)
   - Kiểm tra có đường đi duy nhất giữa mọi cặp đỉnh

2. **Xây dựng cây từ duyệt:**
   - Cho pre-order và in-order → xây dựng cây → tìm post-order
   - Cho post-order và in-order → xây dựng cây → tìm pre-order
   - Cho pre-order của BST → xây dựng cây

---

## 3. DUYỆT ĐỒ THỊ (GRAPH TRAVERSAL)

### 3.1. Khái niệm

**Graph Traversal (Graph Search)** là quá trình thăm (kiểm tra và/hoặc cập nhật) mỗi đỉnh trong đồ thị. Các phép duyệt được phân loại theo thứ tự thăm các đỉnh.

**Ứng dụng:**
- Tìm đường đi giữa hai đỉnh
- Giải mê cung (maze traversal)
- Bài toán "bạn của bạn" (friend of friend problem)
- Kiểm tra tính liên thông
- Tìm chu trình

### 3.2. Tìm kiếm theo chiều sâu (DFS - Depth First Search)

#### Định nghĩa
DFS là thuật toán duyệt đồ thị hữu hạn. DFS thăm các đỉnh con trước khi thăm các đỉnh anh em; nghĩa là, nó duyệt chiều sâu của bất kỳ đường đi cụ thể nào trước khi khám phá chiều rộng của nó.

#### Cấu trúc dữ liệu
Thường sử dụng **ngăn xếp (stack)** - thường là call stack của chương trình thông qua đệ quy.

#### Thuật toán DFS (Đệ quy)
```
DFS(v):
    đánh dấu v đã thăm
    xử lý v
    for each hàng xóm u của v:
        if u chưa được thăm:
            DFS(u)
```

#### Thuật toán DFS (Lặp - dùng Stack)
```
DFS(start):
    tạo stack S
    đẩy start vào S
    while S không rỗng:
        v = lấy phần tử từ S
        if v chưa được thăm:
            đánh dấu v đã thăm
            xử lý v
            for each hàng xóm u của v (theo thứ tự ngược):
                if u chưa được thăm:
                    đẩy u vào S
```

### 3.3. Các thứ tự duyệt trong DFS

#### 1. Preordering
Danh sách các đỉnh theo thứ tự mà chúng được thăm **lần đầu tiên** bởi DFS.

**Ví dụ:** A B D C hoặc A C D B

#### 2. Postordering
Danh sách các đỉnh theo thứ tự mà chúng được thăm **lần cuối cùng** bởi thuật toán.

**Ví dụ:** D B C A hoặc D C B A

#### 3. Reverse Postordering
Đảo ngược của postordering, tức là danh sách các đỉnh theo thứ tự ngược lại của lần thăm cuối cùng.

**Lưu ý:** Reverse postordering **KHÔNG** giống với preordering.

**Ví dụ:** A C B D hoặc A B C D

### 3.4. Tìm kiếm theo chiều rộng (BFS - Breadth First Search)

Mặc dù tài liệu tập trung vào DFS, BFS cũng là phương pháp duyệt quan trọng:

**Đặc điểm:**
- Thăm tất cả các đỉnh ở mức k trước khi thăm các đỉnh ở mức k+1
- Sử dụng **hàng đợi (queue)** thay vì stack
- Tìm đường đi ngắn nhất trong đồ thị không có trọng số

### 3.5. Call Stack trong DFS

DFS đệ quy sử dụng call stack để:
- Lưu trữ trạng thái của các lời gọi hàm
- Quay lui (backtrack) khi không còn đỉnh nào để thăm
- Duy trì thứ tự duyệt

---

## 4. SẮP XẾP TÔ-PÔ (TOPOLOGICAL SORTING)

### 4.1. Đồ thị phi chu trình có hướng (DAG - Directed Acyclic Graph)

**Định nghĩa:** DAG là đồ thị có hướng không chứa bất kỳ chu trình nào.

**Ứng dụng:**
- Lập lịch tác vụ (task scheduling) - ví dụ: hệ thống build, môn học tiên quyết
- Pipeline xử lý dữ liệu
- Giải quyết phụ thuộc (Dependency Resolution) - ví dụ: npm
- Hệ thống quản lý phiên bản (ví dụ: lịch sử commit trong Git)
- Các thuật toán sắp xếp tô-pô

### 4.2. Định nghĩa Topological Sort

**Topological Sort** của một DAG là một thứ tự tuyến tính của các đỉnh sao cho với mỗi cạnh có hướng u→v, đỉnh u đến trước v trong thứ tự.

**Tính chất quan trọng:**
- Mọi DAG hữu hạn đều có topological sort
- Sắp xếp tô-pô **không thể thực hiện** nếu đồ thị không là DAG (có chu trình)
- Có thể có nhiều thứ tự tô-pô hợp lệ cho cùng một đồ thị

**Ví dụ:**
```
Đồ thị: 1→3→5
        2→4→6
        
Các topological sort hợp lệ:
- T = (1, 3, 2, 5, 4, 6)
- T = (1, 2, 3, 5, 4, 6)
- T = (1, 2, 3, 4, 5, 6)
```

### 4.3. Các ứng dụng thực tế

#### 1. Hệ thống Build
IDE như Eclipse, NetBeans phải build project với nhiều thư viện phụ thuộc lẫn nhau. Topological Sort giúp xác định thứ tự các thư viện nên được build hoặc include.

#### 2. Advanced Packaging Tool (APT)
Trong Linux, apt-get cài đặt phần mềm với các phụ thuộc. Topological Sort đảm bảo các gói được cài đặt theo đúng thứ tự phụ thuộc.

#### 3. Task Scheduling
Hữu ích cho việc lập lịch các tác vụ có phụ thuộc. Giúp xác định chuỗi thực thi tác vụ đúng.

#### 4. Bài toán tiên quyết (Prerequisite Problems)
Phổ biến trong giáo dục hoặc quy trình làm việc: một số tác vụ yêu cầu các tác vụ khác phải hoàn thành trước.

**Ví dụ:** Phải hoàn thành môn "Thuật toán cơ bản" trước "Thuật toán nâng cao".

### 4.4. Thuật toán Kahn

#### Ý tưởng
Thuật toán Kahn hoạt động bằng cách liên tục tìm các đỉnh không có cạnh đi vào, loại bỏ chúng khỏi đồ thị, và cập nhật các cạnh đi vào của các đỉnh được kết nối từ các cạnh đã loại bỏ. Quá trình này tiếp tục cho đến khi tất cả các đỉnh đã được sắp xếp.

#### Thuật toán
```
Kahn's Algorithm:
1. Tính bậc vào (in-degree) của mỗi đỉnh
2. Thêm tất cả các đỉnh có bậc vào = 0 vào hàng đợi Q
3. Khởi tạo danh sách rỗng topo_order
4. While Q không rỗng:
   a) Loại bỏ một nút v từ Q và thêm nó vào topo_order
   b) Với mỗi cạnh đi ra từ v, giảm bậc vào của đỉnh đích w đi 1
   c) Nếu bậc vào của w trở thành 0, thêm w vào hàng đợi
5. Nếu hàng đợi rỗng và vẫn còn nút trong đồ thị, đồ thị chứa chu trình và không thể sắp xếp tô-pô
6. topo_order biểu diễn thứ tự tô-pô của đồ thị
```

#### Độ phức tạp
- **Thời gian:** O(V + E) với V là số đỉnh, E là số cạnh
- **Không gian:** O(V)

#### Ví dụ minh họa
```
Đồ thị:
1 → 3 → 5
2 → 4 → 6

Bước 1: Tính in-degree
- Đỉnh 1: in-degree = 0
- Đỉnh 2: in-degree = 0
- Đỉnh 3: in-degree = 1
- Đỉnh 4: in-degree = 1
- Đỉnh 5: in-degree = 1
- Đỉnh 6: in-degree = 1

Bước 2: Q = [1, 2], topo_order = []

Bước 3: Lấy 1 ra
- Q = [2], topo_order = [1]
- Giảm in-degree của 3: in-degree(3) = 0
- Q = [2, 3]

Bước 4: Lấy 2 ra
- Q = [3], topo_order = [1, 2]
- Giảm in-degree của 4: in-degree(4) = 0
- Q = [3, 4]

... và cứ tiếp tục như vậy

Kết quả: topo_order = [1, 2, 3, 4, 5, 6]
```

### 4.5. Thuật toán DFS cho Topological Sort

Ngoài thuật toán Kahn, có thể sử dụng DFS để tìm topological sort:

**Ý tưởng:**
1. Thực hiện DFS trên đồ thị
2. Khi hoàn thành duyệt một đỉnh (postorder), thêm nó vào đầu danh sách kết quả
3. Hoặc thêm vào cuối và đảo ngược (reverse postorder)

**Thuật toán:**
```
TopologicalSort_DFS():
    khởi tạo tất cả đỉnh là chưa thăm
    khởi tạo stack rỗng
    for each đỉnh v:
        if v chưa được thăm:
            DFS_Visit(v)
    return stack (hoặc đảo ngược)

DFS_Visit(v):
    đánh dấu v đã thăm
    for each hàng xóm u của v:
        if u chưa được thăm:
            DFS_Visit(u)
    thêm v vào stack
```

**Độ phức tạp:** O(V + E)

### 4.6. Phát hiện chu trình

Khi thực hiện topological sort:
- Nếu **không** sắp xếp được tất cả các đỉnh → Đồ thị có chu trình
- Trong thuật toán Kahn: Nếu `|topo_order| < |V|` → có chu trình
- Trong DFS: Nếu gặp cạnh ngược (back edge) → có chu trình

---

## TÓM TẮT CÁC KHÁI NIỆM QUAN TRỌNG

### Công thức và Định lý

1. **Định lý bắt tay:** Σ deg(v) = 2|E|

2. **Số cạnh tối đa trong đồ thị đơn:** C(n,2) = n(n-1)/2

3. **Số nút tối đa trong cây nhị phân cao H:** 2^(H+1) - 1

4. **Trong cây nhị phân đầy đủ:** Số lá = Số đỉnh nội + 1

5. **Đồ thị là cây ⟺** Có đường đi duy nhất giữa mọi cặp đỉnh

6. **Cây với n đỉnh** có đúng n-1 cạnh

### Các thuật toán chính

| Thuật toán | Độ phức tạp | Cấu trúc dữ liệu | Ứng dụng |
|------------|-------------|------------------|----------|
| DFS | O(V + E) | Stack | Duyệt đồ thị, tìm chu trình, topological sort |
| BFS | O(V + E) | Queue | Đường đi ngắn nhất, duyệt theo mức |
| Kahn's Algorithm | O(V + E) | Queue | Topological sort |

### So sánh DFS và BFS

| Tiêu chí | DFS | BFS |
|----------|-----|-----|
| Cấu trúc | Stack (đệ quy) | Queue |
| Chiến lược | Đi sâu trước | Đi rộng trước |
| Đường đi | Không đảm bảo ngắn nhất | Đường đi ngắn nhất (không có trọng số) |
| Bộ nhớ | O(h) với h = chiều cao | O(w) với w = độ rộng |
| Ứng dụng | Tìm chu trình, topological sort | Đường đi ngắn nhất |

---

## BÀI TẬP THỰC HÀNH

### Về Đồ thị
1. Cho đồ thị, tính bậc của tất cả các đỉnh
2. Chứng minh số đỉnh bậc lẻ là số chẵn
3. Xác định loại đồ thị (simple, multigraph, directed, etc.)

### Về Cây
1. Duyệt cây với BFS và DFS từ một đỉnh cho trước
2. Xác định mức của mỗi nút và chiều cao của cây
3. Vẽ BST khi chèn các số theo thứ tự cho trước
4. Cho pre-order và in-order, xây dựng cây và tìm post-order
5. Cho post-order và in-order, xây dựng cây và tìm pre-order
6. Cho pre-order của BST, xây dựng cây và tìm post-order

### Về Graph Traversal
1. In DFS và BFS từ đỉnh cho trước
2. In lexicographically largest/smallest DFS
3. Xác định preorder, postorder, reverse postorder
4. Tìm đường đi giữa hai đỉnh

### Về Topological Sort
1. Thực hiện topological sort bằng thuật toán Kahn
2. Thực hiện topological sort bằng DFS
3. Kiểm tra đồ thị có chu trình không
4. Tìm tất cả các topological order có thể

---

## KẾT LUẬN

Toán Rời Rạc 2 tập trung vào các cấu trúc đồ thị và cây - những khái niệm nền tảng trong khoa học máy tính. Các chủ đề chính bao gồm:

1. **Đồ thị:** Hiểu các loại đồ thị và tính chất của chúng
2. **Cây:** Cấu trúc dữ liệu phân cấp quan trọng với nhiều ứng dụng
3. **Duyệt đồ thị:** DFS và BFS là nền tảng cho nhiều thuật toán phức tạp
4. **Topological Sort:** Giải quyết bài toán sắp xếp với ràng buộc phụ thuộc

Việc nắm vững các khái niệm này là cơ sở để học các môn nâng cao như Thuật toán, Cấu trúc dữ liệu, Đồ họa máy tính, AI, và nhiều lĩnh vực khác.

---

**Lưu ý:** Tài liệu này được tổng hợp từ các slide bài giảng. Để hiểu sâu hơn, bạn nên:
- Thực hành các bài tập
- Cài đặt các thuật toán bằng ngôn ngữ lập trình
- Tham khảo sách giáo khoa chính thức
- Làm bài tập trên các nền tảng như LeetCode, HackerRank

**Nguồn:** Discrete Mathematics and Its Applications - Kenneth H. Rosen, và các slide bài giảng MATH202
