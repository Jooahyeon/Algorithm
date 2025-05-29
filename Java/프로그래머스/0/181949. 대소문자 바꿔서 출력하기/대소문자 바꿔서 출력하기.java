import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String answer ="";
        
//         a가 대문자 -> 소문자, a가 소문자 -> 대문자
         for(int i=0; i < a.length(); i++){
            char c = a.charAt(i);
            
            if(Character.isUpperCase(c)) {
                answer += Character.toLowerCase(c);
            } else {
                answer += Character.toUpperCase(c);
            }
        }
        System.out.println(answer);
    }
}