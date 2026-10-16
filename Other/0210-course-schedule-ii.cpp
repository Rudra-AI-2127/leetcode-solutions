class Solution {
public:
    vector<int> findOrder(int numCourses,
                          vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        queue<int> q;
        vector<int> order;

        // Build graph
        for (auto& p : prerequisites) {
            adj[p[1]].push_back(p[0]);
            indegree[p[0]]++;
        }

        // Add courses with no prerequisites
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                q.push(i);
        }

        // Topological sort
        while (!q.empty()) {
            int course = q.front();
            q.pop();

            order.push_back(course);

            for (int next : adj[course]) {
                indegree[next]--;

                if (indegree[next] == 0)
                    q.push(next);
            }
        }

        // Cycle exists if some courses cannot be processed
        if (order.size() != numCourses)
            return {};

        return order;
    }
};