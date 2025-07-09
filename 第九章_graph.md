# 图

## 图的存储结构

图的储存结构至少要保存两类信息：一是顶点的数据，二是顶点间的关系（邻接矩阵）

无向图（邻接矩阵<font color='purple'>对称</font>，可以压缩存储）

有向图（邻接矩阵的第i行1的个数为顶点i的出度，第j列1的个数为顶点j的入度）

<font color='purple'>邻接矩阵</font>——顺序存储，好处是顺序索引，查找快，劣势是对于稀疏图，占据储存空间大

<font color='purple'>邻接表</font>——链式存储

![72583619-a08e-4bfd-9691-2176048b5b8a](file:///D:/Users/asus/Pictures/Typedown/72583619-a08e-4bfd-9691-2176048b5b8a.png)

无向图的邻接表（不分出边和入边），图的边数：所有边链表结点个数之和的一半

对于无向图，插入一条边（i，j），需要插入两次：分别对顶点i和顶点j进行边的插入。

<font color='purple'>有向图的逆邻接表（入度）</font>：链表存弧尾



<font color='purple'>十字链表</font>——有向图（结合入边表和出边表

<font color='purple'>邻接多重表</font>——无向图的链式存储

邻接多重表和邻接表的区别：同一条边在邻接表中用两个结点表示（对应于两个顶点的边链表），而在邻接多重表中只用一个结点表示

<img src="file:///D:/Users/asus/Pictures/Typedown/55a11eb4-ce70-4a24-8c49-a58f83e6b566.png" title="" alt="55a11eb4-ce70-4a24-8c49-a58f83e6b566" style="zoom:50%;">

## 图的遍历

### DFS（深度优先搜索）

在该顶点的邻接点均被访问过之后，搜索**回溯**到有未被访问过的邻接点的顶点，再接着搜索

如何编程实现回溯过程呢？递归是否自带回溯呢？yes,采用递归算法实现搜索的回溯，并设置访问标志数组visited[]

（类似栈的一个次序）

```c
int visited[n];
graph g; //图用邻接矩阵储存
void DFS(int i){
    int j;
    printf("node:%c\n",g.vexs[i]);
    visited[i] = true;
    for(j=0;j<n;j++){ //没有访问过，才递归访问
        if((g.arcs[i][j]==1)&&(!visited[j]))
            DFS(j);
    }
}
```

```c
int visited[n];
vexnode g[n]; //图用邻接表储存
void DFSL(int i){
    int j;
    edgenode *p;
    printf("node:%c\n",g[i].vertex);
    visited[i] = true;
    p = g[i].link; //得到当前结点的一条边
    while(p!=NULL){ //存在边
        if(!visited[p->adjvex]) //边未被访问过
            DESL(p->adjvex);
        p = p->next;
    }
}
```

非连通图的DFS：首先将图中每个顶点的访问标志设为FALSE，之后搜索图中**每个**顶点。若已被访问过，则该顶点一定落在图中已求得的连通分量上；若还没被访问，则从该顶点出发遍历图，可求得图的另一个连通分量。

```c
TRAVER(){ //遍历用邻接矩阵表示的非连通图
    int i;
    for(i=0; i<n; i++)
        visited[i] = FALSE; //标志数组初始化 
    for(i=0; i<n; i++)
        if(!visited[i])  
            DFS(i); //从每一个顶点出发遍历一个连通分量           
}
```

利用深度优先搜索可以实现以下目标：
 (1) 判断图是否连通
 (2) 求图的连通分量

### BFS（广度优先搜索）

广度优先搜索BFS遍历类似于树的按层次遍历。

为了实现逐层访问，需设置一队列Q，以记忆正在访问的这一层和上一层的顶点，以便于向下一层访问。（控制遍历顶点的顺序
与深度优先搜索过程一样，为避免重复访问，需要一个辅助数组 visited [ ]，给被访问过的顶点加标记。入队列时，就把该元素置为已访问过。

```c
//如果使用邻接矩阵，则对于每一个被访问过的顶点，循环要检测矩阵中的 n 个元素，总的时间代价为O(n^2)
//图用邻接矩阵表示
void BFS(int k){
    int i,j;
    SETNULL(Q); //初始化队列
    ENQUEUE(Q,k); //当前访问节点入队
    visited[k] = true;
    while(!EMPTY(Q)){
        i = DEQUEUE(Q); //让当前结点出队
        for(j=0;j<n;j++){
            if((g.arc[i][j]==1)&&(!visited[j])){
                visited[j] = true;
                ENQUEUE(Q,j);
            }
        }
    }
}
```

```c
//图用邻接表表示
//时间复杂度为O(n+e)
BFSL(int k){
    int i; edgenode *p;
    SETNULL(Q);
    ENQUEUE(Q, k);
    visited[k]=TRUE;
    while(!EMPTY(Q)){ 
        i=DEQUEUE(Q);  
        p=g1[i].link;
        while(p!=NULL) {//访问p的整个链
            if(!visited[p->adjvex]){
                visited[p->adjvex]=TRUE;
                ENQUEUE(Q,p->adjvex);
            }
            p=p->next; 
        }  
    }
}
```



- 树的先根遍历是一种深度优先搜索策略，树的层次遍历是一种广度优先搜索策略。

- 深度优先或广度优先可用于求得无向图的生成树
  生成树可由遍历过程中所经过的边组成
  
  

### <font color='purple'>有向无环</font>图的应用

##### 1）拓扑排序

**什么是拓扑排序？** 对有向图给出的次序关系，将图中顶点排成一个**线性序列**，对于有向图中没有限定次序关系的顶点，则可以人为加上任意的次序关系。由此所的顶点的线性序列称之为拓扑有序序列

**拓扑排序算法的基本思想：**

(1)在有向图中选一个入度为零的顶点输出

(2)从图中删除该顶点及所有它的出边

(3)重复执行(1)(2)，直到全部顶点均已输出，或图中剩余顶点的入度均不为零（说明图中存在回路，无法继续拓扑排序）

**特点：**

(1)一个有向图的拓扑序列不一定唯一;
(2)有向无环图一定存在拓扑序列;
(3)有向有环图不存在拓扑序列;
*(4)通过构造拓扑序列，可判定AOV网是否存在环。*

**数据结构**：使用邻接表（出边表）存图，用一个数组存放顶点入度，用一个栈存放入度为0的顶点

![798618dd-be0f-423b-8a93-4282961ef974](file:///D:/Users/asus/Pictures/Typedown/798618dd-be0f-423b-8a93-4282961ef974.png)

![ab138391-34ee-4343-b18e-cf7fc4f15cd5](file:///D:/Users/asus/Pictures/Typedown/ab138391-34ee-4343-b18e-cf7fc4f15cd5.png)

```c
//拓扑排序算法
Status TopologicalSort(ALGraph G){
    SqStack S;
    int count,k,i;
    FindInDegree(G,indegree);
    InitStack(S);
    for(i=0; i<G.Vexnum; ++i){// 建零入度顶点栈S
         if (!indegree[i]) Push(S, i);}// 入度为0者进栈
    count = 0;// 对输出顶点计数  
    while(!StackEmpty(S)){
         Pop(S, i); 
         printf(i, G.Vertices[i].data);  ++count; //输入i号顶点并计数 
         for(p=G.vertices[i].firstarc; p; p=p->nextarc){//对i号顶点的每个邻接点的入度减1     
              k = p->adjvex；
              if(!(--indegree[k])) Push(S, k); //入度为0的入栈
         }
    }
    if (count<G.Vexnum) return ERROR;    //有回路
    else return OK;
}
```

拓扑排序算法的时间复杂度为O(n+e)

拓扑排序--AOV网表示各工序的先后关系

##### 2）关键路径

AOE网：带权的有向无环图，顶点表示事件，边表示活动，权表示活动持续的时间。AOE用来估算工程的完成时间。每个事件表示在它之前的活动已经完成，在它之后的活动可以开始。

AOE网的特点：

(1)表示实际工程计划的AOE网应该是无回路的;
(2)只有一个入度为零的顶点(称作源点),表示整个活动开始;
(3)只有一个出度为零的顶点(称作汇点)表示整个活动结束。

关键路径：在AOE 网中，路径长度最长的路径称为关键路径。关键路径上的活动都是关键活动（关键工程）。

事件的最早发生时间：是从源点v1到vk的最长路径长度，记作ve(k)，为事件vk的最早发生时间。这个长度决定了所有从顶点vk发出的活动能够开工的**最早**时间。

<img title="" src="file:///D:/Users/asus/Pictures/Typedown/1ac5ba04-66f9-4cde-9a06-7934cb1cef16.png" alt="1ac5ba04-66f9-4cde-9a06-7934cb1cef16" style="zoom:67%;">

事件的最迟发生时间——vl(k)：是指在不推迟整个工期的前提下,事件vk允许的最晚发生时间。从后往回计算(从汇点开始计算)，vl(k) = vn的最早发生时间ve(n)-vk到vn的最长路径长度

<img src="file:///D:/Users/asus/Pictures/Typedown/b0c7f457-b8a7-4b57-970d-f61ff154e592.png" title="" alt="b0c7f457-b8a7-4b57-970d-f61ff154e592" style="zoom:67%;">

如果一个顶点的最晚时间和最早时间一样，说明它<font color='purple'>在</font>关键路径上。

活动的最早开始时间——e[i]：若活动ai是由弧$<vk，vj>$表示，则活动ai的最早开始时间应等于事件vk的最早发生时间。因此，有：e[i] = ve[k]。

活动的最晚开始时间——l[i]：在不推迟整个工期的前提下，ai必须开始的最晚时间。若ai由弧$<vk，vj>$表示，则ai的最晚开始时间要保证事件vj的最迟发生时间不拖后。因此，等于vj的最迟发生时间减去$<vk，vj>$的持续时间即，

l[i]=vl[j]-dut$<vk，vj>$

最早开始时间=最晚开始时间的活动为关键活动。

**求关键活动算法要点**：

(1) 求出每个事件i的最早发生时间ve(i)和最晚发生vl(i)
(2) 求出每个活动最早开始时间e(i)和最晚开始时间l(i):
    e(i)=ve[j]
    l(i)=vl[k]-dut($<j,k>$)

(3) 比较e(i)和l(i)， e(i)和l(i)相等的活动即为关键活动



<font color='purple'>求ve的顺序是按拓扑有序的次序；求vl的顺序是按拓扑逆序的次序。</font>（拓扑逆序序列即为拓扑有序序列的逆序列）（方法：在拓扑排序的过程中，另设一个栈记下拓扑有序序列，*栈* 取出顶点的次序即逆序）

```c
status TopologicalOrder(ALGraph G, Stack &T){
    //修改后的拓扑排序只是添加了求事件的最早发生时间
    Stack S;int count, k;
    char indegree[40];  ArcNode *p;
    InitStack(S); // S为零入度顶点栈
    FindInDegree(G, indegree); 
    for(int j=0; j<G.vexnum; ++j) 
        if(indegree[j]==0) Push(S, j); //建零入度顶点栈S， 入度为0者进栈 
    InitStack(T); //建拓扑序列顶点栈T
    count = 0;  
    for(int i=0; i<G.vexnum; i++) ve[i] = 0; // 初始化
    while(!StackEmpty(S)){
        Pop(S, j);  Push(T, j);  ++count; //顶点j入T栈并计数
        for(p=G.vertices[j].firstarc;  p;  p=p->nextarc) { 
            k = p->adjvex;
            if(--indegree[k] == 0) Push(S, k); // 对j的每个邻接点的入度减1，若入度减为0，则入栈
            if(ve[j]+(p->info) > ve[k])  //求事件的最早发生时间ve
                ve[k] = ve[j]+(p->info);  // *p->info=dut(<j,k>)
        }// for   
    }//while
        if (count<G.vexnum) return ERROR; // 有回路
        else return OK;
} // TopologicalOrder

//求事件的最迟发生时间和关键路径
Status CriticalPath(ALGraph G){  // G为有向网，输出G的各项关键活动。
    Stack T;
    int a,j,k,el,ee,dut;
    char tag;
    ArcNode *p;
    if(!TopologicalOrder(G, T)) 
        return ERROR;
    for(a=0; a<G.vexnum; a++) // 初始化顶点事件的最迟发生时间
        vl[a] = ve[G.vexnum-1]; 
    while(!StackEmpty(T)){  //按拓扑逆序求各顶点的vl值，出栈次序正好为拓扑逆序
        for(Pop(T, j), p=G.vertices[j].firstarc; p; p=p->nextarc){
            k=p->adjvex;  dut=p->info; //dut<j,k>
            if(vl[k]-dut < vl[j])  vl[j] = vl[k]-dut;
        }// for
    }
    for(j=0; j<G.vexnum; ++j){ // 求ee,el和关键活动
        for(p=G.vertices[j].firstarc; p; p=p->nextarc){
            k=p->adjvex;  dut=p->info;   
            ee = ve[j];  el = vl[k]-dut;
            tag = (ee==el) ? '*' : ' ';
            printf(j, k, dut, ee, el, tag); // 输出关键活动
        }
    }
    return OK;
}// CriticalPath
```

在拓扑排序求ve[i]和逆拓扑有序求vl[i]时, 所需时间为O(n+e)；求各个活动的e[k]和l[k]时所需时间为O(e)；
总共花费时间仍然是O(n+e)。

<img src="file:///D:/Users/asus/Pictures/Typedown/f49014c0-cf27-406e-9f17-0b5fcdbb4db4.png" title="" alt="f49014c0-cf27-406e-9f17-0b5fcdbb4db4" style="zoom:80%;">

求了关键路径上的顶点，还要具体求出关键活动才能得知关键路径（可能不止一条


