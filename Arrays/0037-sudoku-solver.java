class Solution {
    boolean[][] rows = new boolean[9][10];
    boolean[][] cols = new boolean[9][10];
    boolean[][] boxes = new boolean[9][10];

    public void solveSudoku(char[][] board) {

        // Store existing numbers
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {

                if (board[r][c] != '.') {
                    int num = board[r][c] - '0';
                    int box = (r / 3) * 3 + (c / 3);

                    rows[r][num] = true;
                    cols[c][num] = true;
                    boxes[box][num] = true;
                }
            }
        }

        backtrack(board);
    }

    private boolean backtrack(char[][] board) {

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {

                // Empty cell
                if (board[r][c] == '.') {

                    int box = (r / 3) * 3 + (c / 3);

                    // Try 1 to 9
                    for (int num = 1; num <= 9; num++) {

                        // Check if number can be placed
                        if (rows[r][num] ||
                            cols[c][num] ||
                            boxes[box][num]) {
                            continue;
                        }

                        // Place number
                        board[r][c] = (char) (num + '0');
                        rows[r][num] = true;
                        cols[c][num] = true;
                        boxes[box][num] = true;

                        // Continue solving
                        if (backtrack(board)) {
                            return true;
                        }

                        // Backtrack
                        board[r][c] = '.';
                        rows[r][num] = false;
                        cols[c][num] = false;
                        boxes[box][num] = false;
                    }

                    // No number works
                    return false;
                }
            }
        }

        // Sudoku completely solved
        return true;
    }
}