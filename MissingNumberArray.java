import java.io.*;

class MissingNumberArray{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int test_cases = Integer.parseInt(br.readLine());

		for(int i = 0 ; i < test_cases ; i++) {
			int array_len = Integer.parseInt(br.readLine());
			int expected_sum = array_len * ( array_len + 1 ) / 2 ;
			int actual_sum = 0;

			String[] input_array = br.readLine().split(" ");
			for(int j = 0 ; j < input_array.length ; j++) {
				actual_sum += Integer.parseInt(input_array[j]); 
			} 

			System.out.println(String.valueOf(expected_sum - actual_sum));
		}
	}
}