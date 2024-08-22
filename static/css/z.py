MOD = in    t(1e9 + 7)

def solve():
    S = input().strip()
    n = len(S)
    
    # Prefix sum array
    P = [0] * (n + 1)

    for i in range(1, n + 1):
        P[i] = (1 if S[i - 1] == '1' else -1) + P[i - 1]

    #print(*P)
    cnt = {}
    ans = 0

    for i in range(n + 1):
        ans = (ans + (n - i + 1) * cnt.get(P[i], 0)) % MOD
        cnt[P[i]] = (cnt.get(P[i], 0) + (i + 1)) % MOD

    print(ans)

# Input and process multiple test cases
if __name__ == "__main__":
    tc = int(input().strip())
    for _ in range(tc):
        solve()
