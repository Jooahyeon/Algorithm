class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
//      1. 배열로 문자의 위치를 파악
//      2. s번째 배열 + overwrite의 배열 갯수 파악
//      3. my_string의 문자열이 s번째 + overwrite배열의 갯수보다 큰 경우 이어 씀
//      (my_string > overwrite_String)  
        String answer = "";
        int a = my_string.length();
        int b = overwrite_string.length();
        
        answer = my_string.substring(0,s) + overwrite_string + my_string.substring(s+b,a);
        return answer;
    }
}