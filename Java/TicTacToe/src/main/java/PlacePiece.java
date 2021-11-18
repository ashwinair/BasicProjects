import java.util.ArrayList;

public class PlacePiece {
    static void placePiece(int position, char[][] board, String user, ArrayList<Integer> playersPosition,ArrayList<Integer> cpuPosition) {
        char symbol = ' ';
        if (user.contentEquals("player")) {
            symbol = 'X';
            playersPosition.add(position);
        } else if (user.contentEquals("cpu")){
            symbol = 'O';
            cpuPosition.add(position);
        }
        switch(position){
            case 1:
                board[0][0] = symbol;
                break;
            case 2:
                board[0][2] = symbol;
                break;
            case 3:
                board[0][4] = symbol;
                break;
            case 4:
                board[2][0] = symbol;
                break;
            case 5:
                board[2][2] = symbol;
                break;
            case 6:
                board[2][4] = symbol;
                break;
            case 7:
                board[4][0] = symbol;
                break;
            case 8:
                board[4][2] = symbol;
                break;
            case 9:
                board[4][4] = symbol;
                break;
            default: break;
        }
    }
}
