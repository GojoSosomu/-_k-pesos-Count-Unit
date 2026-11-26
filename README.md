# The ₱ₖ Count Unit System

**A counting notation for peso cash, built around counting in fives.**

> Created by **YOUR NAME**, 2026. Reuse is welcome, **with credit**.
> Spec: [CC BY 4.0](LICENSE-docs.md) · Code: [MIT](LICENSE)

*Plain-text fallback: where ₱ₖ can't be typed, write `P5`, `P10`, `P1000` (for example `267 P5 3`).*

## What it is

A way to count cash in a unit you choose, such as ₱5, while keeping every peso exactly. An amount is split into a count of whole units and a loose remainder. It is a counting aid for hand counts, not a currency and not new mathematics: it organizes unit conversion, weighted sums, and quotient and remainder.

## Quick reference

| What | Rule |
|---|---|
| Unit | 1 ₱ₖ = ₱k (read ₱₅ as "5-pesos Count Unit") |
| Write | W ₱ₖ L |
| Value | V = kW + L |
| Normal form | 0 ≤ L < k |
| Normalize | W′ = W + ⌊L/k⌋, L′ = L mod k |
| From pesos | W = ⌊V/k⌋, L = V mod k |
| Add | add W and W, add L and L, then normalize |
| Compare | normalize both, then compare W, then L |
| Change unit | V = aW + L, then W_b = ⌊V/b⌋, L_b = V mod b |
| ₱₅ weights | ₱5 = 1, ₱10 = 2, ₱20 = 4, ₱50 = 10, ₱100 = 20, ₱200 = 40, ₱500 = 100, ₱1000 = 200 |
| Check | L mod 5 = V mod 5 |

## 1. Definitions

- **Count Unit ₱ₖ** is one unit worth ₱k. 1 ₱₅ = ₱5.
- **₱₅ is not ₱5.** ₱5 is an amount of money; ₱₅ is a counting unit. When writing by hand, keep the subscript clearly under the peso sign.
- **W ₱ₖ L:** W is the whole count of units, L is the loose pesos (a plain whole number).
- **Value:** V = kW + L.

Example: 125 ₱₅ 713 means 125 five-peso units plus 713 loose pesos, so V = 5(125) + 713 = ₱1,338.

## 2. Why the unit is 5

Every Philippine note and coin from ₱5 upward is a multiple of 5. Counting in ₱₅ therefore gives every piece except the ₱1 coin a whole-number weight, and only the ₱1 coins go into the loose part. 5 is the largest unit with this property: it is the greatest common divisor of all denominations except ₱1.

## 3. Counting a pile

| Piece | ₱1 | ₱5 | ₱10 | ₱20 | ₱50 | ₱100 | ₱200 | ₱500 | ₱1000 |
|---|---|---|---|---|---|---|---|---|---|
| Goes to | L | W | W | W | W | W | W | W | W |
| Weight in W | 1 each | 1 | 2 | 4 | 10 | 20 | 40 | 100 | 200 |

1. Multiply each non-₱1 piece count by its weight and add: this is **W**.
2. Count the ₱1 coins, unweighted: this is **L**.
3. Write **W ₱₅ L**.

Example: 3 × ₱5, 2 × ₱10, 1 × ₱100 and 4 × ₱1 gives W = 3 + 4 + 20 = 27 and L = 4, so **27 ₱₅ 4** = ₱139.

## 4. Normal form

An amount is **normalized** when 0 ≤ L < k. To normalize: W′ = W + ⌊L/k⌋ and L′ = L mod k.

Example: 125 ₱₅ 713 has 713 = 142 × 5 + 3 loose pesos, so W′ = 267 and L′ = 3: **267 ₱₅ 3**, still ₱1,338.

This answers "how many fives' worth do I have, and what is left over?" W counts value, not physical coins: it matches real ₱5 coins only if all the money were exchanged into ₱5 coins. Normalizing is optional; the value is kW + L either way.

## 5. Converting to and from pesos

- To pesos: V = kW + L.
- From pesos: W = ⌊V/k⌋, L = V mod k. Example: ₱489 → **97 ₱₅ 4**.

Use integer arithmetic (quotient and remainder). Avoid decimals such as 0.2, which computers store inexactly.

