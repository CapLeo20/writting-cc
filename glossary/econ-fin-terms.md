# 经济学、金融学术语表（v0.1）

**用途**：Claude 回复和写作时统一用这里的中文译名。第一次出现写"中文（英文或缩写）"，之后只用中文或通行缩写。

**基准**：范里安《微观经济学：现代观点》、戴维·罗默《高级宏观经济学》、伍德里奇《计量经济学导论：现代观点》的中译本，以及国内中文期刊的通行用法。

**状态**：v0.1 由 Claude 按通行用法整理，**尚未逐条对照三本中译本核对**。核对过的条目在"核对"列标 ✓。发现译名有出入时，以教材中译本和目标期刊近年用法为准，并在"备注"写明。

**规则**：

1. 有通行中文译名的用中文；没有的直接用英文，不自造译名。
2. 估计方法、检验名称的缩写（OLS、IV、DID、GMM）在中文期刊里可以直接用，第一次出现给全称。
3. 人名构成的方法名保留中文音译加英文，如"豪斯曼（Hausman）检验"；常见的也可以只写英文，全文统一即可。

## 1. 微观经济学

| 英文 | 中文 | 核对 | 备注 |
| --- | --- | --- | --- |
| utility / marginal utility | 效用 / 边际效用 | | |
| preference | 偏好 | | |
| indifference curve | 无差异曲线 | | |
| budget constraint | 预算约束 | | |
| marginal rate of substitution (MRS) | 边际替代率 | | |
| income effect / substitution effect | 收入效应 / 替代效应 | | |
| Slutsky equation | 斯勒茨基方程 | | |
| consumer surplus / producer surplus | 消费者剩余 / 生产者剩余 | | |
| elasticity | 弹性 | | |
| production function | 生产函数 | | |
| returns to scale | 规模报酬 | | |
| marginal cost | 边际成本 | | |
| perfect competition / monopoly / oligopoly | 完全竞争 / 垄断 / 寡头垄断 | | |
| price discrimination | 价格歧视 | | |
| deadweight loss | 无谓损失 | | |
| general equilibrium | 一般均衡 | | |
| Pareto efficiency | 帕累托效率 | | |
| externality | 外部性 | | |
| public good | 公共品 | | |
| asymmetric information | 信息不对称 | | |
| adverse selection / moral hazard | 逆向选择 / 道德风险 | | |
| principal–agent | 委托—代理 | | |
| signaling / screening | 信号传递 / 信息甄别 | | |
| Nash equilibrium | 纳什均衡 | | |
| dominant strategy | 占优策略 | | |
| subgame perfect equilibrium | 子博弈精炼纳什均衡 | | |
| mechanism design / incentive compatibility | 机制设计 / 激励相容 | | |

## 2. 宏观经济学

| 英文 | 中文 | 核对 | 备注 |
| --- | --- | --- | --- |
| Solow model | 索洛模型 | | |
| steady state / balanced growth path | 稳态 / 平衡增长路径 | | |
| golden rule | 黄金律 | | |
| Ramsey–Cass–Koopmans model | 拉姆齐—卡斯—库普曼斯模型 | | |
| overlapping generations (OLG) | 世代交叠模型 | | |
| endogenous growth | 内生增长 | | |
| human capital | 人力资本 | | |
| total factor productivity (TFP) | 全要素生产率 | | 首次写全称，之后可用 TFP |
| real business cycle (RBC) | 实际经济周期 | | |
| nominal rigidity | 名义刚性 | | |
| New Keynesian Phillips curve | 新凯恩斯菲利普斯曲线 | | |
| dynamic stochastic general equilibrium (DSGE) | 动态随机一般均衡 | | |
| Euler equation | 欧拉方程 | | |
| transversality condition | 横截性条件 | | |
| Ricardian equivalence | 李嘉图等价 | | |
| time inconsistency | 时间不一致 | | |
| Taylor rule | 泰勒规则 | | |
| zero lower bound / liquidity trap | 零利率下限 / 流动性陷阱 | | |
| output gap | 产出缺口 | | |
| natural rate of unemployment | 自然失业率 | | |
| permanent income hypothesis | 持久收入假说 | | |
| consumption smoothing / precautionary saving | 消费平滑 / 预防性储蓄 | | |
| impulse response | 脉冲响应 | | |
| calibration | 校准 | | 理工科常说"参数标定" |
| search and matching | 搜寻匹配 | | |

## 3. 计量经济学

