import java.io.*;

class CountSort{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int test_cases = Integer.parseInt(br.readLine());

		for(int x = 0 ; x < test_cases ; x++){
			int[] count_array = new int[3];

			int input_len = Integer.parseInt(br.readLine());
			String input = br.readLine();

			for(int i = 0 ; i < input_len*2 ; i+=2){
				count_array[(int)input.charAt(i)-48] += 1;
				// System.out.println(i + " " + input.charAt(i));
			} 

			StringBuilder sb = new StringBuilder();
			for(int i = 0 ; i < 3 ; i++){
				// System.out.println(i + " " + String.valueOf(count_array[i]));
				while(count_array[i]>0){
					sb.append(String.valueOf(i) + " ");
					count_array[i] -= 1;
				}
			}
			System.out.println(sb.toString());
		}
	}
}