

### 2. Graph Integration

- Two problems:

  1. Pipeline model : dependent on basic embedding effect
  2. Joint model :
    - GNN-separate model    : only local stability
    - GNN-joint model       : hubness problem (Reduction to KGC task)

---

### 2.1 Task - Graph Integration

- Solution to GNN-separate model :

  1. Change the local structure with alignment information
  2. Training to global stability
  3. Repeat

- Problem :

  1. High computational complexity
  2. Thus : Need a fast convergence methods

---

### 2.1 Task - Graph Integration

- Solution GNN-joint (KGC):
  - In next section

- Problem :
  - Can't be used with cohesive sampling

---

### 2.2 Task - Graph Knowledge Completion

- Motivation:
  - Hubness problem
  - Half-concat > non-concat

---

### 2.2 Task - Graph Knowledge Completion

- Why Half-concat > non-concat : last time

  - Not a mapping between two space : $\mathcal{X} \to \mathcal{Y}$
  - A mapping by space-node pair :  $(\mathcal{X}, e\_i) \to (\mathcal{Y}, e\_i)$


---

### 2.2 Task - Graph Knowledge Completion

- Why Half-concat > non-concat : now

  - Not a mapping space-node pair : $\mathcal{X} \to \mathcal{Y}$
  - A mapping by region :  $\mathcal{R}\_{\mathcal{X}} \to \mathcal{R}\_{\mathcal{Y}}$
    - $\mathcal{R}\_{\mathcal{X}}$ : A subspace(region) of $\mathcal{X}$
    - Need to improve

---

### 2.2 Task - Graph Knowledge Completion

- A mapping by region :

<img src="./pictures/1" align='middle' alt="drawing" width="500"/>

---

### 2.2 Task - Graph Knowledge Completion

- New Method :
  - Design a sampling method and a loss function to incorporate this prior knowledge.
  - Make nodes in different region be far

---

### 2.3 Task - KBG methods analysis

- Motivation
  - Lack analysis on graph itself

---

### 2.3 Task - KBG methods analysis

- Analysis
  - Three variables with each methods:
    - Knowledge Graph Embedding methods : $\mathcal{M}$
    - Input graphs and alignment : $\mathcal{G}$
    - Concat | Half-concat | Non-concat : $\mathcal{N}$
  - One input : accuary : $\mathcal{A}$
  - Based on Graph Integration Task with simple neural methods : $\mathcal{A} = \mathcal{L}_{(\mathcal{G}, \mathcal{N})} (\mathcal{M})$

---

### 3. Future work

- Verification of scale-free in KG
- Verification of regionality of mapping
- Improve transE with new method

---

<!-- ### 4. Verification of regionality of mapping

利用合成网络去测试, 网络的种类可以再分析
利用 Auto-encoder 和 VAE 的结果的比较去进行分析. -->

---
<!--
### 4. 其他的点 -->

<!-- - 如果可以验证局部稳定性的话就可以向各种方法中加入潜变量用来增强, 即每个边的变量不是固定的, 而是按照其周围的信息进行加强, 这个非常适合 GNN. -->
