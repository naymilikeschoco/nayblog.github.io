# 图（2）

### 1. 最短路径问题

#### 1.1 单源最短路径

**最短路径算法的核心技术是松弛**

**Bellman-Ford算法** 可以解决一般情况下的单源最短路径问题。
（边的权重可以为负值；且给定带权重的有向图，Bellman-Ford算法返回一个bool变量，表明是否存在一个从源节点可以到达的权重为负的环路（负圈））

```python
 def BellmanFord():   #运行时间：O(VE)
    for each v in V:
        d[v] = inf #初始化d
    d[s] = 0
    for i=1 to |V|-1:
        for each edge (u,v) in E: 
            #进行(|V|-1)次轮(why?)
            Relax(u,v, w(u,v)) #松弛每条边
    for each edge (u,v) in E:
        if (d[v] > d[u] + w(u,v)):
            return no_solution
            #检验结果。何时得到解?
            #没有从源节点可以到达的负圈时

def Relax(u,v,w): 
    if (d[v] > d[u]+w):
        d[v] = d[u]+w
```

![bb583c36-2181-4cce-b1fa-a614652e98df](file:///D:/Users/asus/Pictures/Typedown/bb583c36-2181-4cce-b1fa-a614652e98df.png)

![a1b9e709-bd37-455d-89f8-11be721574a9](file:///D:/Users/asus/Pictures/Typedown/a1b9e709-bd37-455d-89f8-11be721574a9.png)

**Bellman-Ford 算法——动态规划视角**

- 优化子结构：最短路径包含最短子路径
  重叠子问题：从s到x，可经过多条可能的路径（s-t-x，s-y-x，…），而不同的最短路径可能包含同样的子路径（子问题）

![14d26f24-2ca2-410c-b7ec-ff0f42ef09f6](file:///D:/Users/asus/Pictures/Typedown/14d26f24-2ca2-410c-b7ec-ff0f42ef09f6.png)

**改进：使用拓扑排序得到顶点扫描次序：**

![1e33a5eb-20e4-44de-a013-0ad106a15003](file:///D:/Users/asus/Pictures/Typedown/1e33a5eb-20e4-44de-a013-0ad106a15003.png)

![a338b332-dde0-4c14-aaf3-b62f3a29b6eb](file:///D:/Users/asus/Pictures/Typedown/a338b332-dde0-4c14-aaf3-b62f3a29b6eb.png)

**Dijkstra算法**

如果图中没有负边，Dijkstra算法可以超越Bellman-Ford算法

- 类似Best-First 搜索（章11）：从最小优先队列（最小堆）中取结点
  类似Prim算法（章8）：从源点逐渐扩展到所有结点，使用以d[v]为键的优先队列

![23dcfc65-3760-44f1-85b9-db05ab9a2ba7](file:///D:/Users/asus/Pictures/Typedown/23dcfc65-3760-44f1-85b9-db05ab9a2ba7.png)

**运行时间**是多少？取决于优先队列的实现方式

- 最小堆：
  ExtractMin和DecreaseKey操作时间复杂性都是logV，
  总时间为：O((V+E)lgV)

- 斐波那契堆: 
  Decrease-Key代价为O(1)，
  总时间为O(VlgV+E)

#### 1.2 任意两点最短路径

![46639c80-e235-43cf-8706-5d5246ed3fab](file:///D:/Users/asus/Pictures/Typedown/46639c80-e235-43cf-8706-5d5246ed3fab.png)

<img src="file:///D:/Users/asus/Pictures/Typedown/f9d4fb52-4e3e-405e-9cd9-37ad2dc40000.png" title="" alt="f9d4fb52-4e3e-405e-9cd9-37ad2dc40000" style="zoom:67%;">

![d2312b6d-012e-4eee-9764-1eb77439510e](file:///D:/Users/asus/Pictures/Typedown/d2312b6d-012e-4eee-9764-1eb77439510e.png)

![9ff11491-4dda-41f8-9ef2-659ee06968af](file:///D:/Users/asus/Pictures/Typedown/9ff11491-4dda-41f8-9ef2-659ee06968af.png)

<img src="file:///D:/Users/asus/Pictures/Typedown/11d3a648-2958-4c58-a1de-155958c3c3d2.png" title="" alt="11d3a648-2958-4c58-a1de-155958c3c3d2" style="zoom:50%;"><img src="file:///D:/Users/asus/Pictures/Typedown/0155a865-ae45-4ee8-89d1-f1b6eadbba8f.png" title="" alt="0155a865-ae45-4ee8-89d1-f1b6eadbba8f" style="zoom:50%;">

![281a6c1f-f371-4106-960b-c7c979d67e70](file:///D:/Users/asus/Pictures/Typedown/281a6c1f-f371-4106-960b-c7c979d67e70.png)



## 2. 网络流问题

![86b2be91-d4f2-4e2f-9f18-d4f2eef1eff1](file:///D:/Users/asus/Pictures/Typedown/86b2be91-d4f2-4e2f-9f18-d4f2eef1eff1.png)

基本思想：循环增加流的值

1. 初始，对于所有的边e，初始化流f(e)=0

2. 每一次迭代中，增加图中的流值，方法：在当前的余图（残存网络）中寻找一条增广路径，即符合条件的新流路径，从而增加流值

3. 不断迭代，直到不存在增广路径为止，即流值已经最大化

![b3583fd6-b591-4d68-8429-adf40de6149d](file:///D:/Users/asus/Pictures/Typedown/b3583fd6-b591-4d68-8429-adf40de6149d.png)

注意：从流图中计算最大流

<img src="file:///D:/Users/asus/Pictures/Typedown/8119d530-448b-40ad-828b-4b943d30d3f3.png" title="" alt="8119d530-448b-40ad-828b-4b943d30d3f3" style="zoom:50%;">

## 3. 匹配问题

二分图匹配

交替路：从一个未匹配点出发，依次经过非匹配边、匹配边、非匹配边…形成的路径叫交替路

增广路：从一个未匹配点出发，走交替路，如果终点为另一个未匹配点（出发的点不算），则这条交替路称为增广路。

- 增广路的路径长度必定为奇数,第一条边和最后一条边都不属于M。
  增广路经过取反操作,可以得到一个更大的匹配。
  M为二分图G的最大匹配当且仅当不存在相对于M的增广路径

**匈牙利算法**

基本步骤：

1. 置M为空;
2. 找出一条增广路径P,通过取反操作,得到更大的匹配。
3. 重复步骤2,直到找不出增广路为止
