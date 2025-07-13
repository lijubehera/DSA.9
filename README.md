#Day 9 of My LeetCode Journey — Problem: "Check if Any Element Has Prime Frequency" (Easy)

Today’s challenge was a nice mix of math + logic — and I loved every bit of it! 💪

📌 Problem Summary:
You're given an integer array, and you need to:
 🔍 Check if the frequency (i.e., count) of any element in the array is a prime number.
 If yes, return true. Otherwise, return false.

🧠 My Approach:
Frequency Count:
I used Python’s collections.Counter to count how many times each element appears.
Example: For [1, 2, 2, 3], the frequency is {1:1, 2:2, 3:1}.
Prime Number Check:
Created a helper function to check if a number is prime:
A number is prime if it's >1 and divisible only by 1 and itself.
Optimized the check to run up to √n for better performance.
Loop Through Frequencies:
Iterated over each frequency.

The moment I found a prime frequency, I returned true.
🔍 Sample Test Case:
📥 Input: [1, 2, 3, 4, 5, 4]
 📊 Frequencies: {1:1, 2:1, 3:1, 4:2, 5:1}
 ✅ Output: true → because 2 (frequency of 4) is a prime number.

🚀 What I Learned:
Refreshed my understanding of prime number checking.
Revisited and practiced using the Counter library efficiently.
Importance of writing helper functions for readability and reuse.
Always consider time complexity when checking primes.
