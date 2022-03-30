public class PalindromeNumber {
    // Time Complexity: O(log n)
    // Space Complexity: O(n)
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int temp = x;
        int reverseNum = 0;
        while (temp > 0) {
            reverseNum = (reverseNum * 10) + (temp % 10);
            temp = temp / 10;
        }
        return reverseNum == x;
    }

    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public boolean isPalindromeBF(int x) {
        String num = Integer.toString(x);
        return num.equals(new StringBuilder(num).reverse().toString());
        // return num.equals(reverse(num));
    }
    
    public String reverse(String x) {
        String reverseNum = "";
        for (int i = x.length() - 1; i >= 0; i--) {
            reverseNum = reverseNum + x.charAt(i); 
        }
        return reverseNum;
    }

    public static void main (String args[]) {
        PalindromeNumber palindromeNumber = new PalindromeNumber();
        System.out.println(palindromeNumber.isPalindrome(121));
        System.out.println(palindromeNumber.isPalindrome(-121));
        System.out.println(palindromeNumber.isPalindrome(10));
    }
}
