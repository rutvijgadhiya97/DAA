import numpy as np
import matplotlib.pyplot as plt
import time

# Brute Force Algorithm
def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

# Knuth-Morris-Pratt (KMP) Algorithm
def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    compute_lps(pattern, m, lps)
    occurrences = []
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences

def compute_lps(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Boyer-Moore (BM) Algorithm
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []
    skip = preprocess_bad_character(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j == -1:
            occurrences.append(i)
            if i + m < n:
                i += m - skip[ord(text[i + m])]
            else:
                i += 1
        else:
            i += max(1, j - skip[ord(text[i + j])])
    return occurrences

def preprocess_bad_character(pattern):
    skip = [-1] * 256
    m = len(pattern)
    for i in range(m):
        skip[ord(pattern[i])] = i
    return skip

# Rabin-Karp Algorithm
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []
    d = 256
    q = 101  # Prime number
    h_pattern = 0
    h_text = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q
    for i in range(n - m + 1):
        if h_pattern == h_text:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                occurrences.append(i)
        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % q
            if h_text < 0:
                h_text = h_text + q
    return occurrences

# Function to benchmark algorithms
def benchmark(algorithm, text_sizes, pattern_sizes):
    timings = np.zeros((len(pattern_sizes), len(text_sizes)))
    for i, m in enumerate(pattern_sizes):
        pattern = 'a' * m  # Creating a pattern of length m
        for j, n in enumerate(text_sizes):
            text = 'a' * n  # Creating a text of length n
            start_time = time.time()
            algorithm(text, pattern)
            end_time = time.time()
            timings[i][j] = end_time - start_time
    return timings

# Input data
text_sizes = [100, 500, 1000, 5000, 10000]
pattern_sizes = [5, 10, 20, 50]

# Benchmark each algorithm
brute_force_timings = benchmark(brute_force, text_sizes, pattern_sizes)
kmp_timings = benchmark(kmp, text_sizes, pattern_sizes)
boyer_moore_timings = benchmark(boyer_moore, text_sizes, pattern_sizes)
rabin_karp_timings = benchmark(rabin_karp, text_sizes, pattern_sizes)

# Plot time complexity
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
for i, m in enumerate(pattern_sizes):
    plt.plot(text_sizes, brute_force_timings[i], marker='o', label=f'Brute Force, Pattern Size={m}')
    plt.plot(text_sizes, kmp_timings[i], marker='o', label=f'KMP, Pattern Size={m}')
    plt.plot(text_sizes, boyer_moore_timings[i], marker='o', label=f'Boyer-Moore, Pattern Size={m}')
    plt.plot(text_sizes, rabin_karp_timings[i], marker='o', label=f'Rabin-Karp, Pattern Size={m}')

plt.title('Practical Runtime Performance')
plt.xlabel('Text Size')
plt.ylabel('Time (s)')
plt.xscale('log')
plt.yscale('log')
plt.legend()

plt.tight_layout()
plt.show()
