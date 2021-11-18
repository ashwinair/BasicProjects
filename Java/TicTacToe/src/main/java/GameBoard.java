public class GameBoard {
    static void printGameBoard(char[][] board){
        for (char[] rows: board){
            for (char c: rows)
                System.out.print(c);

            System.out.println();
        }
    }

}