| 英文 | 中文 | 核对 | 备注 |
| --- | --- | --- | --- |
| ordinary least squares (OLS) | 普通最小二乘法 | | |
| unbiasedness / consistency / efficiency | 无偏性 / 一致性 / 有效性 | | |
| asymptotic normality | 渐近正态性 | | |
| Gauss–Markov theorem / BLUE | 高斯—马尔可夫定理 / 最优线性无偏估计量 | | |
| dependent variable / independent variable | 被解释变量 / 解释变量 | | 中文期刊惯用；"因变量/自变量"偏理工科 |
| core explanatory variable / control variables | 核心解释变量 / 控制变量 | | |
| interaction term | 交互项 | | |
| standard deviation / standard error | 标准差 / 标准误 | | 两者不要混 |
| heteroskedasticity | 异方差 | | |
| robust standard errors / cluster-robust standard errors | 稳健标准误 / 聚类稳健标准误 | | |
| serial correlation | 序列相关 | | |
| multicollinearity | 多重共线性 | | |
| omitted variable bias | 遗漏变量偏误 | | |
| endogeneity | 内生性 | | |
| reverse causality / simultaneity | 反向因果 / 联立性 | | |
| measurement error | 测量误差 | | |
| identification | 识别 | | 指因果识别，不同于工程里的"系统辨识" |
| instrumental variable (IV) | 工具变量 | | |
| two-stage least squares (2SLS) | 两阶段最小二乘法 | | |
| weak instruments | 弱工具变量 | | |
| exclusion restriction | 排他性约束 | | |
| overidentification test | 过度识别检验 | | |
| panel data | 面板数据 | | |
| fixed effects / random effects | 固定效应 / 随机效应 | | 个体、时间、双向固定效应 |
| Hausman test | 豪斯曼检验 | | |
| first difference | 一阶差分 | | |
| difference-in-differences (DID) | 双重差分 | | |
| staggered DID | 交错双重差分 / 多期双重差分 | | 中文译法不统一，按目标刊近年用法 |
| event study | 事件研究法 | | 金融中的事件研究与此同名不同义 |
| parallel trends | 平行趋势 | | |
| regression discontinuity design (RDD) | 断点回归 | | |
| propensity score matching (PSM) | 倾向得分匹配 | | |
| synthetic control method (SCM) | 合成控制法 | | |
| placebo test | 安慰剂检验 | | |
| treatment group / control group | 处理组 / 控制组（对照组） | | 理工科常说"实验组" |
| average treatment effect (ATE) | 平均处理效应 | | |
| average treatment effect on the treated (ATT) | 处理组平均处理效应 | | |
| local average treatment effect (LATE) | 局部平均处理效应 | | |
| linear probability model | 线性概率模型 | | Probit、Logit、Tobit 通常保留英文 |
| sample selection bias / Heckman two-step | 样本选择偏差 / Heckman 两步法 | | |
| quantile regression | 分位数回归 | | |
| stationarity / unit root / cointegration | 平稳性 / 单位根 / 协整 | | |
| vector autoregression (VAR) | 向量自回归 | | |
| Granger causality | 格兰杰因果 | | 不是真正意义上的因果 |
| generalized method of moments (GMM) | 广义矩估计 | | |
| maximum likelihood estimation (MLE) | 极大似然估计 | | 也写"最大似然估计"，全文统一 |
| confidence interval / significance level | 置信区间 / 显著性水平 | | |
| goodness of fit | 拟合优度 | | |
| baseline regression | 基准回归 | | 中文期刊常用节名 |
| robustness checks | 稳健性检验 | | 不要写"鲁棒性" |
| heterogeneity analysis | 异质性分析 | | |
| mechanism analysis | 机制分析 | | |
| mediation / moderation | 中介效应 / 调节效应 | | 三步法中介检验已受江艇（2022）批评 |

## 4. 金融学

| 英文 | 中文 | 核对 | 备注 |
| --- | --- | --- | --- |
| capital asset pricing model (CAPM) | 资本资产定价模型 | | |
| beta | β 系数 | | |
| systematic risk | 系统风险（不可分散风险） | | 与下一条不要混 |
| systemic risk | 系统性风险（系统性金融风险） | | 指金融体系整体风险 |
| idiosyncratic risk | 特质风险 | | |
| efficient market hypothesis | 有效市场假说 | | |
| arbitrage pricing theory (APT) | 套利定价理论 | | |
| Fama–French three-factor model | 法玛—弗伦奇三因子模型 | | |
| momentum | 动量效应 | | |
| excess return | 超额收益 | | 相对无风险利率 |
| abnormal return / cumulative abnormal return (CAR) | 异常收益 / 累计异常收益 | | 相对预期收益，与"超额收益"不同 |
| risk premium | 风险溢价 | | |
| Sharpe ratio | 夏普比率 | | |
| term structure of interest rates | 利率期限结构 | | |
| duration | 久期 | | |
| leverage | 杠杆 | | |
| capital structure | 资本结构 | | |
| agency cost | 代理成本 | | |
| financing constraints | 融资约束 | | |
| Tobin's Q | 托宾 Q | | |
| liquidity / volatility | 流动性 / 波动率 | | |
| tail risk | 尾部风险 | | |
| macroprudential policy | 宏观审慎政策 | | |
| corporate governance | 公司治理 | | |
| earnings management | 盈余管理 | | |
| initial public offering (IPO) / mergers and acquisitions (M&A) | 首次公开发行 / 并购 | | |

## 5. 理工科易混用语

从理工科转来时最容易带过来的说法。详见 library/patterns/stem-to-econ.md。

| 理工科习惯 | 经济学通行 | 说明 |
| --- | --- | --- |
| 鲁棒性 | 稳健性 | 经济学论文基本不用"鲁棒" |
| 实验组 | 处理组 | 对照组、控制组都可 |
| 仿真 | 模拟、数值模拟、反事实模拟 | |
| 参数标定、参数辨识 | 校准、参数估计 | |
| 因变量、自变量 | 被解释变量、解释变量 | 中文期刊惯用 |
| 系统辨识 | （无对应） | 经济学的"识别"指因果识别 |
| 噪声 | 随机扰动项、误差项 | |
| 收敛（算法） | 收敛（经济增长中的趋同） | 同词不同义，注意上下文 |
| 最优解 | 均衡 | 描述市场结果时 |
| 验证了有效性 | 识别了因果效应、提供了证据 | 经验研究不说"证明了" |
| 显著提升 | 统计显著；经济上可观 | 分开说 |
| 创新点 | 本文的贡献 | |
