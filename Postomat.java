/**
* The program checks the pairs of pincodes for a postomat.
* There are only 5 pairs possible, otherwise an Error message is printed out.
*/


import java.util.Scanner;

class Postomat {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int mistakesCounter = 0;
        while (true) {
            String correctPin = sc.nextLine();
            String usersPin = sc.nextLine();
            if (correctPin.equals(usersPin)) {
                System.out.println("SUCCESS. CORRECT PIN");
                break;
            } else {
                System.out.println("INCORRECT PIN. " + "Try " + ++mistakesCounter + " ot of 5");
                if (mistakesCounter < 5) {
                    continue;
                } else { 
                    System.out.println("Error. Request denied.");
                    break; 
                }
            }
        }
    }
}

/*

Sample Input 1:

1234
1235
3478
1234
5623
5623

Sample Input 2:

1234
1235
3478
1234
5623
5624
0534
5623
4512
3214

*/
