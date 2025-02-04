# 3 Main Ways to Calculate Derivatives

## 1. Numerical Differentiation

**Gradient**: Rise over the slope  

$$
\text{Gradient} = \frac{rise}{run}
$$

You can approximate this as:

$$
\text{Gradient} \approx \frac{f(x+h) - f(x)}{h}
$$

where \( h \) is a small number.

---

### Some Examples

#### Example 1:

Given:

$$
f(x) = x^2
$$

Finding the derivative:

$$
f'(x) = \frac{(x+h)^2 - x^2}{h}
$$

Expanding the numerator:

$$
= \frac{x^2 + 2xh + h^2 - x^2}{h}
$$

$$
= \frac{2xh + h^2}{h}
$$

$$
= 2x + h
$$

As h -> 0:

$$
f'(x) = 2x
$$


# 2. Symbolic Differentiation

Here, we differentiate using the calculus rules we know.

## Power Rule
If:

$$
f(x) = x^n
$$

then:

$$
f'(x) = n x^{n-1}
$$

## Constant Rule
If:

$$
f(x) = k
$$

then:

$$
f'(x) = 0
$$

## Sum Rule
If:

$$
f(x) = g(x) + h(x)
$$

then:

$$
f'(x) = g'(x) + h'(x)
$$

## Product Rule
If:

$$
f(x) = g(x) h(x)
$$

then:

$$
f'(x) = g(x) h'(x) + g'(x) h(x)
$$

---

## Example

Given:

$$
f(x) = 4x^2 + 8x + 16
$$

Differentiating:

$$
f'(x) = 8x + 8
$$

Factored form:

$$
= 8(x + 1)
$$

---

# 3. Automatic Differentiation (Auto Diff)

Unlike computing large terms like symbolic differentiation, **auto differentiation** prioritizes breaking the larger operations into decomposable standard operations (add, subtract, etc.) and chaining them to get the derivatives.
