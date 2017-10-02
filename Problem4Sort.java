import java.util.Arrays;

public class Problem4Sort {

	public static void main(String[] args)
	{
		int[] A = {4, 6, 1, 6, 8, 2, 5};
		
		sorta(A);
		
		System.out.println(Arrays.toString(A));
	}
	
	public static void sorta(int[] input)
	{
		if(input.length < 2) 
		{
			return;
		}
		
		int[] firstHalf = new int[input.length/2];
		int[] secondHalf = new int[(input.length+1)/2];
		int sh = 0;
		for(int i=0; i < input.length; i++)
		{
			if(i < input.length/2)
			{
				firstHalf[i] = input[i];
			}
			else
			{
				secondHalf[sh] = input[i];
				sh++;
			}
		}
		
		sorta(firstHalf);
		sorta(secondHalf);
		
		System.out.println("fh="+Arrays.toString(firstHalf));
		System.out.println("sh="+Arrays.toString(secondHalf));
		
		int BIGNUM = Integer.MAX_VALUE;
		int smallFH = arraymin(firstHalf, firstHalf.length, BIGNUM, -1);
		int smallSH = arraymin(secondHalf, secondHalf.length, BIGNUM, -1);

		for(int i=0; i < input.length; i++)
		{
			if(smallFH < smallSH)
			{				
				input[i] = smallFH;
				smallFH = arraymin(firstHalf, firstHalf.length, BIGNUM, -1);
			}
			else
			{
				input[i] = smallSH;
				smallSH = arraymin(secondHalf, secondHalf.length, BIGNUM, -1);
			}
		}
	}
	
	public static int arraymin(int[] array, int len, int smallest, int where)
	{
		if( len < 1)
		{
			return smallest;
		}
		
		if(array[len-1] < smallest)
		{
			if(where != -1)
			{
				array[where] = smallest;
			}
			smallest = array[len-1];
			where = len-1;
			array[len-1] = Integer.MAX_VALUE;
		}
		return arraymin(array, len-1, smallest, where);
	}
}
