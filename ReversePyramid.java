import java.util.*;


class ReversePyramid1 {
    private int rows;
    ReversePyramid1(int r) {
        rows = r;
    }

    void printPyramid() {
        for(int i=1;i<=rows;i++){
            for(int j=1;j<i;j++){
                System.out.print(" ");
            }
            for(int j=rows-i;j>=0;j--){
                System.out.print("*");
            }
            for(int j=rows-i;j>0;j--){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

class ChildReversePyramid extends ReversePyramid1 {
        ChildReversePyramid(int r){
            super(r);
        }
}

public class ReversePyramid {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        int ro = sc.nextInt();
        ChildReversePyramid obj = new ChildReversePyramid(ro);
        obj.printPyramid();
    }
}