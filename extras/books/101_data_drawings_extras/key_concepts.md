# Key Concepts & Definitions

Core terms and ideas from *101 Data Science Drawings*, with short definitions and context for when you'll encounter them.

---

## Supervised Learning

| Concept | Definition | When It Matters |
|---------|-----------|-----------------|
| **Bias-Variance Tradeoff** | The tension between a model that's too simple (high bias, underfits) and one that's too complex (high variance, overfits). The goal is to find the sweet spot. | Model selection, hyperparameter tuning, comparing algorithms |
| **Overfitting vs Underfitting** | Overfitting: the model memorises training data and fails on new data. Underfitting: the model is too simple to capture patterns at all. | Diagnosing poor model performance, choosing model complexity |
| **Gradient Descent** | An optimisation algorithm that iteratively adjusts model parameters by moving in the direction of steepest decrease in the loss function. | Training neural networks, logistic regression, any iterative model fitting |
| **Decision Trees** | A model that splits data into branches based on feature thresholds, creating a tree of if-then rules. Easy to interpret but prone to overfitting. | Classification and regression tasks, feature importance analysis |
| **Naive Bayes** | A probabilistic classifier that assumes features are independent given the class label. Fast and effective for text classification. | Spam filtering, sentiment analysis, document categorisation |

## Unsupervised Learning

| Concept | Definition | When It Matters |
|---------|-----------|-----------------|
| **K-Means Clustering** | Partitions data into K groups by minimising the distance between points and their cluster centre. Requires choosing K in advance. | Customer segmentation, grouping survey responses, geographic clustering |
| **Principal Component Analysis (PCA)** | Reduces the number of variables by finding new axes (components) that capture the most variance in the data. | Dimensionality reduction, visualising high-dimensional data, preprocessing |

## Probability & Statistics

| Concept | Definition | When It Matters |
|---------|-----------|-----------------|
| **OLS Regression** | Ordinary Least Squares — fits a linear model by minimising the sum of squared differences between observed and predicted values. The workhorse of quantitative research. | Impact evaluation, econometric analysis, any linear relationship modelling |
| **Confidence Intervals** | A range of values that likely contains the true population parameter (e.g., "we are 95% confident the mean is between 3.2 and 4.8"). | Reporting results, policy briefs, uncertainty communication |
| **p-values** | The probability of observing your result (or something more extreme) if the null hypothesis were true. Lower values suggest stronger evidence against the null. | Hypothesis testing, academic publishing, programme evaluation |

## Econometrics

| Concept | Definition | When It Matters |
|---------|-----------|-----------------|
| **Instrumental Variables** | A technique to estimate causal effects when there's endogeneity (the predictor is correlated with the error term). Uses a third variable (the instrument) that affects the outcome only through the predictor. | Causal inference when randomisation isn't possible |
| **Difference-in-Differences** | Compares the change in outcomes over time between a treatment group and a control group. Controls for time-invariant unobserved differences. | Policy evaluation, natural experiments, programme impact studies |

## SQL

| Concept | Definition | When It Matters |
|---------|-----------|-----------------|
| **Joins** | Combine rows from two or more tables based on a related column. Types: INNER (matching rows only), LEFT (all from left table), RIGHT (all from right table), FULL (all rows from both). | Any multi-table database query, merging datasets |
| **Window Functions** | Perform calculations across a set of rows related to the current row without collapsing the result. Examples: `ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`. | Rankings, running totals, comparing rows to their neighbours |

---

*Definitions inspired by the visual approach in Raymond Lim's [101 Data Science Drawings](https://github.com/alod83/Learning-Generative-AI-Tools-for-Excel).*
