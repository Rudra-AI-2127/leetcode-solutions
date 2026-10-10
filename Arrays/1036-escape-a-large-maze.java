class Solution {
    public boolean isEscapePossible(int[][] b, int[] s, int[] t) {
        if (b.length < 2) return true;
        java.util.Set<Long> h = new java.util.HashSet<>();
        for (int[] p : b)
            h.add((long) p[0] * 1000000 + p[1]);
        return f(s, t, h, b.length) && f(t, s, h, b.length);
    }
    private boolean f(int[] s, int[] t, java.util.Set<Long> h, int n) {
        int[][] d = {{1,0},{-1,0},{0,1},{0,-1}};
        java.util.Set<Long> v = new java.util.HashSet<>();
        java.util.Queue<int[]> q = new java.util.LinkedList<>();
        q.offer(s);
        v.add((long) s[0] * 1000000 + s[1]);
        int m = n * (n - 1) / 2;
        while (!q.isEmpty() && v.size() <= m) {
            int[] p = q.poll();
            if (p[0] == t[0] && p[1] == t[1]) return true;
            for (int[] a : d) {
                int x = p[0] + a[0], y = p[1] + a[1];
                if (x < 0 || x >= 1000000 || y < 0 || y >= 1000000)
                    continue;
                long k = (long) x * 1000000 + y;
                if (!h.contains(k) && v.add(k))
                    q.offer(new int[]{x, y});
            }
        }
        return v.size() > m;
    }
}


