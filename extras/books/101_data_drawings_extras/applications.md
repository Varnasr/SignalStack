# Applications in Practice

How the concepts from *101 Data Science Drawings* show up in real-world data science work — from job interviews to production systems.

---

## Cross-validation

**What it is:** Splitting your dataset into K folds, training on K-1 folds, and testing on the remaining fold. Repeat K times and average the results.

**Where you'll use it:**

- Comparing models before selecting one for production
- Tuning hyperparameters (e.g., regularisation strength, tree depth)
- Estimating how well a model will generalise to unseen data

**Common pitfall:** Applying cross-validation after feature selection or preprocessing causes data leakage. Always cross-validate the *entire* pipeline.

---

## Propensity Score Matching

**What it is:** A technique for estimating treatment effects in observational studies. Each unit gets a "propensity score" — the predicted probability of receiving treatment — and treated units are matched to control units with similar scores.

**Where you'll use it:**

- Evaluating programme impact when randomised trials aren't feasible
- Health policy research (e.g., comparing outcomes for patients who received an intervention vs. those who didn't)
- Development economics — estimating the effect of a cash transfer programme

**Common pitfall:** PSM only controls for *observed* confounders. Unobserved differences between groups can still bias results.

---

## Lag and Lead in SQL

**What it is:** Window functions that access data from previous rows (`LAG`) or subsequent rows (`LEAD`) in the result set without self-joining.

**Where you'll use it:**

- Calculating month-over-month or year-over-year changes
- Detecting trends in time-series data (e.g., "did this metric increase from last quarter?")
- Building dashboards that show deltas and growth rates

**Example:**

```sql
SELECT
  month,
  revenue,
  revenue - LAG(revenue) OVER (ORDER BY month) AS revenue_change
FROM monthly_sales;
```

---

## Log Transformation

**What it is:** Applying a logarithmic function to skewed data to make it more normally distributed and to stabilise variance.

**Where you'll use it:**

- Modelling income, population, or any right-skewed variable
- Interpreting regression coefficients as percentage changes (log-log or log-linear models)
- Satisfying normality assumptions in statistical tests

**Common pitfall:** Log of zero is undefined. Handle zeros before transforming (e.g., `log(x + 1)`) and be explicit about which base you're using.

---

## Feature Engineering

**What it is:** Creating new input variables from raw data to improve model performance.

**Where you'll use it:**

- Extracting day-of-week, month, or hour from timestamps
- Creating interaction terms (e.g., age × income)
- Encoding categorical variables (one-hot, target encoding)

**Why it matters:** In many real-world projects, feature engineering has more impact on model quality than algorithm choice.

---

## A/B Testing

**What it is:** A randomised experiment comparing two variants (A and B) to determine which performs better on a defined metric.

**Where you'll use it:**

- Product decisions (e.g., which button colour gets more clicks)
- Policy pilots (e.g., does SMS reminders improve clinic attendance)
- Email campaigns and marketing optimisation

**Common pitfall:** Stopping the test too early ("peeking") inflates false positive rates. Define sample size and duration before starting.

---

*See [key_concepts.md](key_concepts.md) for definitions of the underlying terms.*
