import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String result = "";        // 결과 문자열을 담을 변수
        char c = ' ';               // 문자열을 char로 변환
        
        
        // a의 길이만큼 반복문
        for (int i = 0; i < a.length(); i++) {
            c = a.charAt(i);
          // 조건문으로 대문자이면 소문자, 소문자이면 대문자 구분
            if (Character.isUpperCase(c)) {
                // result에 변환한 값을 담아!
                result += Character.toLowerCase(c);
            } else {
                result += Character.toUpperCase(c);
          }  
      }
        System.out.print(result);
    }
}