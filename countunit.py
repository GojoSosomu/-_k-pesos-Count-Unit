"""
The ₱ₖ Count Unit System: reference implementation.

Created by YOUR NAME, 2026. MIT License (see LICENSE).

An amount is written W ₱ₖ L, with value V = k*W + L.
All arithmetic uses integers (// and %), never decimals.
"""

SUBSCRIPTS = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def value(W, L, k=5):
    """Peso value of W ₱ₖ L."""
    return k * W + L


def from_pesos(V, k=5):
    """Peso value -> (W, L) in normal form (0 <= L < k)."""
    return divmod(V, k)


def normalize(W, L, k=5):
    """Move whole units out of the loose part."""
    return W + L // k, L % k


def add(a, b, k=5):
    """Add two (W, L) amounts in the same unit, then normalize once."""
    return normalize(a[0] + b[0], a[1] + b[1], k)


def compare(a, b, k=5):
    """Return -1, 0 or 1. Normalizes both first, then compares W, then L."""
    a, b = normalize(*a, k), normalize(*b, k)
    return (a > b) - (a < b)


def convert(W, L, a, b):
    """Rewrite W ₱ₐ L as (W, L) in ₱ᵦ, going through the peso value."""
    return divmod(value(W, L, a), b)


def count_pile(pile, k=5):
    """
    Count a pile given as {denomination: quantity}.
    Pieces whose denomination is a multiple of k are weighted (d // k) into W.
    Every other piece (for k=5, the ₱1 coin) goes unweighted into L.
    """
    W = L = 0
    for d, q in pile.items():
        if d % k == 0:
            W += (d // k) * q
        else:
            L += d * q
    return W, L


def check_coins(L, expected_total, k=5):
    """
    Hand-count check for k=5: with every non-₱1 piece a multiple of 5,
    the ₱1 coin count L must satisfy L mod 5 == total mod 5.
    False means recount the ₱1 coins. True means "probably fine", not proof
    (a miscount of exactly 5, 10, ... coins passes).
    """
    return L % k == expected_total % k


def fmt(W, L, k=5):
    """Format as 'W ₱ₖ L', e.g. '267 ₱₅ 3'."""
    return f"{W} ₱{str(k).translate(SUBSCRIPTS)} {L}"
