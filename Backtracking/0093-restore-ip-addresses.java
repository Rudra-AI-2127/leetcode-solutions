class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        backtrack(s, 0, 0, new StringBuilder(), result);
        return result;
    }
    private void backtrack(String s, int index, int parts,
                            StringBuilder current,
                            List<String> result) {
        if (parts == 4) {
            if (index == s.length()) {
                result.add(current.toString());
            }
            return;
        }
        for (int end = index; end < Math.min(index + 3, s.length()); end++) {
            String part = s.substring(index, end + 1);
            if (part.length() > 1 && part.charAt(0) == '0') {
                break;
            }
            int value = Integer.parseInt(part);
            if (value > 255) {
                break;
            }
            int oldLength = current.length();
            if (parts > 0) {
                current.append(".");
            }
            current.append(part);
            backtrack(
                s,
                end + 1,
                parts + 1,
                current,
                result
            );
            current.setLength(oldLength);
        }
    }
}