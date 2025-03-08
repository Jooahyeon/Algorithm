import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        // BufferedReader의 예외처리 (IOException)


        // BufferedReader 객체 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력받을 정수 N 선언
        // String Line으로 Integer.parseInt를 통해 형변환 함
        int N = Integer.parseInt(br.readLine());
        br.close();

        for (int i = 1; i < 10; i++) {
            System.out.println(N + " * " + i + " = " + (N * i));
        }
    }
}
