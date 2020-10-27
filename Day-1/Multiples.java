class Multiples {
	static void findMultiples(int n) {

		for (int i = 1; i <= n; i++) {
			String s = "";

			if (i % 3 == 0) {
				s = "Fizz";
			}

			// Found multiple of 5
			if (i % 5 == 0) {
				s = "Buzz";
			}
			if ((i % 3 == 0) && (i % 5 == 0)) {
				s = "FizzBuzz";
			}
			if (s == "")
				System.out.println(i);
			else
				System.out.println(s);
		}
	}

	public static void main(String[] args) {
		findMultiples(100);
	}
}
