import java.util.ArrayList;
import java.util.List;

public class FizzBuzz {
    // Time complexity: O(n)
    // Space complexity: O(n)
    public List<String> fizzBuzz(int n) {
        List<String> answer = new ArrayList<String>();
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                answer.add("FizzBuzz");
            } else if (i % 5 == 0) {
                answer.add("Buzz");
            } else if (i % 3 == 0) {
                answer.add("Fizz");
            } else {
                answer.add(Integer.toString(i));
            }
        }
        return answer;
    }

    // test
    public static void main(String args[]) {
        FizzBuzz fizzBuzz = new FizzBuzz();
        System.out.println(fizzBuzz.fizzBuzz(3));
        System.out.println(fizzBuzz.fizzBuzz(5));
        System.out.println(fizzBuzz.fizzBuzz(15));
    }
}
