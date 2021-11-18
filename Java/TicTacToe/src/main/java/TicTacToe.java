import java.util.*;

public class TicTacToe {
    static ArrayList<Integer> playersPosition = new ArrayList<>();
    static ArrayList<Integer> cpuPosition = new ArrayList<>();
    public static void main(String[] args) {
        char[][] board = {
                {' ', '|', ' ', '|', ' '},
                {'-', '+', '-', '+', '-'},
                {' ', '|', ' ', '|', ' '},
                {'-', '+', '-', '+', '-'},
                {' ', '|', ' ', '|', ' '}
        };
        GameBoard.printGameBoard(board);
        System.out.println("Enter a no. to place your piece: ");
        while (true) {
            Scanner input = new Scanner(System.in);
            int position = input.nextInt();
            while(playersPosition.contains(position) || cpuPosition.contains(position)){
                System.out.println("Not a valid position entered, try again:");
                position = input.nextInt();
            }
            System.out.println(playersPosition.size() + cpuPosition.size());
            String winner = Winner.checkWinner(playersPosition,cpuPosition);
            if(winner.length() > 0) {
                System.out.println(winner);
                break;
            }


            PlacePiece.placePiece(position, board, "player",playersPosition,cpuPosition);
            Random rand = new Random();
            int cpuPos = rand.nextInt(9) + 1;
            while(playersPosition.contains(cpuPos) || cpuPosition.contains(cpuPos)){
                cpuPos = rand.nextInt(9) + 1;
            }
            PlacePiece.placePiece(cpuPos, board, "cpu",playersPosition,cpuPosition);
            GameBoard.printGameBoard(board);
            winner = Winner.checkWinner(playersPosition,cpuPosition);
            if(winner.length() > 0) {
                System.out.println(winner);
                break;
            }

        }
    }
}
