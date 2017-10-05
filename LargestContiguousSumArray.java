import java.util.*;
import java.lang.*;
import java.io.*;

class LargestContiguousSumArray {
	public static void main (String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int test_cases = Integer.parseInt(br.readLine());

		for(int i = 0 ; i < test_cases ; i++){
			int input_len = Integer.parseInt(br.readLine());
			int[] num_array = new int[input_len];

			String[] input = br.readLine().split(" ");

			int max_so_far = -1000;
			int max_here = 0;

			for(int x = 0 ; x < input_len ; x++){
				num_array[x] = Integer.parseInt(input[x]);
				int element = num_array[x];

				System.out.println("Element " + input[x] + ", max_here " + max_here + ", max_so_far " + max_so_far);
				
				max_here = Math.max(max_here + element,element);
				max_so_far = Math.max(max_so_far, max_here);

				System.out.println("Element " + input[x] + ", max_here " + max_here + ", max_so_far " + max_so_far);
			}

			System.out.println(String.valueOf(max_so_far));
		}
	}
}