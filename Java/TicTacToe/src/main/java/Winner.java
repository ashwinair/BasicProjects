import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Winner {
    public static String checkWinner(ArrayList<Integer> playersPosition,ArrayList<Integer> cpuPosition){
        List topRow = Arrays.asList(1,2,3);
        List midRow = Arrays.asList(4,5,6);
        List lastRow = Arrays.asList(7,8,9);
        List leftCol = Arrays.asList(1,4,7);
        List midCol = Arrays.asList(2,5,7);
        List rightCol = Arrays.asList(3,6,9);
        List cross1 = Arrays.asList(1,5,9);
        List cross2 = Arrays.asList(3,5,7);

        List<List> winningPositions = new ArrayList<List>();
        winningPositions.add(topRow);
        winningPositions.add(midRow);
        winningPositions.add(lastRow);
        winningPositions.add(leftCol);
        winningPositions.add(midCol);
        winningPositions.add(rightCol);
        winningPositions.add(cross1);
        winningPositions.add(cross2);
        for (List list: winningPositions) {
            if (playersPosition.containsAll(list)) {
                return "Bingo !!";
            } else if (cpuPosition.containsAll(list)) {
                return "Bad luck :(";
            }
            if (playersPosition.size() + cpuPosition.size() >= 8){
                return "Cat!! {-_-}";
            }
        }
        return "";
    }
}
