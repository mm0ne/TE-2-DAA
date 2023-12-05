# Python3 implementation for the above approach
import time

def addEdge(adj, x, y):
    adj[x].append(y)
    adj[y].append(x)


def dfs(adj, dp, src, par):
    for child in adj[src]:
        if child != par:
            dfs(adj, dp, child, src)

    for child in adj[src]:
        if child != par:
            # not including source in the vertex cover
            dp[src][0] = dp[child][1] + dp[src][0]

            # including source in the vertex cover
            dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])


def minSizeVertexCover(adj, N):
    dp = [[0 for j in range(2)] for i in range(N + 1)]
    for i in range(1, N + 1):
        # 0 denotes not included in vertex cover
        dp[i][0] = 0

        # 1 denotes included in vertex cover
        dp[i][1] = 1

    dfs(adj, dp, 1, -1)

    # printing minimum size vertex cover
    print(min(dp[1][0], dp[1][1]))


def start_dp(filename: str) -> None:
    with open(filename, "r") as src:
        lines = src.readlines()
        N = int(lines[0].split(" ")[0])
        lines = lines[1:]

        adj = [[] for _ in range(N + 1)]
        for i, j in enumerate(lines):
            values = [int(k) for k in j.strip().split(" ")]

            for val in values:
                addEdge(adj=adj, x=(i + 1), y=val)
        
        start = time.time()
        minSizeVertexCover(adj=adj, N=N)
        end = time.time()

        print(f"It takes {(end - start):.3f} s to compute the vertex cover of {N} vertices\n")


def main():
    start_dp("nary_tree_100.txt")
    start_dp("nary_tree_300.txt")
    start_dp("nary_tree_900.txt")
    start_dp("nary_tree_10000.txt")
    start_dp("nary_tree_100000.txt")
    start_dp("nary_tree_1000000.txt")


if __name__ == "__main__":
    main()
