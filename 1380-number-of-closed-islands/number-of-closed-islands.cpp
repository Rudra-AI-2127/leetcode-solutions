class Solution {
public:
    int m, n;

    int delrow[4] = {-1, 0, 1, 0};
    int delcol[4] = {0, 1, 0, -1};

    void bfs(vector<vector<int>>& grid,
             vector<vector<bool>>& vis,
             int row, int col) {

        queue<pair<int, int>> q;
        q.push({row, col});
        vis[row][col] = true;

        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();

            for (int i = 0; i < 4; i++) {
                int nrow = r + delrow[i];
                int ncol = c + delcol[i];

                if (nrow >= 0 && nrow < m &&
                    ncol >= 0 && ncol < n &&
                    grid[nrow][ncol] == 0 &&
                    !vis[nrow][ncol]) {

                    vis[nrow][ncol] = true;
                    q.push({nrow, ncol});
                }
            }
        }
    }

    int closedIsland(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        vector<vector<bool>> vis(m, vector<bool>(n, false));

        // Step 1: Visit all boundary-connected land.
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0 && !vis[i][0])
                bfs(grid, vis, i, 0);

            if (grid[i][n - 1] == 0 && !vis[i][n - 1])
                bfs(grid, vis, i, n - 1);
        }

        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 0 && !vis[0][j])
                bfs(grid, vis, 0, j);

            if (grid[m - 1][j] == 0 && !vis[m - 1][j])
                bfs(grid, vis, m - 1, j);
        }

        // Step 2: Count the remaining closed islands.
        int islands = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && !vis[i][j]) {
                    islands++;
                    bfs(grid, vis, i, j);
                }
            }
        }

        return islands;
    }
};