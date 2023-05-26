import java.io.BufferedInputStream;
import java.io.FileNotFoundException;

public class Driver {
    public static void main(String[] args) throws FileNotFoundException {
        while(true) {
            Solver wordleSolver = new Solver();
            wordleSolver.menu();
        }

    }
}
