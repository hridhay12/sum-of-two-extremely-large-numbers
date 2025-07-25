# sum-of-two-extremely-large-numbers
Simple addition, unconventional input: handling enormous numbers stored as strings
🧮 Sum of Two Extremely Large Numbers
Simple addition, unconventional input: handling enormous numbers stored as strings.

📌 Overview
This Python solution adds two very large numbers represented as strings — numbers that could overflow standard data types. The twist? It's not just about addition, it's about treating digit characters as numerical values for accurate computation at scale.

🔍 Problem Statement
When two numbers are too large to be stored as integers, we represent them as strings and compute their sum manually — digit by digit, just like we learned in school… only faster.

Example Input:

python
str_num1 = "987654321987654321987654321"
str_num2 = "123456789123456789123456789"
Output:

"1111111111111111111111111110"
⚙️ How It Works
Convert each string into digits

Start from the least significant digit (rightmost)

Use carry-over logic to mimic human-style addition

Rebuild the resulting number as a string


🧪 Test It Yourself
Try it with different lengths, leading zeros, and even edge cases:

💡 Why It’s Cool
This isn’t just arithmetic — it’s problem-solving with constraints. Think competitive coding, interview prep, or real-world scenarios in cryptography and finance.