## 6. Adding

Add the W parts together and the L parts together, then normalize once.

Example: 125 ₱₅ 713 + 3 ₱₅ 400 = 128 ₱₅ 1113 → **350 ₱₅ 3** (check: both are ₱1,753).

This makes pooling counts from several people simple: nobody converts to pesos first.

## 7. Comparing

Normalize both amounts, then compare W, and if equal, compare L.

- 267 ₱₅ 3 > 266 ₱₅ 4, because 267 > 266.
- 125 ₱₅ 713 and 267 ₱₅ 3 are equal (₱1,338). Compare only after normalizing.

## 8. Changing the unit (the ₱ Count Unit Converter)

To rewrite an amount from ₱ₐ to ₱ᵦ, go through its value: V = aW + L, then W_b = ⌊V/b⌋ and L_b = V mod b.

Example: 125 ₱₅ 713 (₱1,338) in ₱₁₀ is **133 ₱₁₀ 8**. Shortcut: normalize to 267 ₱₅ 3, halve W (133, remainder one five), and add that ₱5 to the loose pesos (5 + 3 = 8).

For a single decimal count N_k = V/k, the same conversion is a ratio: **N_b = N_a × (a/b)**. Example: 127.2 in ₱₅ is 63.6 in ₱₁₀ (both ₱636).

Properties: converting a unit to itself changes nothing (identity); converting and converting back returns the original (reversible); converting through an intermediate unit equals converting directly (chaining). Ordinary pesos are the case b = 1.

| Unit | Same amount (₱28,126) |
|---|---|
| ₱₅ | 5,625 ₱₅ 1 |
| ₱₁₀₀ | 281 ₱₁₀₀ 26 |
| ₱₁₀₀₀ | 28 ₱₁₀₀₀ 126 |

For powers of 10 (₱₁₀, ₱₁₀₀, ₱₁₀₀₀), W and L can be read straight off the digits: 20,837,147 is **20,837 ₱₁₀₀₀ 147**.

## 9. Scale and size

The subscript works like the exponent in scientific notation: the lead number gives the size at a glance and the loose part carries the detail. Unlike scientific notation, nothing is rounded, so every peso is kept.

## 10. Error check for hand counts

Every piece except the ₱1 coin is a multiple of 5. If you know what the total should be (for example from a register), the ₱1 coin count must satisfy **L mod 5 = V mod 5**.

- If it fails, recount the ₱1 coins.
- If it passes, the coins are probably right; look at the notes and larger coins.

It only catches errors that are not multiples of 5 (a miscount of exactly 5, 10, … coins passes), so treat a pass as "probably fine", not proof.

## 11. Scope and limits

- It is a **personal counting convention**; others need the weight table to read it.
- Receipts, banks and official records use plain pesos, so convert with V = 5W + L at each handoff.
- Whole pesos only. For centavos: ₱0.25 = 0.05 ₱₅ and ₱0.01 = 0.002 ₱₅.
- It helps most when counting by hand, pooling counts from several people, and handling mostly notes. If software does the whole job, it adds little.

## Reference implementation

`countunit.py` implements everything above with integer arithmetic; `test_countunit.py` checks every worked example in this document.

```python
from countunit import count_pile, normalize, add, convert, fmt

W, L = count_pile({5: 3, 10: 2, 100: 1, 1: 4})   # (27, 4)
print(fmt(*normalize(125, 713)))                  # 267 ₱₅ 3
print(fmt(*convert(125, 713, 5, 10), k=10))       # 133 ₱₁₀ 8
```

Run the tests with `python -m unittest`.

## Prior art

This notation combines established ideas: unit conversion, weighted sums, rational numbers, Euclidean division (quotient and remainder), and mixed-unit notation such as "5 ft 7 in". The symbol, the name, the W ₱ₖ L form, and the way these pieces are organized for counting cash are the author's.

## License and credit

- Specification text: [CC BY 4.0](LICENSE-docs.md): reuse and adapt freely, but credit **YOUR NAME**.
- Code: [MIT](LICENSE): keep the copyright notice in copies.

Suggested credit: *"The ₱ₖ Count Unit System" by YOUR NAME, 2026.*
